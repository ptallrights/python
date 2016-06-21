#!/usr/bin/env python

li = [1,2,3,4,5,6,7,8,9,10]

def afilter(func,lii):
	li = []
	for i in lii:
		if func(i):
			li.append(i)
	return li


def  f1(x):
	if x%2 == 0:
		return True

a = afilter(f1,li)
print a

def mymap(func,lii):
	li = []
	for i in lii:
		if func(i):
			li.append(func(i))
	return li

def f2(y):
	return y*2

b = mymap(f2,li)
print b

def myreduce(func,lii):
	lis = lii[0]
	for i in range(len(lii)-1):
		#print ok,lii[i+1]
		lis = func(lis,lii[i+1])
	return lis

def f3(x,y):
	return x*y

c = myreduce(f3,li)
print c
