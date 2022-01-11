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
On using nmap on the machine we found 4 ports open on the machine. ssh on port 22, http on port 80, zeus-admin on port 9090, and Webmin Server in port 10000.We can see the machine is running on Cent OS.
### Website
On pasting the ip adress(10.200.187.200) in browser the page tries to redirect us to a virtual domain (https://thomaswreath.thm/). After changing aur hosts file we found some personal data of Mr. Thomas Wreath on the webapage which could be possibly used for a phishing attack. Some of the data is given below:-

