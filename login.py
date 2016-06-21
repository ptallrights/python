#!/usr/bin/python
import sys

uaername = 'pt'
password = 'ok'
locked = 1
counter = 0

while counter < 3:
	user = raw_input("please input a name for you:").strip()
	if len(user) == 0:
		print '\033[31;1mUsername cannot be empty!\033[0m'
		continue
	passwd = raw_input("please input password:").strip()
	if len(passwd) == 0:
		print '\033[31;1mPassword cannot be empty!\033[0m'
		continue
	if locked == 0:
		print 'Your username is locked!'
		sys.exit()
	else:
		if user == uaername and passwd == password:
			sys.exit('welcome %s login to our system!' % user)
		else:
			counter += 1
