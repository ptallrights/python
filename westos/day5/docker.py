#!/usr/bin/env python

class Resource(object):
	def __init__(self):
		print 'call me resource init'

	def __new__(cls,*args,**kwargs):
		print "resource new"
		return object.__new__(cls,*args,**kwargs)

class DockerResource(Resource):
	def __new__(cls,*args,**kwargs):
		print "call me docker resource new"
		return Resource.__new__(cls,*args,**kwargs)

	def __init__(self):
		print 'call docker resource init'

	def test(self):
		print 'dosker resource test'

r = DockerResource()
print r
print type(r)
r.test()
