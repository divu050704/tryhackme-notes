# Access the web server, who robbed the bank?

> Spiderman

# What is the Joomla version?

> 3.7.0 

- Checked `/administrator/manifests/files/joomla.xml` and found the version to be `3.7.0`. 

![screenshot for joomla version](https://raw.githubusercontent.com/divu050704/assets-holder/03ca820a0ebc4957f367d33ba380529adebfe0ba/tryhackme-screenshots/Screenshot%202023-06-27%20195051.png)

# What is Jonah's cracked password?

> spiderman123

- Found `joomla 3.7.0` to be vulnerable to `CVE-2017-8917`. 
- Used [this](https://github.com/stefanlucas/Exploit-Joomla/blob/master/joomblah.py) exploit to get username and password.

![screenshot for joomla exploit](https://raw.githubusercontent.com/divu050704/assets-holder/b4299df62eacdaf7eee065e8125a8108510765db/tryhackme-screenshots/Screenshot%202023-06-27%20195807.png)

- Saved this to a hash file and checked its hash type.

![screenshot for hash type](https://raw.githubusercontent.com/divu050704/assets-holder/1c46db05766a05a27e2ab5567156846f8d12eb57/tryhackme-screenshots/Screenshot%202023-06-27%20195956.png)

- Cracked hash with `3200`.

![screenshot hash cracked](https://raw.githubusercontent.com/divu050704/assets-holder/5870433dd402efba030460315b4d7e72d897d900/tryhackme-screenshots/Screenshot%202023-06-27%20204416.png)


# What is the user flag?

> 27a260fe3cba712cfdedb1c86d80442e

- Logged in to `joomla` with credentials cracked above.
- Wen to [http://10.10.180.105/administrator/index.php?option=com_templates&view=template&id=506&file=L2luZGV4LnBocA%3D%3D](http://10.10.180.105/administrator/index.php?option=com_templates&view=template&id=506&file=L2luZGV4LnBocA%3D%3D) and edited this code to my php-reverse-shell code. 
- Accessed the IP address and got back a reverse shell

![screenshot for reverse shell](https://raw.githubusercontent.com/divu050704/assets-holder/4f9354822374b1d8771ece87a4fd21da186a4187/tryhackme-screenshots/Screenshot%202023-06-27%20200741.png)

- We can get a username `jjameson` from the `/home` directory.
- Checked `joomla` configuration file and found password for `mysql` which was reused as `jjameson`. 

![screenshot jjameson password](https://raw.githubusercontent.com/divu050704/assets-holder/136aa4a6d722f80aa83f2cc545ad1c45f9fc136a/tryhackme-screenshots/Screenshot%202023-06-27%20201100.png)

- Secure shelled as `jjameson` and found user flag.

![screenshot for user flag](https://raw.githubusercontent.com/divu050704/assets-holder/52741698e4682b633b9c9956f3fbf47c6e17a524/tryhackme-screenshots/Screenshot%202023-06-27%20201609.png)

# What is root flag?

> eec3d53292b1821868266858d7fa6f79

- Checked `sudo` rights for user `jjameson`  and found `yum` to be able to run without password.
- Found an exploit on `gtfobins`. 

![screenshot for root](https://raw.githubusercontent.com/divu050704/assets-holder/7a7d8f0d423b250a12b8316bffefa1fcb23ea32f/tryhackme-screenshots/Screenshot%202023-06-27%20202157.png)

