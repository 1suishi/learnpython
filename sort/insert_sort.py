#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def insert_sort(a):
	a_len = len(a)
	for i in range(a_len):
		key = a[i]
		j=i
		while(j>0 and key < a[j-1]):
			a[j] = a[j-1]
			j-=1
		a[j] = key


if __name__ == '__main__':
	nums = [10,8,4,-1,2,6,7,3]
	print 'nums is:', nums
	insert_sort(nums)
	print "insert sort is : ",nums