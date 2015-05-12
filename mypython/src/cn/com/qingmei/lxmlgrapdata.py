#-*- coding: UTF-8 -*-
'''
Created on 2015年5月14日

@author: wulg
'''

from lxml.etree import HTML
import lxml
import urllib2
def getHtml(url):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    html=opener.open(url).read()
    return html
html=getHtml("http://cosme.pclady.com.cn/product/99004.html")

#h2=html.decode('gbk').encode('utf8')
#print h2
#print html.decode('gbk').encode('gb2312')
h = HTML(html.decode('gbk'))
#print h
#x=h.xpath('//h3')
#p=h.xpath('//p[@class="pCpgg"]')
#print p
#print list(p[0].itertext())[1]
#print x
#print x[0].text
#h2=h.xpath('//div[@class="troCon"]')
#print list(h2[0].itertext())[1]
#h3=h.xpath('//p[@class="speP"]/a')
#print h3[0].text
h4=h.xpath('//div[@class="Awrap"]/ul/li/a')
print h4[0].find("img").attrib.get("src")
#h5=h.xpath('//div[@class="dTxt"]/p/a')
#print h5[3].text
#print h5[2].text 
#print h5[1].text
#list =h.xpath('//span[@class="productImg"]')
#print list
#for i in list:
#    print i
#    h2 = HTML(getHtml(i))
#    data=h2.xpath('//div[@class="dTxt"]/h3')
#    print h2
#    print data
#h=getHtml("http://cosme.pclady.com.cn/product/99004.html")
#print h
#h3 = HTML(getHtml("http://cosme.pclady.com.cn/product/99004.html"))  
#data=h3.xpath('//div[@class="screen"]')
#print data
#    url=i.get('href').replace("//","")
#    url='http://'+url
#    print url
#    u=getHtml(url)
#    p=HTML(u)
#    params=p.xpath('//ul[@id="J_AttrUL"]/li')
#    print params
#    for p in params:
#        print p.text
#    urls.append(params)
#    time.sleep(1)
#print h.xpath('//div[@class="deal_con_content"]')
#print h.xpath('//table/*')
#list= h.xpath('//table/tr/td/span')
#for i in list:
#    print i.text