#!/usr/bin/env python
import sys
import os

li = []
liff = []
class func(object):

	def __init__(self,filename):
		self.of = open(filename,'a+')


	def finds(self,key):
		for line in self.of:
			line = line.strip()
			li.append(line)
			if len(li) > 6:
				li.pop(0)
			if line.find(key) != -1:
				print '#######start######'
				for i in range(len(li)):
					print li[i]
				print "#######end######"
		self.of.close()	
		

class Judge(object):

	def __init__(self,filepath):
		self.filepath = filepath

	def dpath(self):
		if os.path.isdir(self.filepath):
			res = True
		else:
			print 'The file path is not find'
			res = False
		return res

	def fexist(self):
		filelist = os.listdir(self.filepath)
		for i in filelist:
			fy = os.path.splitext(i)
			if fy[1] == '.log':
				result = True
			else:
				result = False
		return result

	def filepn(self):
		filelist = os.listdir(self.filepath)
		for fl in filelist:
			fll = os.path.splitext(fl)
			if fll[1] == '.log':
				ff = os.path.join(self.filepath,fl)
				liff.append(ff)
		return liff


if __name__ == '__main__':
	if len(sys.argv) == 3:
		p = Judge(sys.argv[1])
		if p.dpath():
			if p.fexist():
				fn = p.filepn()
				for i in fn:
					f = func(i)
					f.finds(sys.argv[2])
			else:	
				print "The dir is not file with '.log'"
	else:
		print "please input argv after script(filepath key)"
