#!/usr/bin/env python
# from __future__ import print_function
import sys
import re
import string
import pprint

lastKey = None
currentlist = []

pp = pprint.PrettyPrinter(depth=6)

values = []

struct = { }

for input in sys.stdin.readlines():

	# For debugging only. You can also use CTRL + D to send EOF
	# Need to add: print the last set even if EOF is reached
	if input.rstrip() == "break":
		while(currentlist):
			for c in currentlist.pop(0): print c # , end=' ')
		sys.stdin.flush()
		sys.exit()

	# Separate values in tuple
	# print(input)

	
	
	temp = input.rstrip()

	inputKey, inputValue = temp.split('\t')
	# append.values(inputValue)
	# print inputKey
	
	
#for s in scores:
#  scorelist.append([scores[s][t] for t in topics])
	
	
	# insert(0,inputValue)
	
	# .append(inputValue)
	
	if (inputKey == lastKey):
		# Add to list
		currentlist.append(inputValue)
	else: 
		# Print current list item and create a new list
		# currentlist.insert(0, inputKey)
		# pp.pprint(currentlist)
		# while(currentlist):
		# for c in currentlist: print "c\t" #, end=' ')
		struct[inputKey] = currentlist
		currentlist = [inputKey, inputValue]

	# For debugging purposes only
	#print "currentlist is " + string.translate(str(currentlist), None, "'")

	lastKey = inputKey
	# d[scope_item].append(relation)
	#struct[inputKey].append(inputValue)

# pp.pprint(struct)

for k,v in struct.items():
    print '"' + k + '"\t' + "\t".join(v)
  