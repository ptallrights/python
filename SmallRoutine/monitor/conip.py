#!/usr/bin/env python
# encoding: utf-8
# __author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: conip.py.py
@time: 2016/7/26 14:48
"""

#!/usr/bin/env python
# -*- coding: gbk -*-
import socket,time
while 1:
  file_obj = open('ip.txt')
  for line in file_obj:
    try:
      sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      ip = line.split()[0]
      port = int(line.split()[1])
      print ip,port
      #设置超时时间（0.0）
      sc.settimeout(2)
      sc.connect((ip,port))
      timenow=time.localtime()
      datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
      logstr="%s:%s 连接成功->%s \n" %(ip,port,datenow)
      print logstr
      sc.close()
    except:
      file = open("log.txt", "a")
      timenow=time.localtime()
      datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
      logstr="%s:%s 连接失败->%s \n" %(ip,port,datenow)
      print logstr
      file.write(logstr)
      file.close()
  print "sleep 10....."
  time.sleep(10)