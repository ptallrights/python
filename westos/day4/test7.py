#!/usr/bin/env python

class World(object):
	
	def __init__(self,name,nation):
		self.name = name
		self.nation = nation
		self.__money = 10000000000

	def flag(self):
		print self.__money
		return self.name
	@property
	def action(self):
		return self.nation
	@action.setter
	def action(self,num):
		self.nation = num

f = World('Asia','China')
print f.flag()

print f.action

f.action = 'India'
print f.action
