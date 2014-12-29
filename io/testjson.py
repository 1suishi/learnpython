#!/usr/bin/env python

# can't name my own file json.py
# because there is a module named json
# this will cause the module can't be import

import json
d = dict(name = "Bob" , age ="20", score = 88)
print json.dumps(d)
