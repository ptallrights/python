#!/usr/bin/env python

import threading
import time
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] %(threadName)s %(message)s'
)

def wait_e(e):
	logging.debug('wait for e.....')
	#e.wait()
	time.sleep(10)
	e.set()
	logging.debug('event set... %s' % e.is_set())
	logging.debug('end.....')

def wait_e_t(e,t):
	while not e.is_set():
		logging.debug('wait for e time...')
		e.wait(t)
		logging.debug('event %s' % e.is_set())
		if e.is_set():
			logging.debug('do something')
		else:
			logging.debug('timeout...')

	logging.debug('endtwo...')

#def worker():
#	while True:
#		logging.debug('asasasasas')
#		time.sleep(1)

if __name__ == '__main__':
	e = threading.Event()

	t1 = threading.Thread(target=wait_e,args=(e,))

	t2 = threading.Thread(target=wait_e_t,args=(e,5))

#	t3 = threading.Thread(target=worker)

	t1.start()
	t2.start()
#	e.set()
#	t3.start()
