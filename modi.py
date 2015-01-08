#!/usr/bin/env python
# -*- coding: utf-8 -*-

def decorator(func):
    print "hello"
    print func
    return func

@decorator
def foo():
    pass

print foo