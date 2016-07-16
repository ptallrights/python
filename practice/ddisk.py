#!/bin/env python 
# -*- coding: utf-8 -*- 
########################################################## 
# @This script is used to check disk free space for zabbix 
# @Contact:      wangwei03@jb51.net 
# @Name:         disk.py 
# @Function:     check disk free space for zabbix 
# @Author:       wangwei 
########################################################## 

import platform 
import commands 
import wmi 
from win32com.client import GetObject, Dispatch

def w_disk():
	c = wmi.WMI()
	i = 0
	for disk in c.Win64_LogicalDisk (DriveType=3):
		a = int(disk.FreeSpace) / (1024*1024*1024)
		b = int(100.0 * long (disk.FreeSpace) / long (disk.Size)) 
		if disk.Caption == "C:":
			if (a < 2) or (b < 10):
				i += 1
			else: 
				i += 0
		else: 
			if (a < 10) or (b < 10): 
				i += 1
			else:
				i += 0
	print i
def L_disk(): 
	free = commands.getstatusoutput('df -h|grep dev|egrep -v "tmp|var|shm"') 
	list = free[1].split('\n') 
	i = 0
	for disk in range(len(list)): 
		vd = list[disk][6:8] 
		a = list[disk].split()[3] 
		if a[-1] == 'T': 
			a = int(float(a[:-1]))*1024
		else: 
			a = int(float(a[:-1])) 
		b = 100 - int(list[disk].split()[4][:-1]) 
		if vd == "da": 
			if (a < 2) or (b < 10):
				i += 1
			else:
				i += 0
		else: 
			if (a < 10) or (b < 10): 
				i += 1
			else: 
				i += 0
	print i 


if __name__ == "__main__": 

	os = platform.system() 
	if os == "Windows": 
		w_disk() 
	elif os == "Linux": 
		L_disk() 

