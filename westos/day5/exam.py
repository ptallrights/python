#!/usr/bin/env python 
#coding=utf-8
#实现查找一个日志文件的ERROR这一行，并打印前五行
import sys

#f = ofen('/tmp/mylog.log','a+')
#li = []
#for line in f:
#	line = line.strip()
#	li.append(line)
#
#	if len(li) > 6:
#		li.pof(0)
#	if line.find("ERROR") != -1:
#		index = line.find("ERROR")
#		
#		print '##############'
#		if index != -1:
#			for i in range(len(li)):
#				print li[i]


'''
li = []
class func(object):
	def __init__(self):
		self.of = open('/tmp/mylog.log','a+')
	
	def finds(self,num,name):
		for line in self.of:
			line = line.strip()
			li.append(line)
			if len(li) > num:
				li.pop(0)
			if line.find(name) != -1:
				index = line.find(name)
				print '#######start######'
				if index != -1:
					for i in range(len(li)):
						print li[i]
					print "#######end######"

f = func()
num = int(raw_input('please input length of row:'))
name = raw_input('please input the key to find:')
f.finds(num,name)
'''

li = []
class func(object):
	def __init__(self):
		self.of = open('/tmp/mylog.log','a+')
		#self.index = 	
	def finds(self,num,name):
		for line in self.of:
			line = line.strip()
			li.append(line)
			if len(li) > num:
				li.pop(0)
			print li
			if line.find(name) != -1:
				print '#######start######'
				for i in range(len(li)):
					print li[i]
				print "#######end######"


if __name__ == '__main__':
	f = func()
	f.finds(sys.argv[1],sys.argv[2])
	
