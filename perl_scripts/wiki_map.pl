#!/usr/bin/perl

while (<>) {
     if ($_ =~ /<title>(*.)<\/title>\s/) {
		print $1 , "\n";	     
     }
}