#!/usr/bin/env python

#def func_name():
#	return 'test'
#
##func = func_name
#func = func_name()
#
#print type(func)
#print type(func_name)
#
#a = func()

def func(f):
	print 'call func'
	f(3,5)

def func2(x,y):
	print 'call func2',x,y

func(func2)

func2(1,1)

def fun3(x):
	for i in range(x,0,-1):
		if i==0:
			return 0
		else:	
			return i

c = fun3(4)
print c
