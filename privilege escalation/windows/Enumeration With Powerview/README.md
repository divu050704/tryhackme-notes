# Powerview
- Powerview is a powershell script which is used for enumerating domain after a shell access to the machine.
- Cheat-sheet for this script can be found [here](https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993)

# Process

- Start Powershell with bypass flag value

```console
controller\administrator@DOMAIN-CONTROLL C:\Users\Administrator>powershell -ep bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Administrator> 
```

- Start `PowerView.ps1` script

```console
PS C:\Users\Administrator\Downloads> .\PowerView.ps1
```
- Import module from script

```console
PS C:\Users\Administrator\Downloads> Import-Module .\PowerView.ps1
```


- Enumerate domain users.

```console
PS C:\Users\Administrator\Downloads> Get-NetUser | Format-Table name,displayName

name                displayName
----                -----------
Administrator
Guest
krbtgt
Machine-1           Machine-1
Admin2              Admin2
Machine-2           Machine-2
SQL Service         SQL Service
POST{P0W3RV13W_FTW} POST{P0W3RV13W_FTW}
sshd                sshd
```



