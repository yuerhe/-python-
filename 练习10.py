# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:36:47 2018

@author: Administrator
"""


第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序
print('火车站三字码是：'+'BJX')
    ls=open('./火车站编码.csv','r').readlines()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xf8 in position 6572: illegal multibyte sequence
"""
#1
def hanzi_to_pin(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(date,from_station,to_station)
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
print(url)
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
#2
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-26&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
data=data['data']['result']
p='  ' 
t='日期{}车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
t=t.split(p)
for i in t:
    print(i.center(10),end='')
print()
for j in range(0,9):
    s=data[j]
    ls=s.split('|')
    ls=[ls[13],ls[3],[ls[4],ls[5]],[ls[8],ls[9]],ls[10],'--','--','--','--',ls[23],'--',ls[26],'--',ls[28],ls[29],'--',ls[1],'\n']
    for i in ls:
        print(str(i).center(13).replace('[','').replace(']','').replace('CXW','重庆西').replace('BXP','北京西')
    .replace('CUW','重庆北').replace('CQW','重庆').replace('GIW','贵阳').replace('CDW','成都'),end='')

#3
import urllib.request as r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-26&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
data=data['data']['result']
p='  '
s=data[8]
ls=s.split('|')
t='日期{}车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
t=t.split(p)
for i in t:
    print(i.center(10),end='')
print()
ls=[ls[13],ls[3],[ls[4],ls[5]],[ls[8],ls[9]],ls[10],'--','--','--','--',ls[23],'--',ls[26],'--',ls[28],ls[29],'--',ls[1]]
for i in ls:
    print(str(i).center(13).replace('[','').replace(']','').replace('CQW','重庆').replace('BXP','北京西'),end='')