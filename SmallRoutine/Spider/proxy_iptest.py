#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: proxy_iptest.py
@time: 2016/7/27 13:12
"""

#encoding:UTF-8
import codecs
import urllib2
import datetime
import time
import threading
from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf_8_sig')

#获取更多标签的links
def get_links(url):
    links ={}
    bsObj = get_bsObj(url)
    for a in bsObj.find('ul',id='nav').findAll('a')[1:4]:
        if u"代理" in a.get_text():
            links.update({a.get_text():url+a['href']})
    return links

#获取table头
def get_TableHeard(url):
    bsObj = get_bsObj(url)
    th = bsObj.findAll('th')
    csvHeader = []
    for a in th:
        csvHeader.append(a.get_text())
    return csvHeader

 #获取总页面数
def get_allpage_links(url):
    bsObj = get_bsObj(url)
    allPageNum = bsObj.find('div',class_='listnav').findAll('a')[-2].string
    pageLinks = []
    for num in range(202,301):
        pageLinks.append(url+'/'+str(num))
    return pageLinks

#获取BeautifulSoup对象
def get_bsObj(url):
    send_headers = {
     'Host':'http://www.kuaidaili.com',
     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Connection':'keep-alive'
     }
    req = urllib2.Request(url,headers=send_headers)
#    try:
#        html = urllib2.urlopen(req)
#    except urllib2.HTTPError, e:
#        print e.code
#        print e.reason
    html = urllib2.urlopen(req)
    bsObj = BeautifulSoup(html,'lxml')
    return bsObj

#获取代理ip信息存入csv
def get_proxyInfo(urls,csvWriter):
    for url in urls:
        time.sleep(3)
        bsObj = get_bsObj(url)
        trs = bsObj.findAll('tr')
        trs.pop(0)
        for tr in trs:
            row = []
            for con in tr:
                if con != '\n' and con !='':
                    row.append(con.get_text().strip())
            div = tr.findAll('div')
            row.append(div[0]['title'])
            row.append(div[2]['title'])
            writer.writerow(row)
        print url+"爬取结束！"

if __name__ == '__main__':
    threadList = []
    rootUrl = "http://www.kuaidaili.com"
    links = get_links(rootUrl)
    for link in links:
        #try:
        dt = datetime.datetime.now()
        csvFile = open('IP_'+link +dt.strftime('%Y%m%d_%H%M')+'.csv','wb+')
        writer = csv.writer(csvFile)
        #writer.writerow(get_TableHeard(links[link]))
        for i in range(20):
            allUrls = get_allpage_links(links[link])
            urls = allUrls[((len(allUrls)+19)/20*i):((len(allUrls)+19)/20*(i+1))]
            t = get_proxyInfo(urls,writer)
            threadList.append(t)
        for i in range(20):
            threadList[i].start()
        for i in range(20):
            threadList[i].join()
        #except Exception,e:
            #print e
        #finally:
                #csvFile.close()