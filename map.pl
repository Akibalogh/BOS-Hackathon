#!/usr/bin/perl

while (<>) {
	my @tmp = split("\t",$_);
	next if ($tmp[6] eq 'nan' || $tmp[8] eq 'nan' );
	print "$tmp[6]\t$tmp[8]\n";
}

1;
