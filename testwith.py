#!/usr/bin/env python 

class A:
	def __enter__(self):
		print 'in enter'
	def __exit__(self, type, value, trace):
		print 'in exit'

with A() as a:
	print 'in with'
