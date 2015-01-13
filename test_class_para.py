#!/usr/bin/env python
# -*-coding: utf-8-*-

class A(object):
	x=1
	def show(x):
		return x

if __name__ == '__main__':
	print A.x
	a= A()
	print a.x