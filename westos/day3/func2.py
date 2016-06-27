#!/usr/bin/env python
import time
import datetime
import functools

#"""
#def func():
#	start = datetime.datetime.now()
#	time.sleep(4)
#	end = datetime.datetime.now()
#
#	cost = end - start
#	print cost.total_seconds()
#
#func()
#"""
#"""
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
#@func
#def f2(arg):
#	print arg
#	time.sleep(arg)
#@func
#def f3(arg1,arg2):
#	print arg1,arg2
#	time.sleep(5)
#
#@func
#def f4():
#	time.sleep(6)
#
##f = func(f4)
##f()
##f2(3)		#fc = func(f2);fc(3)
#f3(3,5)
#"""

#def check_priv(fc):
#
#	def wrap(*arg,**kwargs):
#		if username == 'admin':
#			fc(*arg,**kwargs)
#		else:
#			print "Permission denied"
#	return wrap
#
#username = "admin"
#
#@check_priv
#def f6(arg):
#	print arg
#	print "restart nginx...",arg
#
#f6('ok')

def func_boss(func):
	print "This is a function boss"
	@functools.wraps(func)
	def func_son(*arg,**kwargs):
		print "This is a function son"
		func(*arg)
		print "Ending"
	return func_son

S = 1
@func_boss
#func_test = func_boss(func_test)
def func_test(*arg):
	print "This is a function test"	
	#S = 1
	global S
	for i in range(len(arg)):
		S = S*arg[i]
	print S
	return S

#func_test(1,2,3,4)
#func_test()

a = func_test

print a.__name__
