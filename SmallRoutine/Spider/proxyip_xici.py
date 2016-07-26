#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: proxyip_xici.py.py
@time: 2016/7/26 16:11
"""


import urllib2
from BeautifulSoup import BeautifulSoup

# get the proxy
of = open('proxy.txt', 'w')
for page in range(1,50):
    url = 'http://www.xicidaili.com/nn/%s' %page
    user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    request = urllib2.Request(url)
    request.add_header("User-Agent", user_agent)
    content = urllib2.urlopen(request)
    soup = BeautifulSoup(content)
    trs = soup.find('table', {"id":"ip_list"}).findAll('tr')
    for tr in trs[1:]:
        tds = tr.findAll('td')
        ip = tds[2].text.strip()
        port = tds[3].text.strip()
        protocol = tds[6].text.strip()
        if protocol == 'HTTP' or protocol == 'HTTPS':
            of.write('%s=%s:%s\n' % (protocol, ip, port))
            print '%s://%s:%s' % (protocol, ip, port)



import urllib2
import threading

inFile = open('proxy.txt', 'r')
outFile = open('available.txt', 'w')
url = 'http://www.lindenpat.com/search/detail/index?d=CN03819011@CN1675532A@20050928'
lock = threading.Lock()


def test():
    lock.acquire()
    line = inFile.readline().strip()
    lock.release()
    # if len(line) == 0: break
    protocol, proxy = line.split('=')
    cookie = "PHPSESSID=5f7mbqghvk1kt5n9illa0nr175; kmsign=56023b6880039; KMUID=ezsEg1YCOzxg97EwAwUXAg=="
    try:
        proxy_support = urllib2.ProxyHandler({protocol.lower():'://'.join(line.split('='))})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        request = urllib2.Request(url)
        request.add_header("cookie",cookie)
        content = urllib2.urlopen(request,timeout=4).read()
        if len(content) >= 1000:
            lock.acquire()
            print 'add proxy', proxy
            outFile.write('\"%s\",\n' %proxy)
            lock.release()
        else:
            print '出现验证码或IP被封杀'
    except Exception, error:
        print error
all_thread = []
for i in range(500):
    t = threading.Thread(target=test)
    all_thread.append(t)
    t.start()

for t in all_thread:
    t.join()

inFile.close()
outFile.close()


import requests
import re

of = open('proxy.txt', 'w')
url = 'http://www.youdaili.net/Daili/guonei/3661'
for i in range(1,4):
    if i == 1:
        Url = url+'.html'
    else:
        Url = url+'_%s.html' %i
    html = requests.get(Url).text
    res = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', html)
    for pro in res:
        of.write('http=%s\n' %pro)
        print pro
of.closed


import requests
import re
import time
from BeautifulSoup import BeautifulSoup
of = open('proxy.txt', 'w')
url = 'http://www.haodailiip.com/guonei/'
for i in range(1,20):
    Url = 'http://www.haodailiip.com/guonei/' + str(i)
    print "正在采集"+Url
    html = requests.get(Url).text
    bs = BeautifulSoup(html)
    table = bs.find('table',{"class":"proxy_table"})
    tr = table.findAll('tr')
    for i in range(1,31):
        td = tr[i].findAll('td')
        proxy_ip = td[0].text.strip()
        proxy_port = td[1].text.strip()
        of.write('http=%s:%s\n' %(proxy_ip,proxy_port))
        print 'http=%s:%s\n' %(proxy_ip,proxy_port)
    time.sleep(2)
of.closed