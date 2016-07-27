#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: a_retest.py
@time: 2016/7/27 9:00
"""

import re
s1 = "adkkdk"
s2 = "abc123def"

an = re.search('^[a-z]+$',s1)
print an
if an:
    print 's1:',an.group(),'全为小写'
else:
    print s1,'不全是小写'

an = re.match('[a-z]+$',s2)
if an:
    print 's2:',an.group(),'全为小写'
else:
    print s2,'不全是小写'

a = '123abc456'
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)

def expend_abbr(sen,abbr):
    lenabbr = len(abbr)
    ma = ''
    for i in range(0,lenabbr):
        ma += abbr[i] + "[a-z]+" + ' '
    print "ma:",ma
    ma = ma.strip(' ')
    print ma
    p = re.search(ma,sen)
    if p:
        return p.group()
    else:
        return ''

print expend_abbr("Welcome to Algriculture Bank China","ABC")