#!/usr/bin/env python
x = input("Enter the first number: ")
y = input("Enter the sencond number: ")

try:
	print x/y
except ZeroDivisionError:
	print "the sencond number can't be zero!"

print 'End'