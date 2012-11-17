#!/usr/bin/env python
from __future__ import print_function
import sys
import re
import string

lastKey = None
currentlist = []
keys = {}

for input in sys.stdin.readlines():

	# Separate values in tuple
	inputKey, inputValue = input.rstrip().split("\t")
	
	values = keys.get(inputKey.rstrip(),[])
	values.append (inputValue)
	keys[inputKey.rstrip()] = values

for k,v in keys.iteritems():
 print ("'" + k + "'"  + "\t" + "\t".join(v))