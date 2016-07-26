#!/usr/bin/env python
# coding:utf-8
# __author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: getjpg.py.py
@time: 2016/7/26 10:29
"""

import urllib2

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/p/2738151262")

print html