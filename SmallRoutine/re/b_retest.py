#!/usr/bin/env python
# -*- coding: cp936 -*-
#__author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: b_retest.py
@time: 2016/7/27 9:47
"""


import re
def expand_abbr(sen, abbr):
    lenabbr = len(abbr)
    ma = ''
    for i in range(0, lenabbr-1):
        ma += abbr[i] + "[a-z]+" + ' ' + '([a-z]+ )?'
    ma += abbr[lenabbr-1] + "[a-z]+"
    print 'ma:', ma
    ma = ma.strip(' ')
    p = re.search(ma, sen)
    if p:
        return p.group()
    else:
        return ''

print expand_abbr("Welcome to Algriculture dev Bank of China", 'ABC')

sen = "abc,123,456,789,mnp"
p = re.compile("\d+,\d+?")

for com in p.finditer(sen):
    mm = com.group()
    print "hi:", mm
    print "sen_before:", sen
    sen = sen.replace(mm, mm.replace(",", ""))
    print "sen_back:", sen, '\n'



m0 =  "在一九四九年新中国成立"
m1 =  "比一九九零年低百分之五点二"
m2 =  '人一九九六年击败俄军,取得实质独立'

def fuc(m):
    m = m.decode('cp936')
    a = re.findall(u"[\u96f6|\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d]+\u5e74", m)
    if a:
        for key in a:
            print key
    else:
        print "NULL"

fuc(m0)
fuc(m1)
fuc(m2)