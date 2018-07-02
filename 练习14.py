# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:10:48 2018
K12（小学到高中12年的简称）--
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
.....
西藏藏医学院：5
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
-2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定


@author: Administrator
"""
#1
f=open('./all_school.txt','r',encoding='utf-8')
ls=f.read()
import re
ls1=re.compile('jianjie-(.*?).html').findall(ls)
ls2=re.compile('(.*?)http://').findall(ls)
for i in range(0,2300):
    print('学校:{}编号:{}'.format(ls2[i],ls1[i]))
#2
import urllib.request as r
url='http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
import re
ls3=re.compile('<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">',re.S).findall(d)
ls4=re.compile('<span><a href="http://www.gaokaopai.com/daxue-..-0-0-0-0-0-0.html">(.*?)</a></span>',re.S).findall(d)
for i in range(len(ls4)):
    print(ls4[i],ls3[i])
#3
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
f=open('./all_school.txt','r',encoding='utf-8')
ls=f.read()
import re
ls1=re.compile('jianjie-(.*?).html').findall(ls)
f1=open('./b.txt','w',encoding='utf-8')
for i in ls1:
    try:
        hh='id={}&type=2&city=43&state=1'.format(i).encode()
        req=r.Request(url,data=hh,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        import json
        dd=json.loads(d)   
        for a in range(len(dd['data'])):
            a1=dd['data'][a]['city']
            a2=dd['data'][a]['school']
            a3=dd['data'][a]['profess']
            a4=dd['data'][a]['subject']
            a5=dd['data'][a]['plan']
            f1.write('城市:{},学校:{},专业:{},科内:{},人数:{}\n'.format(a1,a2,a3,a4,a5))
    except Exception as err:
        print('学校在湖南不招收理科生')
f1.close()

#3
import urllib.request as r
f=open('./all_school.txt','r',encoding='utf-8')
ls=f.read()
import re
ls1=re.compile('jianjie-(.*?).html').findall(ls)
f1=open('./e.txt','w',encoding='utf-8')
for i in ls1:
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    hh='id={}&type=1&city=42&state=1'.format(i).encode()
    req=r.Request(url,data=hh,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    if d[0]=='{':
        f1.write('{}\n'.format(d))
    else:
        while d[0]!='{':
             url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
             hh='id={}&type=1&city=42&state=1'.format(i).encode()
             req=r.Request(url,data=hh,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
             d=r.urlopen(req).read().decode('utf-8','ignore')
        f1.write('{}\n'.format(d))
f1.close()



















