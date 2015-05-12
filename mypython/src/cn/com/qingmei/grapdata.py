#-*- coding: UTF-8 -*-

'''
Created on 2015年5月12日

@author: wulg
'''

from BeautifulSoup import BeautifulSoup
import os
import re
import sys
import urllib2
reload(sys)
total=0
urls=[]
def getHtml(url):
    page=urllib2.urlopen(url, "", 3000)
    html=page.read()
    return html
def getProductUrl(html):
    if os.path.exists("d://product/oulaiya")==False:
        os.makedirs("d://product/oulaiya")
    str=''
    reg = r"href=(.+\?from=sr_.+) target=\"_blank\""
    list = re.findall(reg,html)
    for u in list:
        str+=u.strip()
        urls.append(u)
    f = open("d://product/oulaiya/url.txt", "w")
    f.write(str)
    f.close()
    return urls
def getData():
    for u in urls:
        productHtml=getHtml(u)
        soup=BeautifulSoup(productHtml)
def parseHtml(productHtml):
        print 11
    
html = getHtml("http://search.jumei.com/?filter=0-11-3&search=%E6%AC%A7%E8%8E%B1%E9%9B%85&bid=4");

print getProductUrl(html) 
getData()
