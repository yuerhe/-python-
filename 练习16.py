
题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例
class People:
    def __init__(self,quanguo):
        self.quanguo=quanguo
    def msg(self):
        print('全国总人数是:{}'.format(self.quanguo))      
    def calc(self,x,y):
        print(x+y)
a.calc(1,1)

f=open('./全国招生计划表.txt','r',encoding='utf-8')
h=f.read()
z={}
import re
ls3=re.compile('"plan":"(.*?)",').findall(ls2)
a=0
ls=[]

for i in range(len(ls3)):
    a=a+int(ls3[i])
print('全国总人数:{}'.format(a))



f=open('./全国招生计划表.txt','r',encoding='utf-8')
h=f.readlines()
z={}
import re
e=0
ls=[]
import json
for i in range(142600):
    z[i]=json.loads(h[i])
for d in range(142600):
    if z[d]['status']==1:
        ls.append(z[d])
for a in range(len(ls)):
    for b in range(len(ls[a]['data'])):
        c=int(ls[a]['data'][b]['plan'])
        e=e+c
        print('全国总人数:{}'.format(e))



for i in range(len(q)):
    if q[i]['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])



#各地区招生人数总合
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北','上海':'华东','江苏':'华东','浙江':'华东','安徽':'华东','福建':'华东','江西':'华东','山东':'华东','北京':'华北','天津':'华北','山西':'华北','河北':'华北','内蒙古':'华北','河南':'华中','湖南':'华中','湖北':'华中','广东':'华南','广西':'华南','海南':'华南','西藏':'西南','四川':'西南','贵州':'西南','云南':'西南','重庆':'西南','陕西':'西北','甘肃':'西北','青海':'西北','新疆':'西北','宁夏':'西北'}
areaplan={'东北':0,'华东':0,'华北':0,'西北':0,'华中':0,'华南':0,'西南':0}
ls=[]
f=open('./全国招生计划表.txt','r',encoding='utf-8')
ls1=f.readlines()
import json
for i in range(len(ls1)):
    ls.append(json.loads(ls1[i]))
for j in range(len(ls)):
    if ls[j]['status']==0:
        continue
    ls1=ls[j]['data']
    for school in ls1:
        city=school['city']
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
a=areaplan['东北']+areaplan['华东']+areaplan['华北']+areaplan['华南']+areaplan['华中']+areaplan['西南']+areaplan['西北']
print('东北招生人数:{}\n华东招生人数:{}\n华北招生人数:{}\n华南招生人数:{}\n华中招生人数:{}\n西南招生人数:{}\n西北招生人数:{}\n全国招生总人数:{}'.format(areaplan['东北'],areaplan['华东'],areaplan['华北'],areaplan['华南'],areaplan['华中'],areaplan['西南'],areaplan['西北'],a))
    
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:29:57 2018

@author: Administrator
"""

