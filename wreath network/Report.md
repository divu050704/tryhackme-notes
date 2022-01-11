# Overview
1. There are three machines on the network
2. There is at least one public facing webserver
3. There is a self-hosted git server somewhere on the network
4. The git server is internal, so Thomas may have pushed sensitive information into it
5. There is a PC running on the network that has antivirus installed, meaning we can hazard a guess that this is likely to be Windows
6. By the sounds of it this is likely to be the server variant of Windows, which might work in our favour
7. The (assumed) Windows PC cannot be accessed directly from the webserver

# Enumeration
### Nmap scan
 ![nmap scan](https://github.com/divu050704/tryhackme-notes/blob/main/wreath%20network/Screenshots/nmap.png)

