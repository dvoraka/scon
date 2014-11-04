#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

import subprocess
import readline
import sqlite3


class SConn:

    def __init__(self):

        self.data = {
            # hard coded data
            'server1': 'ssh root@servername',
            'server2': 'ssh -p 12345 user@servername2',
        }

        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.completer)

    def update(self):

        self.load_data()

    def print_db(self):

        print(self.data)

    def load_data(self):
        '''Load data from database.'''

        db_con = sqlite3.connect('scon.db')
        cursor = db_con.cursor()

        try:
            cursor.execute('SELECT * FROM commands')
            data = cursor.fetchall()

            for field in data:

                params = field[1]
                self.data[field[0]] = params

        except sqlite3.OperationalError as error:

            if error.args[0] == 'no such table: commands':

                print('Creating table...')
                try:

                    self.create_table(cursor)
                    db_con.commit()
                    db_con.close()
                    print('Table created.')

                except sqlite3.OperationalError as e:

                    print(e)

    def create_table(self, cursor):

        cursor.execute('CREATE TABLE commands(name text, attrs text)')

    def completer(self, text, state):

        choices = list(self.data.keys())
        results = [x for x in choices if x.startswith(text)] + [None]

        return results[state]

    def read_input(self):

        while True:

            string = input('scon> ')

            if string == 'q':

                break

            if string in self.data:

                command = self.data[string]
                if command.startswith('ssh '):

                    print(command)
                    subprocess.call(command, shell=True)

                else:

                    print('Unknown command!')

            else:

                print('Not found.')


def main():

    sc = SConn()
    sc.load_data()
    sc.read_input()


if __name__ == '__main__':

    main()
