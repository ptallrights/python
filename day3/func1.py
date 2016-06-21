#!/usr/bin/env python
import time
import datetime
#def func():
#	print "ext_func"
#	def inn_func():
#		print "inn_func"
#	return inn_func()
#
#print func()

#def func():
#	print "ext_func"
#	def inn_func():
#		print "inn_func"
#	return inn_func
#
#f = func()
#f()

#def func():
#	print "ext_func"
#	def inn_func(f):
#		start = datetime.datetime.now()
#		f()
#		end = datetime.datetime.now()
#
#		cost = end - start
#		print cost.total_seconds()
#
#	return inn_func
#
#def f2():
#	time.sleep(3)
#f = func()
#f(f2)


#def func(fc):
#	print "ext_func"
#	def inn_func(*arg):
#		start = datetime.datetime.now()
#		fc(*arg) #f2(arg)
#		end = datetime.datetime.now()
#
#		cost = end - start
#		print cost.total_seconds()
#
#	return inn_func
#
#def f2(arg):
#	print arg
#	time.sleep(arg)
#
#def f3(arg1,arg2):
#	print arg1,arg2
#	time.sleep(5)
#
#def f4():
#	time.sleep(6)
#
#f = func(f4)
#f()

#def func1(fc):
#	print "This is a function of boss."
#	print type(fc)
#	def func2(*arg):
#		print "This is a function in function."
#		print arg
#		fc(*arg)
#		print fc(*arg)
#	
#	return func2
#
#def f1(x,y):
#	return x*y
#
#f = func1(f1)
#f(3,5)

#def func1(fc):
#	print "This is a function of boss."
#	print type(fc)
#	def func2(arg1,arg2):
#		print "This is a function in function."
#		print arg1,arg2
#		fc(arg1,arg2)
#		print fc(arg1,arg2)
#	
#	return func2
#
#def f1(x,y):
#	return x*y
#
#f = func1(f1)
#f(4,5)
"""
def func1(fc):
	print "This is a function of boss."
	print type(fc)
	def func2(*arg):
		print "This is a function in function."
		print arg
		fc(arg)
		#print fc(*arg)
	
	return func2

def f1(arg):
	S = 1
	print len(arg)
	for i in range(len(arg)):
		S = S*arg[i]
	print S

f = func1(f1)
f(4,5,6,)
"""
"""
def func(fc):
	print "ext_func"
	def inn_func(*arg):
		start = datetime.datetime.now()
		fc(*arg) #f2(arg)
		end = datetime.datetime.now()

		cost = end - start
		print cost.total_seconds()

	return inn_func

@func
def f2(arg):
	print arg
	time.sleep(arg)
@func
def f3(arg1,arg2):
	print arg1,arg2
	time.sleep(5)

@func
def f4():
	time.sleep(6)

#f = func(f4)
#f()
#f2(3)		#fc = func(f2);fc(3)
f3(3,5)
"""

def check_priv(fc):

	def wrap(*arg,**kwargs):
		if username == 'admin':
			fc(*arg,**kwargs)
		else:
			print "Permission denied"
	return wrap

username = "admin"

@check_priv
def f6(arg):
	print arg
	print "restart nginx...",arg

f6('false')
