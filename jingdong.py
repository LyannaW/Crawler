# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:41:52 2020

@author: think
"""

#%%获取产品评论内容与数据
import requests
import json

header = {'Connection': 'close',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
for i in range(0, 150):
    url1 = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4403&productId=100010345582&score=3&sortType=5&page='
    url2 = str(i)
    uel3 = '&pageSize=10&isShadowSku=0&fold=1'
    finalurl = url1+url2+uel3
    xba = requests.get(finalurl,headers = header).text[26:-2]
    data=json.loads(xba)
    for i in data['comments']:
        content = i['content']
        print("评论内容".format(content))
        file=open(r"D:\大创\企业项目\爬虫\京东洗碗刷评论\18\jingdong.txt", 'a')
        file.writelines(format(content))
for i in data['productCommentSummary']:
    file=open(r"D:\大创\企业项目\爬虫\京东洗碗刷评论\18\summary.txt",'a')
    file.writelines(i)
    file.writelines('\t')
    file.writelines(data['productCommentSummary'][i])
    file.writelines('\n')
#fw = open(r"D:\大创\企业项目\爬虫\京东洗碗刷评论\18\summary.txt",'w+')
#fw.write(str(data['productCommentSummary'])) #把字典转化为str
#fw.close()
print("finished")
#%%京东评论与打分

import re
import requests
 
#if os.path.exists('comment.txt'):
#    os.remove('comment.txt')
#else:
#    f = open('comment.txt','a')
f=open(r"D:\大创\企业项目\爬虫\京东洗碗刷评论\评论与打分\comment.txt", 'a')

count = 0
url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetch\
        JSON_comment98&productId=100010345582&score=0&sortType=5&page='
url2 = '&pageSize=10&isShadowSku=0&rid=0&fold=1'
 
for i in range(0,150):#输入需要爬虫的页面数
    try:
        html = requests.get(url + str(i) + url2)
        html = html.text
        
        #使用正则提取评论信息
        content1 = re.findall(r'"guid".*?,"content":(.*?),',html)
        
        #对提取的评论信息进行去重
        content2=[]
        temp = ''
        for c in content1:
            if temp != c:
                content2.append(c)
            temp = c
 
        #使用正则提取score字段信息
        score = re.findall(r'"referenceImage".*?,"score":(.*?),',html)
        
        for s,c in zip(score,content2):
            count += 1
            c = c.replace('\\n','')
            f.write(str(count)+'\t' + str(s)+'\t' + c)
            f.write('\n')
        

    except:
        print('爬取第'+str(i)+'页出现问题')
#        continue
        break
f.close()