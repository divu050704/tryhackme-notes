# Enumaeration
## Internet Protocol
```
10.10.197.159
```
## Nmap scan
A http sever and ms-wbt-server found to be running on ports 80 and 3389 respectively.
## Gobuster scan
Checked robots.txt and found one of the possible passwords.
Found the administrator name by googling poem written in one of the page.
Found email of the administrator to be SG@anthem.com.
# Attack
1. RDP  to the machine with username `sg` and password `UmbracoIsTheBest!`.
2. Found user.txt on the Desktop.
3. Found backup file in C://backups.
4. Change permission of the file and found the administrator password.
5. Escalated the previlage and accessed the C://User/Administrator Folder and found `root.txt` in the Desktop of the Administrator.
