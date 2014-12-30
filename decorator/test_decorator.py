#!/usr/bin/env python
import time

def now():
	return time.time()

print now()
print now.__name__