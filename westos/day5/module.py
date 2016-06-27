#!/usr/bin/env python
#coding=utf-8
# docs.python.org	python官方文档网站

def test():
	print 'This is a test'

def test2():
	print 'test2'

class DB(object):
	def __init__(self):
		self.a = 101
	def test(self):
		return self.a
