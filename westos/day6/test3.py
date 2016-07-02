#!/usr/bin/env python

from collections import namedtuple

def namedtuple2():
	class People():
		def __init__(self,id,name,age,add,phone):
			self.id = id
			self.name = name
			self.add = add
			self.age = age
			self.phone = phone
	return People

if __name__ == '__main__':
	try:
		p = namedtuple2()
		r = p(11,'tom',21,'xixili',13456877)
	
		print r.id
		print r.phone
		print r.name
	except Exception as e:
		print e
