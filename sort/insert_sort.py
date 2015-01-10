#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys

def merger(arr,begin,mid,end):
	lf = arr[begin:mid]
	rg = arr[mid:end]
	lf[mid] = sys.maxint
	rg[end] = sys.maxint
	l=0
	r=0
	for i in range(begin,end):
		if lf[l] < rg[r]:
			arr[i] = lf[l]
			l+=1
		else:
			arr[i] =rg[r]
			r+=1

def merger_sort(arr,begin,end):
	if begin < end:
		mid = (begin+end)/2
		print arr[begin:mid]
		#assert arr[begin:mid] != [10]
		merger_sort(arr,begin,mid)
		merger_sort(arr,mid,end)
		merger(arr,begin,mid,end)

if __name__ =="__main__":
	arr=[10,8,4,-1,2,6,7,3]
	#print arr
	merger_sort(arr,0,len(arr))
	print "merger_sort is: ",arr