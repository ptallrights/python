#!/usr/bin/env python

import time
import urllib2
import threading

web_site = [
	'http://www.baidu.com',
	'http://www.163.com',
	'http://www.lagou.com',
	'http://www.51cto.com',
	'http://www.taobao.com'
]

def worker(web):
	#try:
	#	req = urllib2.urlopen(web)
	#except Exception as e:
	#	print e
	#print 'ok'
	time.sleep(1)

#def co():
#	threads = []
#	for web in web_site:
#		t = threading.Thread(target=worker,args=(web,),name='test') #thread-0
#		threads.append(t)
#		t.start()

if __name__ == '__main__':
	for web in web_site:
		worker(web)
#	co()

