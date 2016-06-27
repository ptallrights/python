#!/usr/bin/env python

class Tom(object):

	def __init__(self,name):
		self.name = name
		self.a = 100
		self.b = None
		self.__c = 300

	def test1(self):
		print self.name
		self.b = 200
		print 'test1',self.b

	def test2(self,age):
		self.age = age
		print 'test2',self.age
		self.__test3()

	def __test3(self):
		print self.a
	
	def print_c(self):
		print self.__c

t = Tom('jerry')
t.test1()
t.test2(21)

def test4(num):
	print 'test4',num

t.exam = test4
t.exam(225)

t.print_c()
