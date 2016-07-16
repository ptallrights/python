#!/usr/bin/env python
#coding=utf-8
# name IsOpen.py
import os
import sys
import socket

def IsOpen(ip,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect((ip,int(port)))
		s.shutdown(2)
		print '%d is open' % port
		return True
	except:
		print '%d is down' % port
		return False

if __name__ == '__main__':
	IsOpen("192.168.1.3",3306)
