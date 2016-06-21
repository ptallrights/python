#!/usr/bin/env python
#10! 1*2*3*..*10

def fact(n):
	if n<=1:
		return n
	else:
		return fact(n-1)*n

a = fact(10)
print a

def fact2(n):
	ret = 1
	for x in range(n,1,-1):
		ret = ret * x
	return ret

b = fact2(10)
print b
#1*2 = 2
# 2*3 = 6
#  6*4 = 24
#  ........
