#!/usr/bin/env python
#coding=utf-8

#try:
#	exp
#except:
#	exp
#finally:
#	exp

#raise IOError('error in IO')		#强制抛出一个异常并终止程序

#assert condition,message			#当condition为假时，抛出message信息并终止程序（条件判断）
#a = 2
#assert a==1,'a!=1'

#try:
#	a = [1,2]
#	print a[1]
#	raise IndexError('raise error')
#except Exception as e:
#	print 'except'
#	print e
#except NameError as e:
#	print e
#except IndexError as e:
#	pass
#finally:
#	print 'finally'
#
#print 'out try'

try:
	d = {}
	d['key']
	raise KeyError('key is not defined')
except Exception as e:
	print 'except error'
	print e
finally:
	print 'it is finally test'
