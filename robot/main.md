# Enumeration
## Nmap
```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-10 20:33 IST
Nmap scan report for 10.10.214.175
Host is up (0.18s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE  SERVICE VERSION
22/tcp  closed ssh
80/tcp  closed http
443/tcp closed https

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.44 seconds
```
## Gobuster
```
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.6.84
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
2022/05/11 20:47:35 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 213]
/.hta.php             (Status: 403) [Size: 217]
/.htaccess            (Status: 403) [Size: 218]
/.htaccess.php        (Status: 403) [Size: 222]
/.htpasswd            (Status: 403) [Size: 218]
/.htpasswd.php        (Status: 403) [Size: 222]
/0                    (Status: 301) [Size: 0] [--> http://10.10.6.84/0/]
/admin                (Status: 301) [Size: 232] [--> http://10.10.6.84/admin/]
/atom                 (Status: 301) [Size: 0] [--> http://10.10.6.84/feed/atom/]
/audio                (Status: 301) [Size: 232] [--> http://10.10.6.84/audio/]  
/blog                 (Status: 301) [Size: 231] [--> http://10.10.6.84/blog/]   
/css                  (Status: 301) [Size: 230] [--> http://10.10.6.84/css/]  
```
# Attack
1. Found robot.txt in which a file `fsociety.dic` was found and found *First Flag* .
2. Found to be a password file.
3. Brute forces the username with Hydra found out to be `Elliot`.
4. Brute forced password with Hydra and fsocity.dic and found password to be `ER28-0652`.
5. Logged in and edited 404.php with a reverse shell.
6. Executed script by a going to a wrong page and got a reverse shell.
7. Found another MD5 password file in `/home/robot`.
8. Cracked the password and changed user to robot and read the file with *Second Key*.
9. Loaded linpeas.sh and found `nmap` to suspective.
10. Started a shell with `nmap --interactive` followed by `!sh`.
11. Got a root shell.
