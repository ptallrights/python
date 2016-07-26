#!/usr/bin/env python
# encoding: utf-8
# __author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: a_test.py.py
@time: 2016/7/26 13:57
"""

import urllib

url = "http://www.baidu.com/"

#urlopen()
sock = urllib.urlopen(url)
htmlCode = sock.read()
sock.close
fp = open("e:/1.html","wb")
fp.write(htmlCode)
fp.close

#urlretrieve()
urllib.urlretrieve(url, 'e:/2.html')
