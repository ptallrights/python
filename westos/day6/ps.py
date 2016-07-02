#!/usr/bin/env python
#ps -C cmd |wc -l

import subprocess
import sys

def ps_find():
	class Find():
		def __init__(self,cmd):
			self.cmd = cmd
			p = subprocess.Popen("ps -C %s |wc -l" % self.cmd,stdout=subprocess.PIPE,shell=True)
			self.l = int(p.stdout.read())
		def okok(self):
			if self.l != 1:
				print 'exist'
			else:
				print 'not exist'
	return Find

if __name__ == '__main__':
	try:
		r = ps_find()
		p = r(sys.argv[1])
		p.okok()
	except Exception as e:
		print e
