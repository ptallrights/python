#!/usr/bin/env python

import threading
import time
import logging

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] %(threadName)s %(message)s'
)

#logging.handlerSocket

def daemon():
	logging.info('daemon start....')
	time.sleep(2)
	#raise IndexError('daemon.......')
	logging.info('daemon done....')

def non_daemon():
	logging.info('non-daemon start....')
	time.sleep(0.4)
	logging.info('non-daemon done....')


if __name__ == '__main__':
	d = threading.Thread(target=daemon,name='daemon')
	d.setDaemon(True)

	t = threading.Thread(target=non_daemon,name='non-daemon')
	t.setDaemon(True)
	d.start()
	t.start()
	logging.info('hello ......')
	d.join()
	logging.info('okokokokokok')
