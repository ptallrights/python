#!/usr/bin/env python

#print
#logging threadsafe

import threading
import time
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] %(threadName)s %(message)s'
)

#logging.handlerSocket

def worker():
	#print threading.currentThread().getName(),'start....'
	logging.info('start....')
	time.sleep(2)
	#print threading.currentThread().getName(),'done....'
	logging.info('done....')


if __name__ == '__main__':
	for i in range(10):
		t = threading.Thread(target=worker)
		t.start()


