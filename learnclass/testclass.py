#!/usr/bin/env python

class TestStaticMethod:
    def foo():
        print 'calling static method foo()'        
    foo = staticmethod(foo)

class TestClassMethod:
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:',cls.__name__
    foo = classmethod(foo)

tsm = TestStaticMethod()
TestStaticMethod.foo()    # calling static method foo()
tsm.foo()                 #calling static method foo()

tcm = TestClassMethod()
TestClassMethod.foo()     #calling class method foo\n  foo() is part of class: TestClassMethod
tcm.foo()                 # 同上