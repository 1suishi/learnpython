#!/usr/bin/env python
# -*-coding: utf-8 -*- 


class Messenger:
     def __init__(self, **kwargs):
         self.__dict__ = kwargs
m = Messenger(info="some information", b=['a', 'list'])
m.more = 11
print m.info, m.b, m.more