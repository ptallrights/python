#!/usr/bin/env python
#coding=utf-8
#编程规范，示例如下：

#class Hello(object):
#	'''test doc
#		example:
#	'''
#	a = 100 #this is a number for a
#	#this is a number for b
#	b = 200
#	c = ['a','b']   #or 分行写
#	d = {
#			'key1':'v1',
#			'key2':'v2',
#			'key3':'v3'
#	}
#
#	def __init__(self,num,m):
#		self.age = num
#		self.__money = m
#
#	def test(self):
#		return 100
#
#	def echo_info(self):
#		print self.test()
#
#	def __eq__(self,other):
#		return self.age == other.age
#
#	def __add__(self,other):
#	#	return self.age + other.age
#		return Hello(self.age + other.age,0)
#
#	def __str__(self):
#		return 'age =%d' % self.age
#
#	def __del__(self):	#析构函数，在整个类调用执行完后会执行
#		print 'world'
#
#d = Hello(2,200)
#d2 = Hello(3,100)
#
##d.echo_info()
#print d == d2
##s = d + d2			#s = Hello(d.age + d2.age,0)
##print s.age
#
#print d
#print d2

class Information(object):
	'''This is a doc
		example for test,please don't change it.
	'''

	def __init__(self,sch,cla,m,n):
		print "welecome to school system."
		self.school = sch
		self.classroom = cla
		self.num = 100
		self.__money = m
		self.num = n

	def school_name(self):
		return self.school

	def class_name(self):
		return self.classroom

	def class_money(self):
		return self.__money

	def __eq__(self,another):
		return self.__money == another.__money

	def __gt__(self,another):
		return self.__money > another.__money

	def __ne__(self,another):
		return self.__money != another.__money

	def __add__(self,another):
		return self.__money + another.__money
		#return Information('jiaoda','dz1302',self.__money + another.__money)
		#return Information('jiaoda','dz1302',1024,self.num + another.num)

	def __str__(self):
		return 'money = %d' % self.__money

	def __hash__(self):
		return 1314521

	def __getattr__(self,name):
		print "get attr %s" % name
		return name

	def __del__(self):
		print "Goodbye,welecom here again."

f = Information('youdian','tg1312',9999,6)
l = Information('ligong','jk1213',6666,4)
#print f.school_name()
#print f.class_name()
#print f.class_money()
print f == l
print f + l
print f > l

s = f + l
print s
print f.ccc

#===========================
#welecome to school system.
#welecome to school system.
#False
#welecome to school system.
#money = 1024 Goodbye,welecom here again.
#
#True
#welecome to school system.
#10
#get attr ccc
#ccc
#Goodbye,welecom here again.
#Goodbye,welecom here again.
#Goodbye,welecom here again.

