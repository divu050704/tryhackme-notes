# Introduction
- We already have `AD-RSAT` installed on the system so we will use the default on with [these](https://docs.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps) list of commands.
- We can also use other `cmdlets` like [PowerView](https://github.com/PowerShellEmpire/PowerTools/tree/master/PowerView)

# Users

- We can get enumerate a specific users by

```console
Get-ADUser -Identitiy <Username> -Properties * -Server <DC>
```
> Identity - Here Identity is the user which we would like to enumerate
> Properties - It is the properties we would like to see (* means all of them)
> Server - It is the domain of Domain Control 

- We can also use `filter` tag to search for a user.

```console
Get-ADUser -Filter "<Property> like '<Data>'"
```

- With Filter tag we can also use `Format-Table` to make a table name by specifying column name with Properties

```console
Get-ADUser -Filter "<Propoerty> like '<Data>'" | Format-Table <Properties> -A
```

### Example
- For looking a specific user

```console
PS C:\Users\lynda.franklin> Get-ADUser -Identity zoe.marshall -Properties *  -Server za.tryhackme.com


AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : za.tryhackme.com/People/Finance/zoe.marshall
Certificates                         : {}
City                                 :
CN                                   : zoe.marshall
codePage                             : 0
Company                              :
CompoundIdentitySupported            : {}
Country                              :
countryCode                          : 0
Created                              : 2/24/2022 10:06:06 PM
createTimeStamp                      : 2/24/2022 10:06:06 PM
Deleted                              :
Department                           : Finance
Description                          :
DisplayName                          : Zoe Marshall
DistinguishedName                    : CN=zoe.marshall,OU=Finance,OU=People,DC=za,DC=tryhackme,DC=com
Division                             :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {1/1/1601 12:00:00 AM}
EmailAddress                         :
EmployeeID                           :
EmployeeNumber                       :
Enabled                              : True
Fax                                  :
GivenName                            : Zoe
HomeDirectory                        :
HomedirRequired                      : False
HomeDrive                            :
HomePage                             :
HomePhone                            :
Initials                             :
instanceType                         : 4
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 0
LastLogonDate                        :
LockedOut                            : False
logonCount                           : 0
LogonWorkstations                    :
Manager                              :
MemberOf                             : {CN=Internet Access,OU=Groups,DC=za,DC=tryhackme,DC=com}
MNSLogonAccount                      : False
MobilePhone                          :
Modified                             : 2/24/2022 10:06:06 PM
modifyTimeStamp                      : 2/24/2022 10:06:06 PM
msDS-User-Account-Control-Computed   : 0
Name                                 : zoe.marshall
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Person,CN=Schema,CN=Configuration,DC=za,DC=tryhackme,DC=com
ObjectClass                          : user
ObjectGUID                           : 4c9ef9c2-5f2f-45cb-82e7-973e343bf3fb
Office                               :
OfficePhone                          :
Organization                         :
OtherName                            :
PasswordExpired                      : False
PasswordLastSet                      : 2/24/2022 10:06:06 PM
PasswordNeverExpires                 : False
PasswordNotRequired                  : False
POBox                                :
PostalCode                           :
PrimaryGroup                         : CN=Domain Users,CN=Users,DC=za,DC=tryhackme,DC=com
primaryGroupID                       : 513
PrincipalsAllowedToDelegateToAccount : {}
ProfilePath                          :
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 132902139669207850
SamAccountName                       : zoe.marshall
sAMAccountType                       : 805306368
ScriptPath                           :
sDRightsEffective                    : 0
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-3330634377-1326264276-632209373-2463
SIDHistory                           : {}
SmartcardLogonRequired               : False
sn                                   : Marshall
State                                :
StreetAddress                        :
Surname                              : Marshall
Title                                : Mid-level
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 512
userCertificate                      : {}
UserPrincipalName                    :
uSNChanged                           : 25310
uSNCreated                           : 25306
whenChanged                          : 2/24/2022 10:06:06 PM
whenCreated                          : 2/24/2022 10:06:06 PM
```

- For Searching properties(Name) match or is like a string.

```console
PS C:\Users\lynda.franklin> Get-ADUser -Filter "Name -like '*.brown'"   | Format-Table GivenName , Name -A

GivenName Name
--------- ----
Barry     barry.brown
Suzanne   suzanne.brown
Alan      alan.brown
Pauline   pauline.brown
Katherine katherine.brown
Dorothy   dorothy.brown
Allan     allan.brown
Stanley   stanley.brown
Bruce     bruce.brown     
Lindsey   lindsey.brown
Jane      jane.brown
Jay       jay.brown
Lucy      lucy.brown
Leon      leon.brown
Laura     laura.brown
Lawrence  lawrence.brown
Gregory   gregory.brown
Kimberley kimberley.brown
Joyce     joyce.brown
Maria     maria.brown
Thomas    thomas.brown
Brandon   brandon.brown
Ian       ian.brown
Kim       kim.brown
```

# Groups
- We can read details of a specific group by

```console
Get-ADGroup -Identity <GROUPNAME>
```

- We can get details of a group members with

```console
Get-ADGroupMember -Identity <GroupName>
```

### Example 
- Read details of a group

```console
PS C:\Users\lynda.franklin> Get-ADGroup -Identity "Tier 1 Admins"


DistinguishedName : CN=Tier 1 Admins,OU=Groups,DC=za,DC=tryhackme,DC=com
GroupCategory     : Security
GroupScope        : Global
Name              : Tier 1 Admins
ObjectClass       : group
ObjectGUID        : 96a07816-4218-40c1-8224-5051645aa2cc
SamAccountName    : Tier 1 Admins
SID               : S-1-5-21-3330634377-1326264276-632209373-1105

```

- Read details of group members

```console
PS C:\Users\lynda.franklin> Get-ADGroupMember -Identity "Tier 1 Admins"  | Format-Table *

distinguishedName                                               name               objectClass objectGUID                           SamAccountName     SID
-----------------                                               ----               ----------- ----------                           --------------     ---
CN=t1_arthur.tyler,OU=T1,OU=Admins,DC=za,DC=tryhackme,DC=com    t1_arthur.tyler    user        77f38ece-c0dd-4991-b02b-3365f64ff539 t1_arthur.tyler    S-1-5-21-3330634377-13262642...
CN=t1_henry.miller,OU=T1,OU=Admins,DC=za,DC=tryhackme,DC=com    t1_henry.miller    user        d15c1146-6fef-40f5-82d3-beed3aad89bc t1_henry.miller    S-1-5-21-3330634377-13262642...
CN=t1_gary.moss,OU=T1,OU=Admins,DC=za,DC=tryhackme,DC=com       t1_gary.moss       user        7de2e387-b70f-4c78-9709-2b3d13be159a t1_gary.moss       S-1-5-21-3330634377-13262642...
CN=t1_jill.wallis,OU=T1,OU=Admins,DC=za,DC=tryhackme,DC=com     t1_jill.wallis     user        5267ea24-623e-4dd4-91aa-50c936b576fb t1_jill.wallis     S-1-5-21-3330634377-13262642...
CN=t1_marian.yates,OU=T1,OU=Admins,DC=za,DC=tryhackme,DC=com    t1_marian.yates    user        c150fdff-2de0-4a8d-ae2f-b335b442e272 t1_marian.yates    S-1-5-21-3330634377-13262642...
CN=t1_rosie.bryant,OU=T1,OU=Admins,DC=za,DC=tryhackme,DC=com    t1_rosie.bryant    user        8f5e9057-0e9c-4d74-b8af-0d4fe1b25219 t1_rosie.bryant    S-1-5-21-3330634377-13262642...
CN=t1_joel.stephenson,OU=T1,OU=Admins,DC=za,DC=tryhackme,DC=com t1_joel.stephenson user        2d6bea54-92f7-4b3a-adbc-c5668ef76d98 t1_joel.stephenson S-1-5-21-3330634377-13262642...

```

# ADObjects
- We can search for Active Directory Objects using different filter like, all AD Objects which were changed after a specific date

```console
PS C:\Users\lynda.franklin> Get-ADObject -Filter 'whenChanged -gt $ChangeDate' -includeDeletedObjects -Properties *  | Format-Table Name, whenChanged, whenCreated

Name                                   whenChanged            whenCreated
----                                   -----------            -----------
za                                     11/10/2022 11:59:45 AM 2/24/2022 9:57:28 PM
Administrator                          6/7/2022 2:47:23 PM    2/24/2022 9:57:34 PM
vagrant                                3/16/2022 6:59:42 PM   2/24/2022 9:57:34 PM
THMDC                                  11/9/2022 9:57:44 PM   2/24/2022 9:58:38 PM
Domain Admins                          3/16/2022 6:38:55 PM   2/24/2022 9:58:38 PM
RID Manager$                           5/18/2022 4:49:38 PM   2/24/2022 9:58:48 PM
RID Set                                5/18/2022 4:49:38 PM   2/24/2022 9:58:48 PM
Servers                                3/16/2022 6:19:44 PM   2/24/2022 10:04:40 PM
Workstations                           3/16/2022 6:43:56 PM   2/24/2022 10:04:40 PM
Admins                                 3/16/2022 6:10:35 PM   2/24/2022 10:04:41 PM
Tier 0 Admins                          3/16/2022 6:55:58 PM   2/24/2022 10:04:41 PM
roy.perry                              3/28/2022 8:54:58 AM   2/24/2022 10:04:41 PM
denise.jenkins                         5/31/2022 8:02:53 PM   2/24/2022 10:04:41 PM
gemma.lyons                            6/6/2022 6:11:01 PM    2/24/2022 10:04:41 PM
kerry.murray                           6/8/2022 3:19:08 PM    2/24/2022 10:04:41 PM
darren.davis                           6/8/2022 6:42:22 PM    2/24/2022 10:04:42 PM
kenneth.davies                         11/9/2022 11:14:36 PM  2/24/2022 10:04:42 PM
graeme.williams                        11/9/2022 11:32:54 PM  2/24/2022 10:04:42 PM
lynda.franklin                         11/10/2022 4:11:03 AM  2/24/2022 10:04:42 PM
rachel.dunn                            11/10/2022 7:32:12 AM  2/24/2022 10:04:42 PM
mandy.bryan                            11/10/2022 9:56:26 AM  2/24/2022 10:04:42 PM
t2_henry.taylor                        3/16/2022 6:11:24 PM   2/24/2022 10:04:45 PM
t2_sophie.davies                       3/16/2022 6:11:24 PM   2/24/2022 10:04:53 PM
t2_brian.wilson                        3/16/2022 6:11:24 PM   2/24/2022 10:04:53 PM
t2_christian.goodwin                   3/16/2022 6:11:24 PM   2/24/2022 10:05:00 PM
t2_chloe.carter                        3/16/2022 6:11:24 PM   2/24/2022 10:05:02 PM
t2_victor.fisher                       3/16/2022 6:11:24 PM   2/24/2022 10:05:17 PM
t1_arthur.tyler                        3/16/2022 6:11:18 PM   2/24/2022 10:05:20 PM
philip.clements                        3/21/2022 11:41:23 AM  2/24/2022 10:05:21 PM
t2_philip.clements                     3/21/2022 11:41:00 AM  2/24/2022 10:05:21 PM
t2_jane.oneill                         3/16/2022 6:11:24 PM   2/24/2022 10:05:28 PM
t1_henry.miller                        11/9/2022 10:27:47 PM  2/24/2022 10:05:29 PM
t2_natasha.scott                       3/16/2022 6:11:24 PM   2/24/2022 10:05:44 PM
t2_craig.iqbal                         3/16/2022 6:11:24 PM   2/24/2022 10:05:56 PM
t1_gary.moss                           3/16/2022 6:11:18 PM   2/24/2022 10:05:56 PM
t2_gerard.davis                        3/16/2022 6:11:24 PM   2/24/2022 10:06:00 PM
t2_zoe.watson                          3/16/2022 6:11:24 PM   2/24/2022 10:06:03 PM
t1_jill.wallis                         3/16/2022 6:11:18 PM   2/24/2022 10:06:10 PM
t2_tom.bray                            3/16/2022 6:11:24 PM   2/24/2022 10:06:10 PM
t2_marian.yates                        3/16/2022 6:11:24 PM   2/24/2022 10:06:12 PM
t1_marian.yates                        3/16/2022 6:11:17 PM   2/24/2022 10:06:12 PM
t2_jeremy.leonard                      3/16/2022 6:11:24 PM   2/24/2022 10:06:20 PM
t1_rosie.bryant                        3/16/2022 6:11:17 PM   2/24/2022 10:06:25 PM
georgina.edwards                       4/29/2022 11:13:07 PM  2/24/2022 10:06:39 PM
t1_joel.stephenson                     3/16/2022 6:11:17 PM   2/24/2022 10:06:42 PM
gordon.stevens                         4/29/2022 11:13:07 PM  2/24/2022 10:06:44 PM
hollie.powell                          4/29/2022 11:13:07 PM  2/24/2022 10:06:45 PM
heather.smith                          4/29/2022 11:13:07 PM  2/24/2022 10:06:46 PM
THMIIS                                 11/9/2022 9:57:54 PM   2/27/2022 10:52:02 AM
THMMDT                                 11/9/2022 10:07:08 PM  2/28/2022 5:50:34 PM
THMMDT-Remote-Installation-Services    2/28/2022 7:10:38 PM   2/28/2022 7:10:15 PM
Contoso                                2/28/2022 7:35:22 PM   2/28/2022 7:35:22 PM
ZA                                     2/28/2022 7:47:59 PM   2/28/2022 7:37:04 PM
Accounts                               2/28/2022 7:37:04 PM   2/28/2022 7:37:04 PM
Computers                              2/28/2022 7:37:04 PM   2/28/2022 7:37:04 PM
Groups                                 2/28/2022 7:37:05 PM   2/28/2022 7:37:04 PM
Admins                                 2/28/2022 7:37:04 PM   2/28/2022 7:37:04 PM
Service Accounts                       2/28/2022 7:37:04 PM   2/28/2022 7:37:04 PM
Users                                  2/28/2022 7:37:04 PM   2/28/2022 7:37:04 PM
Servers                                2/28/2022 7:37:04 PM   2/28/2022 7:37:04 PM
Workstations                           2/28/2022 7:37:05 PM   2/28/2022 7:37:04 PM
Security Groups                        2/28/2022 7:37:05 PM   2/28/2022 7:37:05 PM
svcMDT                                 3/16/2022 7:11:26 PM   2/28/2022 7:53:08 PM
svcLDAP                                3/16/2022 7:11:02 PM   3/1/2022 11:44:06 AM
svcAV                                  3/16/2022 7:10:06 PM   3/5/2022 6:49:09 PM
svcFileCopy                            11/9/2022 10:06:45 PM  3/6/2022 9:22:29 AM
THMJMP1                                11/9/2022 10:00:00 PM  3/16/2022 11:26:00 AM
T0                                     3/16/2022 6:10:35 PM   3/16/2022 6:10:35 PM
T1                                     3/16/2022 6:10:53 PM   3/16/2022 6:10:53 PM
T2                                     3/16/2022 6:11:03 PM   3/16/2022 6:11:03 PM
t0_tinus.green                         3/21/2022 8:17:47 AM   3/16/2022 6:12:53 PM
{7F070CE4-1DC6-4006-9749-54D32D8D729F} 3/16/2022 6:34:24 PM   3/16/2022 6:19:44 PM
Machine                                3/16/2022 6:19:44 PM   3/16/2022 6:19:44 PM
User                                   3/16/2022 6:19:44 PM   3/16/2022 6:19:44 PM
{EF776176-2518-429A-A779-93BE7F22A7AE} 3/16/2022 6:35:26 PM   3/16/2022 6:34:13 PM
Machine                                3/16/2022 6:34:13 PM   3/16/2022 6:34:13 PM
User                                   3/16/2022 6:34:13 PM   3/16/2022 6:34:13 PM
{6BD8D1FC-852C-41B2-8D76-BD80B653D7F1} 3/16/2022 6:44:36 PM   3/16/2022 6:43:56 PM
Machine                                3/16/2022 6:43:56 PM   3/16/2022 6:43:56 PM
User                                   3/16/2022 6:43:56 PM   3/16/2022 6:43:56 PM
```

- We can also check bad Password Counts for a user so that we can do a password spray attack.

```console
PS C:\Users\lynda.franklin> Get-ADObject -filter "badPwdcount -gt 0" -Properties * | Format-Table Name, badPwdCount

Name              badPwdCount
----              -----------
henry.taylor                1
frank.fletcher              1
henry.black                 1
mark.oconnor                1
dawn.hughes                 1
joanne.davies               1
alan.jones                  1
maria.sheppard              1
sophie.blackburn            1
gordon.stevens              1
dominic.elliott             1
louise.talbot               1
jennifer.wood               1
frances.chapman             1
dawn.turner                 1
samantha.thompson           1
anthony.reynolds            1
```

# Domains
We can get information about domains with 

```console
Get-ADDomain -Sever <DOMAIN-NAME>
```

### Example

```console
PS C:\Users\lynda.franklin> Get-ADDomain -Server za.tryhackme.com


AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=za,DC=tryhackme,DC=com
DeletedObjectsContainer            : CN=Deleted Objects,DC=za,DC=tryhackme,DC=com
DistinguishedName                  : DC=za,DC=tryhackme,DC=com
DNSRoot                            : za.tryhackme.com
DomainControllersContainer         : OU=Domain Controllers,DC=za,DC=tryhackme,DC=com
DomainMode                         : Windows2012R2Domain
DomainSID                          : S-1-5-21-3330634377-1326264276-632209373
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=za,DC=tryhackme,DC=com
Forest                             : za.tryhackme.com
InfrastructureMaster               : THMDC.za.tryhackme.com
LastLogonReplicationInterval       :
LinkedGroupPolicyObjects           : {CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=za,DC=tryhackme,DC=com}
LostAndFoundContainer              : CN=LostAndFound,DC=za,DC=tryhackme,DC=com
ManagedBy                          :
Name                               : za
NetBIOSName                        : ZA
ObjectClass                        : domainDNS
ObjectGUID                         : 518ee1e7-f427-4e91-a081-bb75e655ce7a
ParentDomain                       :
PDCEmulator                        : THMDC.za.tryhackme.com
PublicKeyRequiredPasswordRolling   :
QuotasContainer                    : CN=NTDS Quotas,DC=za,DC=tryhackme,DC=com
ReadOnlyReplicaDirectoryServers    : {}
ReplicaDirectoryServers            : {THMDC.za.tryhackme.com}
RIDMaster                          : THMDC.za.tryhackme.com
SubordinateReferences              : {DC=ForestDnsZones,DC=za,DC=tryhackme,DC=com, DC=DomainDnsZones,DC=za,DC=tryhackme,DC=com, CN=Configuration,DC=za,DC=tryhackme,DC=com}
SystemsContainer                   : CN=System,DC=za,DC=tryhackme,DC=com
UsersContainer                     : CN=Users,DC=za,DC=tryhackme,DC=com
```

# Altering AD-Objects
We can change passwords of other users.
```console
PS C:\Users\lynda.franklin> Set-ADAccountPassword -Identity lynda.franklin -OldPassword (ConvertTo-SecureString -AsPlaintext "Vbwg6014" -force) -NewPassword (ConvertTo-SecureString -A
sPlaintext "Password123" -Force
```

