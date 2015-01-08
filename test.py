#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import uuid, time

def next_id(t=None):
	if t is None:
		t = time.time()
	return '%015d     %s000' % (int (t*1000),uuid.uuid4().hex)

print next_id()