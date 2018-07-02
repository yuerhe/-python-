# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:37:56 2018

@author: Administrator
"""

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