#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: test0727.py
@time: 2016/7/27 14:03
"""

import urllib2
import re
import sys
from bs4 import BeautifulSoup


def get_bs0bj(url):
    send_headers = {
     'Host':'http://www.kuaidaili.com',
     'User-Agent':'Mozilla/4.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Connection':'keep-alive'
     }
    print "okokok"

    req = urllib2.Request(url)
    print "okokok"
    req.add_header("User-Agent",send_headers)
    html = urllib2.urlopen(req)
    soup = BeautifulSoup(html)
    print soup
    return soup


if __name__ == '__main__':
    url = "http://www.kuaidaili.com"
    get_bs0bj(url)