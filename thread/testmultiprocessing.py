#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'benniuo'

'''
test multiprocessing
fork
'''
import os

print 'Process (%s) start ...' % os.getpid()

pid = os.fork()

print pid

if pid == 0:
	print 'I am child Process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
	print 'I (%s) just create a child Process (%s).' % (os.getpid(), pid) 