1. Nmap scan shows `80` as an interesting port.
2. On enumeration on web using gobutser found `/cloud` to upload files.
3. It perevents the uploading of unwanted file by checking file extension, but we can bypass it by adding an extra space and image extension behind the filename, for e.g. `http://<YOUR-IP>/reverse.php .jpg`.
4. Got a reverse shell, and found `dataset.kdbx` in `/opt`.    
5. Downloaded it to local machine and bruteforced it using `john` and `rockyou.txt`.
6. Secure shelled into the machine as `sysadmin`.
7. Found a script in `/home/sysadmin` which was making backups and excuting as root, but didn't have write access.
8. Using require file created a reverse shell.
9. Got root flag.
