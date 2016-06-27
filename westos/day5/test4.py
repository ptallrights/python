#!/usr/bin/env python
#MRO

class A(object):
	def __init__(self):
		pass
	def m(self):
		print 'a.ma'

class B(object):
	def m(self):
		print 'b.mb'

class C(A,B):
	pass

c = C()
c.m()
