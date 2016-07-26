#!/usr/bin/env python
# encoding: utf-8
# __author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: a_spider.py.py
@time: 2016/7/25 15:33
"""
import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
        reg = r'src="(.+?\.jpg)" pic_ext'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        x = 1
	for i in imglist:
                urllib.urlretrieve(i,'%s.jpg' % x)
                x+=1


html = getHtml("http://tieba.baidu.com/p/3879322563?fr=frs")
getImg(html)