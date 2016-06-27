#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def func_name(*arg):
	#print arg
	print arg[0],'<===>',arg

def cat(arg,arg1,*arg2,**arg3):
	print "下面是一个测试的结果："
	print "arg:",arg
	print "arg1:",arg1
	print "*arg2:",arg2
	print "**arg3:",arg3

cat([1,2],3,5,4,7,9,8,age=23,**{'key':'values','name':'tom'})

#func_name('who','are','you','haha')
li = [2,4,6,8,10]
func_name(li)	#([2,4,6,8,10],)
func_name(*li)	#func_name(2,4,6,8,10)====>(2,4,6,8,10)

li2 = ['a','b','c','d']

func_name(*li2)
