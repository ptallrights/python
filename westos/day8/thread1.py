#!/usr/bin/env python

import threading
import time
import logging

def worker(c):
	c.inc()

class Counter(object):

	def __init__(self,start=0):
		self.value = start
		#self.lock = threading.Lock()

	def inc(self):
		self.value += 1

if __name__ == "__main__":

	c  = Counter()

	for i in range(100):
		t = threading.Thread(target=worker)
		t.start()
		#worker(i)

	
