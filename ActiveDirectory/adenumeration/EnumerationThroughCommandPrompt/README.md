# Users

- We can list all the users on the Active Directory domain by

```console
net user /domain
```

- We can also get information about a specific user

```console
net user <USERNAME> /domain
```

### Example
- In our case to list all users

```console
za\lynda.franklin@THMJMP1 C:\Users\lynda.franklin>net user /domain
The request will be processed at a domain controller for domain za.tryhackme.com.


User accounts for \\THMDC.za.tryhackme.com

-------------------------------------------------------------------------------
aaron.conway             aaron.hancock            aaron.harris
aaron.johnson            aaron.lewis              aaron.moore
aaron.patel              aaron.smith              abbie.joyce
abbie.robertson          abbie.taylor             abbie.walker
abdul.akhtar             abdul.bates              abdul.holt
abdul.jones              abdul.wall               abdul.west
abdul.wilson             abigail.cox              abigail.cox1
abigail.smith            abigail.ward             abigail.wheeler
adam.heath               adam.jones               adam.parker
adam.pugh                adam.reynolds            adam.woodward
Administrator            adrian.blake             adrian.chapman
adrian.foster            adrian.wilson            aimee.ball
aimee.dean               aimee.humphries          aimee.jones
aimee.potter             aimee.robinson           alan.brown
alan.jones               albert.elliott           albert.harrison
albert.hayes             albert.hunter            albert.lee
albert.stone             alex.burrows             alex.graham
alex.harris              alexander.hale           alexander.hill
alexander.sutton         alexandra.elliott        alexandra.harrison
alexandra.howard         alexandra.richards       alexandra.saunders
<--------------------------------snip------------------------------------>
tracy.macdonald          trevor.day               trevor.james
trevor.james1            trevor.newman            trevor.shaw
trevor.smith             trevor.stevens           trevor.thompson
vagrant                  valerie.davis            valerie.hawkins
valerie.jackson          valerie.lewis            vanessa.arnold
vanessa.collins          vanessa.harris           vanessa.jones
vanessa.newman           vanessa.peacock          vanessa.shepherd
victor.adams             victor.dixon             victor.edwards
victor.fisher            victor.perkins           victor.smith
victoria.jones           victoria.roberts         victoria.russell
victoria.savage          victoria.shaw            victoria.woodward
vincent.brooks           vincent.price            vincent.wood
vincent.young            wayne.bentley            wayne.harrison
wayne.henderson          wayne.walker             wayne.whitehouse
wendy.carpenter          wendy.evans              wendy.mills
wendy.roberts            wendy.taylor             wendy.whittaker
william.bailey           william.holmes           william.little
william.miah             william.payne            william.williams
yvonne.baker             yvonne.black             yvonne.craig
yvonne.grant             yvonne.johnson           yvonne.smith
zoe.barnes               zoe.ellis                zoe.fleming
zoe.hopkins              zoe.humphreys            zoe.lane
zoe.marshall             zoe.watson
The command completed successfully.

```

- Let's check details of `t0_tinus.green`

```console
za\lynda.franklin@THMJMP1 C:\Users\lynda.franklin>net user t0_tinus.green /domain
The request will be processed at a domain controller for domain za.tryhackme.com.

User name                    t0_tinus.green
Full Name                    T0 Tinus Green
Comment                      THM{Enumerating.Via.MMC}
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            3/16/2022 6:12:53 PM
Password expires             Never
Password changeable          3/16/2022 6:12:53 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   Never

Logon hours allowed          All

Local Group Memberships
Global Group memberships     *Tier 0 Admins        *Domain Users
The command completed successfully.

```

# Groups

- We can list all the groups on a domain with

```console
net group /domain
```

- We can also list details of a specific group by

```console
net group <GROUP NAME> /domain
```

### Example
- List all the groups

```console
za\lynda.franklin@THMJMP1 C:\Users\lynda.franklin>net group /domain
The request will be processed at a domain controller for domain za.tryhackme.com.


Group Accounts for \\THMDC.za.tryhackme.com

-------------------------------------------------------------------------------
*Cloneable Domain Controllers
*DnsUpdateProxy
*Domain Admins
*Domain Computers
*Domain Controllers
*Domain Guests
*Domain Users
*Enterprise Admins
*Enterprise Key Admins
*Enterprise Read-only Domain Controllers
*Group Policy Creator Owners
*HR Share RW
*Internet Access
*Key Admins
*Protected Users
*Read-only Domain Controllers
*Schema Admins
*Server Admins
*Tier 0 Admins
*Tier 1 Admins
*Tier 2 Admins
The command completed successfully.
```

- Details of a group

```console
za\lynda.franklin@THMJMP1 C:\Users\lynda.franklin>net group "Tier 1 Admins" /domain
The request will be processed at a domain controller for domain za.tryhackme.com.

Group name     Tier 1 Admins
Comment

Members

-------------------------------------------------------------------------------
t1_arthur.tyler          t1_gary.moss             t1_henry.miller
t1_jill.wallis           t1_joel.stephenson       t1_marian.yates
t1_rosie.bryant
The command completed successfully.


```

# Password Policy

- We can password policies of a domain with 

```console
net accounts /domain
```

### Example
```console
za\lynda.franklin@THMJMP1 C:\Users\lynda.franklin>net accounts /domain
The request will be processed at a domain controller for domain za.tryhackme.com.

Force user logoff how long after time expires?:       Never
Minimum password age (days):                          0
Maximum password age (days):                          Unlimited
Minimum password length:                              0
Length of password history maintained:                None
Lockout threshold:                                    Never
Lockout duration (minutes):                           30
Lockout observation window (minutes):                 30
Computer role:                                        PRIMARY
The command completed successfully.


```
