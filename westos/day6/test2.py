#!/usr/bin/env python

import sys
from os import path
from collections import Counter
import re

def counter(file_path):
	data = False
	if path.isfile(file_path):
		with open(file_path) as f:
			words = re.findall(r'\w+',f.read().lower())
			c_result = Counter(words)
			data = c_result.most_common(10)
	return data

if __name__ == '__main__':
	try:
		file_path = sys.argv[1]
		C = counter(file_path)
		print C
	except Exception as e:
		print e
