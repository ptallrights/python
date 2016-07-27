#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: c_retest.py
@time: 2016/7/27 10:03
"""

import re
numHash = {}
numHash['零'.decode('utf-8')] = '0'
numHash['一'.decode('utf-8')] = '1'
numHash['二'.decode('utf-8')] = '2'
numHash['三'.decode('utf-8')] = '3'
numHash['四'.decode('utf-8')] = '4'
numHash['五'.decode('utf-8')] = '5'
numHash['六'.decode('utf-8')] = '6'
numHash['七'.decode('utf-8')] = '7'
numHash['八'.decode('utf-8')] = '8'
numHash['九'.decode('utf-8')] = '9'

def change2num(words):
    print "words:",words
    newword = ''
    for key in words:
        print key
        if key in numHash:
            newword += numHash[key]
        else:
            newword += key
    return newword

def Chi2Num(line):
    a = re.findall(u"[\u96f6|\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d]+\u5e74", line)
    if a:
        print "------"
        print line
        for words in a:
            newwords = change2num(words)
            print words
            print newwords
            line = line.replace(words, newwords)
    return line

m0 =  "在一九四九年新中国成立"
m1 =  "比一九九零年低百分之五点二"
m2 = '人一九九六年击败俄军,取得实质独立'

if __name__ == "__main__":
    print Chi2Num(m0)