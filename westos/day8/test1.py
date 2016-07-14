#!/usr/bin/env python

import time
import threading
import urllib2

web_sites = [
	'http://www.baidu.com',
	'http://www.163.com',
	'http://www.taobao.com',
	'http://www.cctv.com'
]

def worker(url):
	req = urllib2.urlopen(url)
	time.sleep(1)

if __name__ == '__main__':
	for i in web_sites:
		t = threading.Thread(target=worker,args=(1,))
		t.start()


