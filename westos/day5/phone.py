#!/usr/bin/env python

class Phone(object):

	def __init__(self,size,color,memory):
		self.size = size
		self.color = color
		self.memory = memory

	def call(self):
		s = 'I can call'
		return s
	def sms(self):
		s = 'Are you gua le mei?'
		return s

class Phones(Phone):

	def __init__(self,size,color,memory,pix):
		self.pix = pix
		super(Phones,self).__init__(size,color,memory)

	def install_app(self,app):
		s = 'install %s' % app
		return s

class Huwei(Phone):

	def weixin(self,msg):
		if msg.find('gcd') == -1:
			return 'sending....'
		else:
			return 'You can\'t send the msg'

p = Phone(1.2,'black','4M')

iphone = Phones(4.7,'white','4G','1280*766')

h = Huwei(4.7,'yellow','4G')

print iphone.install_app('weixin')

print h.sms()
print h.call()
print h.weixin('wansui')
sms = p.sms()
call = p.call()
print sms,call
