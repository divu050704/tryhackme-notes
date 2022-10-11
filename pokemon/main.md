## Ip Address 
- 10.10.22.228

## Enemuration
#### Nmap
Found two ports open
1. ssh - 22
2. http- 80

#### Http 
Found user and password for ssh in the source code

## Attack
1. Logged in with the credentials `pokemon:hack_the_pokemon`.
2. Found grass-type in Desktop folder.
3. Found water-type in /var/www/html/water-type.txt
 - The data was encoded in rot-13 shift
4. Found fire-type in `/etc/why_am_i_here?/`
 - The data was encoded in base64 format.
5. Uploaded linpeas from the local machine and started enumerating.
 - Nothing interesting found
6. In home directory found the `roots-pokemon.txt` file.
7. On reading found permission denied but ash can read the file.
8. Found `.cplusplus` file in `/home/pokemon/Videos/Gotta/Catch/Them/ALL!`.
9. On readind found the credentials for ash.
10. Changed user and read the file

