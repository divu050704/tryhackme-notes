# User flag

- Started enumeration by scanning the ports open on the machine using `rustscan`.

![screenshot for ruststcan](https://raw.githubusercontent.com/divu050704/assets-holder/e1d8e0ff50d0bb5d640ec3eb2f004fb29764edde/tryhackme-screenshots/image.png)

- Found samba port open, checked if I can list shares without passwords and it was successful.
- Found extra share named `datasci-team`.

![screenshot for samba](https://raw.githubusercontent.com/divu050704/assets-holder/e116ef7761191ada992548ba63a247d1b40e0b5a/tryhackme-screenshots/Screenshot%202023-06-18%20182655.png)

- Connected to `datasci-team` and downloaded all the files.


![screenshot for share](https://raw.githubusercontent.com/divu050704/assets-holder/6fcfce18ae1a66d1e4b842b625c2723e90918b7e/tryhackme-screenshots/Screenshot%202023-06-18%20183145.png)

- Found a jupyter token on the samba share.
- We know from the `rustscan` that there is a `jupyter` port running on the machine.
- Logged in with the token and started a new terminal.
- But this is a linux machine, but we saw in the `rustscan` that this was a windows machine, so checked the system info, and found out we were in a WSL (Windows Subsystem for Linux).

![screenshot for wsl](https://raw.githubusercontent.com/divu050704/assets-holder/9379000d99afc48e9ee6102cac6783a2a46ed645/tryhackme-screenshots/Screenshot%202023-06-18%20183534.png)

- We can go to windows machine from `/mnt/c` but it seems that it is not mounted and we need to be root to mount the drive.
- Checked for commands that the current user can run as `sudo`.
- Found that we could run `/home/dev-datasci/.local/bin/jupyter` and `/bin/su dev-datasci -c ` as root. 
- But there was no file `/home/dev-datasci/.local/bin/jupyter`.

![sudo screenshot](https://raw.githubusercontent.com/divu050704/assets-holder/4980c287d9f23ad24fff10c5cb458e6422f8e4db/tryhackme-screenshots/Screenshot%202023-06-18%20184248.png)

- So copied `/bin/bash` to `/home/dev-datasci/.local/bin/jupyter`and started as root. 

![screenshot for root](https://raw.githubusercontent.com/divu050704/assets-holder/c9dc9d7af6716eaafccb46c6dd030d7146fca053/tryhackme-screenshots/Screenshot%202023-06-19%20165022.png)

- Now mounted `C:` to `/mnt/c`

![screenshot for mounted drive](https://raw.githubusercontent.com/divu050704/assets-holder/1a583fa47e051faa55e76fd0e144ffe36e785596/tryhackme-screenshots/Screenshot%202023-06-19%20165526.png)

- Found user flag.

![screenshot for user flag](https://raw.githubusercontent.com/divu050704/assets-holder/547cfffc5f130e65dc5c03604f328cf36d438137/tryhackme-screenshots/Screenshot%202023-06-19%20165728.png)

# Root flag

![screenshot for root flag](https://raw.githubusercontent.com/divu050704/assets-holder/54616ba797554aa1634cee4a7c6c3f4d3a66d61d/tryhackme-screenshots/Screenshot%202023-06-19%20165935.png)

