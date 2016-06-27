#!/usr/bin/env python

class Dog(object):
	a = 100
	def __init__(self,name):
		self.n = name

	@classmethod
	def cls_m(cls):
		print 'cls_m'

	@staticmethod
	def static_m(a,b):
		print a,b

Dog.static_m(3,4)

d = Dog(200)
d.static_m(1,2)
