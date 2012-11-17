#!/usr/bin/env python
from __future__ import print_function
import sys
import re
import string

lastKey = None
currentlist = []

for input in sys.stdin.readlines():

	# For debugging only. You can also use CTRL + D to send EOF
	# Need to add: print the last set even if EOF is reached
	if input.rstrip() == "break":
		while(currentlist):
			for c in currentlist.pop(0): print(c, end=' ')
		sys.stdin.flush()
		sys.exit()

	# Separate values in tuple
	inputKey, inputValue = input.rstrip().split(r":")

	if (inputKey == lastKey):
		# Add to list
		currentlist.append(inputValue)
	else: 
		# Print current list item and create a new list
		while(currentlist):
			for c in currentlist.pop(0): print(c, end=' ')

		currentlist = [inputKey, inputValue]

	# For debugging purposes only
	#print "currentlist is " + string.translate(str(currentlist), None, "'")

	lastKey = inputKey
