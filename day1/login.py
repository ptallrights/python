#!/usr/bin/env python
#coding=utf-8

while True:
	user = raw_input("please input your name:").strip()
	passwd = raw_input("please in put password:").strip()
	if len(user) == 0:
		print "Username is not be empty."
		continue
	elif len(passwd) == 0:
		print "Password is not be empty."
		continue
	else:
		print "Welecome %s come in the system." % user
