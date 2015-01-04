#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#一个简单的re实例，匹配字符串中的hello字符串
import re

m = re.match(r'hello', 'hello world!')
print m.group()

