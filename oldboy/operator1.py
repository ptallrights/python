#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: operator1.py
@time: 2016/7/28 11:57
"""

from __future__ import division

class Operator(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mult(self):
        return self.x*self.y
    def div(self):
        return self.x//self.y

if __name__ == "__main__":
    while True:
        x = int(raw_input("please input first number:"))
        o = raw_input("please input operator:")
        y = int(raw_input("please input second number:"))

        op = Operator(x,y)
        operator = {"+":op.add(),"-":op.sub(),"*":op.mult(),"/":op.div()}
        r = operator.get(o)
        print "The calulate result is: \033[34m%d %s %s = %d\033[0m" % (x,o,y,r)

        s = str(raw_input("please input 'c'to continue or 'q' to quit:"))
        if s == 'c':
            continue
        elif s == 'q':
            print "\033[31mWelcome to continue to use the next time\033[0m"
            break