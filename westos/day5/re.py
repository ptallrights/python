#!/usr/bin/env python

class Resource(object):

	def __new__(cls,*args,**kwargs):
		print 'class resource __new__'
		obj = super(Resource,cls).__new__(cls,*args,**kwargs)
		print obj.__class__
		return obj

	def __init__(self):
		print "call me init for Resource"

	def test(self):	
		print "call me test for Resource"

	def create(self):
		print "call me create for Resource"

#class subResource(object):
class subResource(Resource):
	
	def __init__(self):
		print 'sub resource init'

	def test(self):
		print 'sub resource test'

class Heat(object):

	def __new__(cls,*args,**kwargs):
		print "class __new__ %s" % cls
		return object.__new__(cls,*args,**kwargs)
		
	def __init__(self):
		print 'heat init'


r = Heat()
print r
h = Resource()
print h
f = subResource()
print f
