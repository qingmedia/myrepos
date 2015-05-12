#-*- coding: UTF-8 -*-  
'''
Created on 2015年5月19日

@author: wulg
'''
 

from lxml.etree import HTML
import MySQLdb
import lxml
import sys
import os
import time
import urllib2
import uuid
reload(sys)
sys.setdefaultencoding('utf8')
if os.path.exists("d://product/cream")==False:
    os.makedirs("d://product/cream")
errorTxt=open("d://product/cream/error.txt" ,'a')
#读取html
def getHtml(url):
#    h=urllib2.urlopen(url, '', 3000).read()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    h=opener.open(url).read()
    return h
#解析xml 获取想要的数据
def parseData(urlList):
    urlW=open("d://product/cream/url.txt" ,'a')
    for u in urlList:
        url=u.get("href").strip()
        print url
        urlW.write(url)
        urlW.write("\n")
        h = HTML(getHtml(url).decode('gbk'))
        try:
            dTxt=h.xpath('//h3')
            name=dTxt[0].text.strip().split()[0]+" "+dTxt[0].text.strip().split()[1]#名字
            brand=dTxt[0].text.strip().split()[0]#品牌
        except Exception:
            errorTxt.write(url)
#        print brand
#        print name
        try:
            pCpgg=h.xpath('//p[@class="pCpgg"]')
            td=h.xpath('//td[@class="td2"]')  
        except Exception:
            errorTxt.write(url)
        try:
            if td:
                price=list(td[0].itertext())[1].strip()
            else :
                price=list(pCpgg[0].itertext())[1].strip()#价格
#    print price   
        except Exception:
            errorTxt.write(url)
        try:
            norms=list(pCpgg[-1].itertext())[1].strip()#规格
        #    print norms
        except Exception:
            errorTxt.write(url)
        try:
            spePs=h.xpath('//p[@class="speP"]/a')
            effect=''
            for speP in spePs:
                effect+=speP.text.strip()+" "#功效
        #    print effect
        except Exception:
            errorTxt.write(url)
        try:
            awrap=h.xpath('//div[@class="Awrap"]/ul/li/a')
            imgUrl=awrap[0].find("img").attrib.get("src")#图片链接地址
        #    print imgUrl
        except Exception:
            errorTxt.write(url)
        try:
            troCon=h.xpath('//div[@class="troCon"]')
            des=list(troCon[0].itertext())
            description=''
            for d in des:
                if len(d.strip())>20:
                    description+=d.strip()+""#产品描述
    #    print description
        except Exception:
            errorTxt.write(url)    
    
        
        try:
            dTxt=h.xpath('//div[@class="dTxt"]/p/a')
            series=dTxt[1].text.strip() #系列
        except Exception:
            errorTxt.write(url) 
        
#        print series
        insertData(name,brand,price,norms,effect,imgUrl,description,series)
#插入数据库       
def insertData(name,brand,price,norms,effect,imgUrl,description,series):
    db = MySQLdb.connect("121.40.236.42","root","123456","qingmei" )
    cursor = db.cursor()
    storagedate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    categoryId="402881AC4D411BBA014D411BBAF80004"
    uuidStr=str(uuid.uuid4())
    uid=''.join(uuidStr.split('-'))
    sql = 'insert into qm_product (id,category_id,brand,name,product_img_url,price,description,effect,weight,product_series,creation_time) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % \
    (uid,categoryId,brand.encode('utf-8'),name.encode('utf-8'),imgUrl.encode('utf-8'),price.encode('utf-8'),description.encode('utf-8'),effect.encode('utf-8'),norms.encode('utf-8'),series.encode('utf-8'),storagedate) 
#    (uid,categoryId,brand.decode('utf-8'),name.decode('utf-8'),imgUrl.decode('utf-8'),price.decode('utf-8'),description.decode('utf-8'),effect.decode('utf-8'),norms.decode('utf-8'),series.decode('utf-8'),storagedate) 
    sqlW=open("d://product/cream/sql.txt" ,'a')
    print sql
    sqlW.write(sql)
    sqlW.write("\n")
    try:
        db.set_character_set('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute(sql)
        db.commit()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    cursor.close()  
    db.close()    
#urlHtml=getHtml("http://cosme.pclady.com.cn/products_list/br0_bs0_bi1_sm179_ef0_pb0_pe0_or0.html")
for i in range(251 ,301):
    i=str(i)
    print i
    htmls="http://cosme.pclady.com.cn/products_list/br0_bs0_bi1_sm5_ef0_pb0_pe0_or0_p"+i+".html#productList"
    urlHtml=getHtml(htmls)
    html= HTML(urlHtml.decode('gbk'))
    urlList=html.xpath('//div[@class="dList"]/ul/li/i[@class="iPic"]/a')
    try:
        parseData(urlList) 
    except Exception as e:
        errorTxt.write("\n")
        errorTxt.write(i)
        continue
#html= HTML(urlHtml.decode('gbk'))
#urlList=html.xpath('//div[@class="dList"]/ul/li/i[@class="iPic"]/a')
#parseData(urlList)
