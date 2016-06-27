#!/usr/bin/env python
# _*_ coding:utf-8 _*_

print "你好,开始练习"
def func_name(arg,arg1,arg2,arg3='ok',arg4='?'):
	print arg,arg1,arg2,arg3,arg4

ARG = raw_input("please input your idea:")
func_name('what','are','you',arg3=ARG)

def login(user,passwd):
	if len(user) == 0:
		print "Name is not be empty"
	elif len(passwd) < 6:
		print "password is not be short"
	else:
		print "Welocome you come in the system,%s" % user



User = raw_input("please input your name:")
Passwd = raw_input("please input your password:")
login(User,Passwd)	
