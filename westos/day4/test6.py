#!/usr/bin/env python
import datetime

class Dog(object):

	def __init__(self,n):
		self.n = n
		self.__a = None

	@property
	def open_f(self):
		return self.__a == None

	@open_f.setter
	def open_f(self,value):
		self.__a = value

d = Dog(22)
print d.open_f

d.open_f = 'ok'
print d.open_f

print "#######################"
class Timef(object):
	def __init__(self):
		self.__time = datetime.datetime.now()
	@property
	def time(self):
		return self.__time.strftime('%Y-%m-%d %H:%M:%S')

	@time.setter
	def time(self,value):
		self.__time =datetime.datetime.strptime(value,'%Y-%m-%d %H:%M:%S')

t = Timef()

print t.time    #qubieyu print t.time() <dangyou@propertyshi,zuoweishuxing>

t.time = '2016-06-17 00:00:00'
print t.time


print "######################"

class Hello(object):
	def __init__(self,num):
		self.mon = num
		self.rmb = 111
	@property
	def money(self):
		print self.rmb
		return self.mon
	@money.setter
	def money(self,value):
		self.mon = value

m = Hello(50)
print m.money

m.money = 25
print m.money
