#!/usr/bin/env python

import threading
import time
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] %(threadName)s %(message)s'
)

def domain():
	#print 'domain start...'
	logging.info('domain start...')
	time.sleep(2)
	#print 'domian stop...'
	logging.info('domain stop...')

def non_domain():
	#print 'non-domian start...'
	logging.info('non-domian start...')
	time.sleep(0.5)
	#print 'non-domian stop...'
	logging.info('non-domain stop...')


if __name__ == '__main__':

	d = threading.Thread(target=domain,name='domian')
	d.setDaemon(True)

	t = threading.Thread(target=non_domain,name='non-domain')
	d.start()
	t.start()
	
