#!/usr/bin/env python

import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
	n = int(s)
	#	1
	#	print '>>> n = %d' % n
	#	2
	#	assert n != 0, 'n is zero'

	#	3
	#logging.info('n = %d' % n)
	return 10 / n

def main():
	foo('0')

main()