#!/usr/bin/env python
# from __future__ import print_function
import sys
# import re
import string
# import pprint

lastKey = None
currentlist = []

# pp = pprint.PrettyPrinter(depth=6)

values = []

struct = { }

for input in sys.stdin.readlines():
	
	temp = input.rstrip()

	inputKey, inputValue = temp.split('\t')
	
	if (inputKey == lastKey):
		# Add to list
		currentlist.append(inputValue)
	else: 

		struct[inputKey] = currentlist
		currentlist = [inputKey, inputValue]

	# For debugging purposes only
	#print "currentlist is " + string.translate(str(currentlist), None, "'")

	lastKey = inputKey


for k,v in struct.items():
    print '"' + k + '"\t' + "\t".join(v)
    