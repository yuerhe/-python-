# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:29:05 2018

@author: Administrator
"""
练习15
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)

class Weather:
    def __init__(self,temp,description,pressure):
        self.temp=temp
        self.description=description
        self.pressure=pressure
    def msg(self):
        print('温度是:{} 情况:{} 气压:{}'.format(self.temp,self.description,self.pressure))
ls=[3,11,19]
for i in ls:
    a=data['list'][i]['main']['temp']
    b=data['list'][i]['weather'][0]['description']
    c=data['list'][i]['main']['pressure']
    d=Weather(a,b,c)
    d.msg()
