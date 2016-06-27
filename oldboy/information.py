#!/usr/bin/python

name = raw_input("what are you name? :")
age = raw_input("how old are you? :")
job = raw_input("what are you job? :")

msg = """Informatoin of %s to below:
	Name : \033[42;1m%s\033[0m
	Age  : \033[32;1m%s\033[0m
	Job  : \033[46;1m%s\033[0m
""" % (name,name,age,job)

if int(age) >= 30:
	print "you are too old,just do job for ....."
else:
	print "you are still too young!"

print msg
