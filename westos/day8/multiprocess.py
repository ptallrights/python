#!/usr/bin/env python

import multiprocessing
import time
import urllib2
web_sites = [
	'http://www.baidu.com',
	'http://www.163.com',
	'http://www.taobao.com',
	'http://www.jingdong.com',
]

def worker(url):
	req = urllib2.urlopen(url)
	time.sleep(1)
	print 'hello'

if __name__ == '__main__':

	for i in web_sites:
		p = multiprocessing.Process(target=worker,args=(i,))
		#p.daemon  = True
		p.start()
	print 'main_process'
