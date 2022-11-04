# Enumeration

## `cat /proc/version` and `uname -a`
These command can be used to see system information
```console
karen@wade7363:/$ cat /proc/version
Linux version 3.13.0-24-generic (buildd@panlong) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014
karen@wade7363:/$ uname -a
Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

## ps Command
`ps aux` Command can be used to see running services on the system for all users.
```console
karen@wade7363:/$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.2  0.5  33604  2960 ?        Ss   07:36   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    07:36   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    07:36   0:00 [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    07:36   0:00 [kworker/0:0]
root         5  0.0  0.0      0     0 ?        S<   07:36   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        S    07:36   0:00 [kworker/u30:0]
root         7  0.0  0.0      0     0 ?        S    07:36   0:00 [rcu_sched]
root         8  0.0  0.0      0     0 ?        R    07:36   0:00 [rcuos/0]
root         9  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/1]
root        10  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/2]
root        11  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/3]
root        12  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/4]
root        13  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/5]
root        14  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/6]
root        15  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/7]
root        16  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/8]
root        17  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/9]
root        18  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/10]
root        19  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/11]
root        20  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/12]
root        21  0.0  0.0      0     0 ?        S    07:36   0:00 [rcuos/13]
```

**1. What is the hostname of the target?**<br />
*wade7363*
```console
karen@wade7363:/$ hostname
wade7363

```



