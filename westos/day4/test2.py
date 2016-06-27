#!/usr/bin/env python

class Cat():
	def __init__(self,name,age,color):
		self.name = name
		self.age = age
		self.color = color

	def eat(self):
		print self.name,"is eating......"

	def sleep(self):
		print "sleeping,please don't call me"

	def push(self):
		print self.name,'is push three laoshu'

mery = Cat('mery',2,'white')
tom = Cat('tom',4,'black')

print tom.name
tom.eat()

def test():
	print 'okok'

tom.test = test
tom.test()
