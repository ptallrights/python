#!/usr/bin/env python

class Of(object):

	def __new__(cls,*args,**kwargs):
		print 'new'
		return super(Of,cls).__new__(cls,*args,**kwargs)
		#return object.__new__(cls,*args,**kwargs)

	def __init__(self):
#		self.f = open('/tmp/test.log','w')
		print "init"

	def test(self):
		print 'hello'

#	def __enter__(self):
#		self.test()
#		return self.f
#
#	def __exit__(self,*excinfo):
#		self.f.close()
#
#with Of() as f:
#	f.write('okokok\n') 

f = Of()
