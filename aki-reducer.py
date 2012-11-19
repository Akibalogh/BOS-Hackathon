#!/usr/bin/env python
from __future__ import print_function
import sys
import re
import string

lastKey = None
currentlist = []
keys = {}

for input in sys.stdin.readlines():

	inputKey, inputValue = input.rstrip().split("\t")
	
	try:
		if keys[inputKey] > 0:
			keys[inputKey] = keys[inputKey] + int(inputValue)
	except:
		keys[inputKey] = int(inputValue)

for k,v in sorted( keys.iteritems() , key=lambda item: -item[1] ):
	if v == 1:
		continue
	print ( k   + "\t" + str(v))


