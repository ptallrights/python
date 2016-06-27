#!/usr/bin/env python 
#coding=utf-8
#实现查找一个日志文件的ERROR这一行，并打印前五行

#f = open('/tmp/mylog.log','a+')
#li = []
#for line in f:
#	line = line.strip()
#	li.append(line)
#
#	if len(li) > 6:
#		li.pop(0)
#	if line.find("ERROR") != -1:
#		index = line.find("ERROR")
#		
#		print '##############'
#		if index != -1:
#			for i in range(len(li)):
#				print li[i]

of = open('/tmp/mylog.log','a+')
li = []
class func(object):
	def __init__(self,op):
		self.op = op
	
	def finds(self,num,name):
		for line in self.op:
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

f = func(of)
num = int(raw_input('please input length of row:'))
name = raw_input('please input the key to find:')
f.finds(num,name)
