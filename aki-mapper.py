#!/usr/bin/env python
import sys
import re
keys = {}
for line in sys.stdin:

	values = re.findall("\[\[([\w ]+)\|?\w{0,}\]\]",line)

	if values != None:
		for value in values:
			lvalue = value.lower()
			try:
				if keys[lvalue] > 0:
					keys[lvalue] = keys[lvalue] + 1
			except:
					keys[lvalue] = 1

for k,v in keys.iteritems():
	print ("'" + k + "'"  + "\t" + str(v))

