#!/usr/bin/env python

import time


def log(func):
	def wrapper(*args,**kw):
		print "call begin"
		var =  func(*args , **kw)
		return var
	print "call end"
	return wrapper


@log
def now():
	return time.time()

print now()


