#!/usr/bin/env python

#/proc/loadavg

def load_avg():
	load = {}
	with open('/proc/loadavg') as f:
		avg = f.read().split()
		load['avg_1'] = avg[0]
		load['avg_5'] = avg[1]
		load['avg_15'] = avg[2]

	return load

if __name__ == '__main__':
	print load_avg()
