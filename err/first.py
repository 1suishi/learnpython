#!/usr/bin/env python
try:
	x = input("Enter the first number: ")
	y = input("Enter the sencond number: ")
	print x/y
except ZeroDivisionError:
	print "the sencond number can't be zero!"
except TypeError, e:
	print "That wasn't a number,was it?"

print 'End'