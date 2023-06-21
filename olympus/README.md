# What is flag 1?

- Started enumeration of this machine using `rustscan`.

![screenshot for rustscan](https://raw.githubusercontent.com/divu050704/assets-holder/main/tryhackme-screenshots/Screenshot%202023-06-21%20195222.png)


- As we can see there are two ports open on the machine `http` and `ssh` .
- Started `gobuster` on the web server for enumerating directories.

![screenshot for gobuster](https://raw.githubusercontent.com/divu050704/assets-holder/main/tryhackme-screenshots/Screenshot%202023-06-21%20195813.png)

- As we can see there is a directory as `~webmaster`. 
- Checked out the directory and found a login page

![screenshot for lgin page](https://raw.githubusercontent.com/divu050704/assets-holder/main/tryhackme-screenshots/Screenshot%202023-06-21%20200101.png)

- Connected this request to `burpsuite` and copied the request to a file named `req` and started `sqlmap` which found out that the service is vulnerable to SQL injection

![screenshot 1 for sqlmap](https://raw.githubusercontent.com/divu050704/assets-holder/b21a36f7c288d4689d215c91c33e5fb172f7f583/tryhackme-screenshots/Screenshot%202023-06-21%20201417.png)


- Then enumerated databases for this service, and found database named `olympus`, which seems to suspicious so started table enumeration on this service.

![screenshot for sqlmap](https://github.com/divu050704/assets-holder/blob/main/tryhackme-screenshots/Screenshot%202023-06-21%20201754.png?raw=true)

- Enumerated for columns in table named `flag`.

![screenshot 3 for sqlmap](https://github.com/divu050704/assets-holder/blob/main/tryhackme-screenshots/Screenshot%202023-06-21%20201836.png?raw=true)


- Then checked out flag in database `flag` and column `flag`. 

![screenshot 4 for sqlmap](https://github.com/divu050704/assets-holder/blob/main/tryhackme-screenshots/Screenshot%202023-06-21%20202227.png?raw=true)

# What is flag 2?

- Then started `sqlmap` for table `users`.

![screenshot 4 for sqlmap](https://raw.githubusercontent.com/divu050704/assets-holder/0855efedf975678e79d4f5b13243c1139c37a288/tryhackme-screenshots/Screenshot%202023-06-21%20202938.png)

- Then started enumeration for columns `user_name` and `user_password`. 

![screenshot for users table](https://github.com/divu050704/assets-holder/blob/main/tryhackme-screenshots/Screenshot%202023-06-21%20205915.png?raw=true)


- Cracked this hash (`bcrypt $2*$, Blowfish (Unix)`) with `hashcat`.

![screenshot of hashcat](https://raw.githubusercontent.com/divu050704/assets-holder/98040451518629fa11ef7864110f9ae9faef5725/tryhackme-screenshots/Screenshot%202023-06-21%20210013.png)

- On login found out new sub-domain in users section `chat.olympus.thm`. 

![screenshot for users](https://raw.githubusercontent.com/divu050704/assets-holder/f47536b65235eccb662dedc99555f6848fa63bdf/tryhackme-screenshots/Screenshot%202023-06-21%20210404.png)

- Added this subdomain to `/etc/hosts` file.
- On the home page we could see a chat in which we could upload files, and the third is talking about some random file name.

![screenshot of chats](https://github.com/divu050704/assets-holder/blob/main/tryhackme-screenshots/Screenshot%202023-06-21%20210802.png?raw=true)

- Uploaded a `php` reverse shell as we know that the current server is running with help of `php`. 
- Now all we need is a URL, we found a table named `chats` in the above enumeration so checked for columns in this table, using `sqlmap`.

![screenshot for chats columns](https://raw.githubusercontent.com/divu050704/assets-holder/b2584b99da27fd34a8f1a80f303dafdabacdd4ee/tryhackme-screenshots/Screenshot%202023-06-21%20211650.png)

- Found an interesting table named `file`, so enumerated it.

![screenshot for filenames](https://raw.githubusercontent.com/divu050704/assets-holder/528bbaba500f0355bf40dcacc2b1cfe7ec298b01/tryhackme-screenshots/Screenshot%202023-06-21%20212152.png)

- So used my gut that we data could be in `uploads` directory, so gave it a try and it was successful, got a reverse shell back.

![screenshot for reverse shell](https://raw.githubusercontent.com/divu050704/assets-holder/31bc99a61fdd20b59de118bdb52b904c7837baa5/tryhackme-screenshots/Screenshot%202023-06-21%20212257.png)

- Found flag in `/home/zeus/user.flag` 


# What is Flag 3?

- Checked for SUIDs and found a suspicious file `cputils`. 

![screenshot for SUIDs](https://raw.githubusercontent.com/divu050704/assets-holder/ab4695afdcdff94a5b203cfb540ded87468961af/tryhackme-screenshots/Screenshot%202023-06-21%20212706.png)

- Gave a test run to `cputils` and found it was a binary to copy files, so copied `id_rsa` to `/tmp`. 

![screenshot for copying id_rsa](https://raw.githubusercontent.com/divu050704/assets-holder/7573d85f1f2de3ca881d6ff8754ed97f8c1a5277/tryhackme-screenshots/Screenshot%202023-06-21%20213036.png)

- Copied this file to my attacking machine and cracked it using john.

![screenshot for ssh passphrase](https://raw.githubusercontent.com/divu050704/assets-holder/8013f64c41f625700c7fcd6522511f648a1a2a8a/tryhackme-screenshots/Screenshot%202023-06-21%20213536.png)

- Logged in the ssh using passphrase.

![ssh login](https://raw.githubusercontent.com/divu050704/assets-holder/5cd3d3cc15ce4f2c93eca6c42c8fdd717792be7a/tryhackme-screenshots/Screenshot%202023-06-21%20213733.png)

- We can see there is some backdoor file, so searched for it, and found a suspicious file in `/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc`. 

![screenshot for backdoor](https://raw.githubusercontent.com/divu050704/assets-holder/39d94338db3a544e95544071c165484c5486096e/tryhackme-screenshots/Screenshot%202023-06-21%20214139.png)

- We can see a file in as `$suid_bd` `/lib/defended/libc.so.99`. 
- Gave it a try and we were root.

![screenshot for root](https://raw.githubusercontent.com/divu050704/assets-holder/6dc81475211a55356f9103a6919b7f642ea01b3c/tryhackme-screenshots/Screenshot%202023-06-21%20214355.png)


# What is Flag 4?

- We can see in hint that flag is in `The flag is located in /etc/` . 
- Used grep to search file.

![screenshot for final flag](https://raw.githubusercontent.com/divu050704/assets-holder/7d171952ef72727a074f7602d4b4ce421ee15702/tryhackme-screenshots/Screenshot%202023-06-21%20214806.png)
