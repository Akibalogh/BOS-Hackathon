#!/usr/bin/perl

while (<>) {
	%seen{$_}++;
	if ($seen{$_} == 1) {
		print $_;
	}
	#if ($_ =~ /^TRAA/) {
	#	print $_ , "\n";
	#}
}

1;
