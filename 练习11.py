# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?wd=%E7%9F%A5%E4%B9%8E&rsv_spt=1&rsv_iqid=0x9f7ecfa00005fa56&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=58025142_5_oem_dg&rsv_enter=1&rsv_sug3=12&rsv_sug1=11&rsv_sug7=100'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
for i in range(0,7):
    print('标题:{}'.format(ls[i]))
ls1=re.compile('class="c-abstract">(.*?)</div>').findall(data)
for j in range(len(ls1)):
    print('描述:{}'.format(ls1[j]))
ls2=re.compile('style="text-decoration:none;">(.*?)/&nbsp').findall(data)
for p in range(len(ls2)):
    print('网址:{}'.format(ls2[p]))

#题目十二：使用re爬取天气信息
#1.天气描述，天气温度，天气气压
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import re
ls3=re.compile('"description":"(.*?)",').findall(data)
ls4=re.compile('"temp":(.*?),').findall(data)
ls5=re.compile('"pressure":(.*?),').findall(data)
for i in range(0,36):
    print('天气描述:{},温度:{},气压:{}'.format(ls3[i],ls4[i],ls5[i]))

