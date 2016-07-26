#!/usr/bin/env python
# encoding: utf-8
# __author__ = 'ptallrights'

"""
@version: python 2.7.11
@author: ptallrights
@license: my Licence 
@software: PyCharm
@file: proxy_ip.py.py
@time: 2016/7/26 16:02
"""

'''
Created on 2013-8-13
通过python实现自动抓取网上的代理ip和端口

@author: ptallrights
'''

import urllib,time,re,logging


#URL = 'http://www.goodips.com/?ip=&port=&dengji=&adr=%E7%94%B5%E4%BF%A1&checktime=&sleep=1%E7%A7%92%E5%86%85&cunhuo=48%E5%B0%8F%E6%97%B6%E4%BB%A5%E4%B8%8A&px='
URL = 'http://www.xicidaili.com/'

class getProxyIP:
    def format_log(self):
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s  %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='proxy.log',
                filemode='w+')


        logging.info("ip:        " + "port")


#   从网页抓去代理 ip ，并整理格式
    def getProxyHtml(self):
#        抓去代理 ip页面的代码
        page = urllib.urlopen(URL)
        html = page.read()
        #print html
        return html

    def ipPortRe(self):
#       从页面代码中取出代理 ip和端口
        html = self.getProxyHtml()
        #ip_re = re.compile(r'(((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?))')
        ip_re = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+\n.+>(\d{1,5})<')
        ip_port = re.findall(ip_re,html)
        print ip_port
        return ip_port


    def proxyIP(self):
#       格式化输出代理 ip和端口
        ip_port = self.ipPortRe()
#       将代理 ip整理成['221.238.28.158:8081', '183.62.62.188:9999']格式
        proxyIP = []
        for i in range( 0,len(ip_port)):
            proxyIP.append( ':'.join(ip_port[i]))
            logging.info(proxyIP[i])
#       将代理 ip整理成[{'http': 'http://221.238.28.158:8081'}, {'http': 'http://183.62.62.188:9999'}]格式
        proxy_list = []
        for i in range( 0,len(proxyIP)):
            a0 = 'http://%s'%proxyIP[i]
            a1 = { 'http ':'%s'%a0}
            proxy_list.append(a1)
        print proxy_list
        return proxy_list


if __name__ == '__main__':
    time_start = time.time()
    t = getProxyIP()
    t.format_log()
    t.proxyIP()
    time_end = time.time()
    time = time_end - time_start
    print time