#!/usr/bin/env python

#/proc/meminfo

def mem_info():
	with open('/proc/meminfo') as f:
		m = f.read().split('\n')
		m1 = m[0].split(':')
		m2 = m[1].split(':')	
		ml = []
		ml.append(m1[1].strip())
		ml.append(m2[1].strip())
	return ml

if __name__ == '__main__':
	print mem_info()
