scon
====

Small utility for connecting to servers.

```
$ ./scon.py
scon> # tab
server1  server2  home  office
scon> server # tab
server1  server2  
scon> server
Not found.
scon> server2
('ssh', '-p 12345', 'user@servername2') # debug output
ssh: Could not resolve hostname servername2: Name or service not known
scon> home
('ssh', u'user@172.16.0.15')
user@172.16.0.15's password:

The programs included with the Ubuntu system are free software;
...

user@172.16.0.15:~$ exit
logout
Connection to 172.16.0.15 closed.
scon> office # or with key

The programs included with the Ubuntu system are free software;
...

worker@cooloffice:~$ exit
logout
Connection to 10.0.13.137 closed.
scon> 
```
