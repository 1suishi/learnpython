#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'begin call'
			print '%s %s():' % (text, func.__name__)
			func(*args,**kw)
			print 'end call'
		return wrapper
	return decorator

@log('execute')
#@log()
def now():
	print '2015-01-08'



if __name__ == '__main__':
	now()
	print now