#!/usr/bin/env python
try:
	f = open("../err/first.py" , 'r')
	print f.read()
finally:
	if f:
		f.close()