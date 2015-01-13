#!/usr/bin/env python
# -*-coding: utf-8-*-

def ma(cls):   
	print'method a' 

def mb(cls):   
	print'method b' 

method_dict = {   
'ma': ma,   
'mb': mb,   
}

def hello(x):
	print x


class T(object):
    x = 2;
    def show(x):
        print x

class DynamicMethod(type):   
    def __new__(cls, name, bases, dct):
        '''
        print 'name: ' ,name
        print 'bases: ' ,bases
        print 'dct: ' , dct
        '''
        if name[:3] =='Abc':
            dct.update(method_dict)

        return type.__new__(cls, name, bases, dct)

    
    #def __init__(cls,name,bases,dct):
        #super(DynamicMethod,cls).__init__(name,bases,dct)

class AbcTest(object):   
    __metaclass__ = DynamicMethod

    def mc(self, x):   
		print x * 3 

class NotAbc(object):   
    #__metaclass__ = DynamicMethod

    def md(self, x):   
		print x * 3 

def main(): 
    #pass
    print AbcTest

    a = AbcTest()

    print a
    print a.ma()

    #AbcTest.ma()
    #AbcTest.mc()
    #a.mc(3)   
    #a.ma()
    #print dir(a)

    #b = NotAbc()
    #print dir(b)   

if __name__ == '__main__':   
    main()
    '''
    print 
    print dir(AbcTest)
    print
    print dir(hello)
    print 
    print dir(T)
'''