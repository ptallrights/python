#!/usr/bin/env python

#class Dog(object):
#	a = 100
#
#	def test(self):
#		self.b = 200
#		print 'test'
#d = Dog()
#d2 = Dog()
#
#d.a = 300
#print Dog.a
#print d.a
#print d2.a

class Dog(object):
	a = 100

	def test(self):
		self.b = 200
		print 'test'

	@classmethod
	def test2(cls,name):
		print name
		cls.b = 300
		print cls.a
		print 'test2'

Dog.test2('tom')
print Dog.b

d = Dog()
d.test2('tom')
print d.b
