#!/usr/bin/env python
#coding=utf-8
#Num = raw_input("please input people number:")

#for i in Num:
Name = raw_input("please input your name:")
Age = raw_input("please input your age:")
School = raw_input("please input your school:")
print "%s is bulid in dict" % Name
di = {'name':Name,'age':Age,'school':School}

def dict(**kwarg):
	if kwarg.has_key('age'):
		for k,v in kwarg.items():
			print k,v 
	else:
		print 'ok'
	print kwarg

dict(**di)
