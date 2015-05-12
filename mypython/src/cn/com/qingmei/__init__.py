#-*- coding: UTF-8 -*-   

from lxml.etree import HTML
import lxml
import urllib2
import uuid
def getHtml(url):
#    h=urllib2.urlopen(url, '', 3000).read()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    h=opener.open(url).read()
    return h
for i in range(2 ,50):
    if i<10:
        i="0"+str(i)
    else :
        i=str(i)
    print i
#html=getHtml("http://cosme.pclady.com.cn/product/80237.html").decode('gbk').encode('utf8')
#print html
#htmlStr = HTML(html) 
#for p in price:
#    print p.text
#html=getHtml("http://list.tmall.com/search_product.htm?spm=a221z.7076649.1000.7.rkibAz&cat=50026502&sort=s&acm=lb-tms-1044523-44534.1003.8.121344&style=g&q=%B1%A3%CA%AA&uuid=121344&from=sn_1_cat-qp&abtest=&scm=1003.8.lb-tms-1044523-44534.ITEM_1413427435975_121344&pos=1#J_crumbs")
#html2=HTML(html)
#urls =html2.xpath('//a[@class="productImg"]')
#for u in urls:
#    url=getHtml("http:"+u.get('href'))
#    urlData=HTML(url)
#    data=urlData.xpath('//ul[@id="J_AttrUL"]/li')
#    print data
#    for d in data:
#        print d.text
    
#url="http://detail.tmall.com/item.htm?id=38333829040&skuId=62603109023&areaId=330100&cat_id=50026502&rn=226b67d5dc0855ca30c8c9b19eaa9f4a&user_id=289209604&is_b=1"
#u=getHtml(url)
#p=HTML(u)
#print p
#params=p.xpath('//ul[@id="J_AttrUL"]')
#print params