#!/usr/bin/env  python
#list

import threading
import time
import logging
import random

logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] %(threadName)s %(message)s'
)

#p/c

def producer(li):
	for x in range(10):
		i = random.randint(0,100)
		logging.info('product %d' % i)
		li.append(i)
		time.sleep(i/100.0)


def consumer(li,lst):
	count = 0
	while count < 10:
		if li:
			count += 1
			i = li[0]
			li.remove(i)
			lst.append(count)
			logging.info('consume %d' % i)
			time.sleep(1)

def handler(lst):
	num = 0
	while num < 10:
		if lst:
			num += 1
			i = lst[0]
			lst.remove(i)
			logging.info('handler %d' % i)
			time.sleep(2)

if __name__ == '__main__':
	li = list()
	lst = list()
	p = threading.Thread(target=producer,args=(li,))

	c = threading.Thread(target=consumer,args=(li,lst))

	h = threading.Thread(target=handler,args=(lst,))

	p.start()
	c.start()
	h.start()
