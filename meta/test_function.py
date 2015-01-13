#!/usr/bin/env python
# -*-coding: utf-8-*-

class A():
    @staticmethod
    def test_static():
        print "static"
    def test_normal(self):
        print "normal"
    @classmethod
    def test_class(cls):
        print "class", cls

a = A()
A.test_static()
A.test_class()
a.test_static()
a.test_normal()
a.test_class()