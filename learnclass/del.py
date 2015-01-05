#!/usr/bin/env python
class Person():
    population=0
    def __init__(self,name):
        self.name=name
        #print 'my name\' is %s' % self.name
        Person.population+=1
    def sayHi(self):
        print 'hello everyone,my name\' is %s'% self.name
    def howMany(self):
        if Person.population==1:
            print "I am the only one here"
        else:
            print "we have %d people here" % Person.population
    def __del__(self): 
        print '%s say bye,' % self.name
        Person.population-=1
        if Person.population==0:
            print 'I am the last one here'
        else:
            print 'we still have %d people here' % Person.population
john=Person('john')
john.sayHi()
john.howMany()     

smith=Person('smith')
smith.sayHi()
smith.howMany()

del john
del smith
