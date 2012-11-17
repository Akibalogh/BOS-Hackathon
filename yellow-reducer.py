#!/usr/bin/env python
from __future__ import print_function
import sys
import re
import string

lastKey = ""
currentKey = None
keycount = 0
loopcount = 0
inputKey = ""

for input in sys.stdin.readlines():

	if loopcount == 0:
		lastKey = inputKey
		keycount = 1
		loopcount = 1

	# Separate values in tuple
	inputKey, inputValue = input.rstrip().split("\t")

	if inputKey ==  lastKey:
		keycount = keycount + 1
	else:
		print (str(keycount) + "\t" + lastKey)
		keycount = 1
		lastKey = inputKey
