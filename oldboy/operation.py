#!/usr/bin/python
#coding:utf-8

from __future__ import division

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mult(x,y):
	return x*y

def div(x,y):
	return x/y

#def operator(x,o,y):
#	if o == "+":
#		print add(x,y)
#	elif o == "-":
#		print sub(x,y)
#	elif o == "*":
#		print mult(x,y)
#	elif o == "/":
#		print div(x,y)
#	else:
#		pass
#
#x = int(raw_input("please input first number:"))
#y = int(raw_input("please input second number:"))
#o = raw_input("please input operator:")
#operator(x,o,y)

operator = {"+":add,"-":sub,"*":mult,"/":div}

x = int(raw_input("please input first number:"))
y = int(raw_input("please input second number:"))
o = raw_input("please input operator:")
#print operator[o](x,y)
print operator.get(o)(x,y)
