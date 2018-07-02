# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:35:30 2018

@author: Administrator
"""

题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总
import urllib.request as r
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
for j in range(1,8,6):
    s=data[j]
    ls=s.split('|')
    ls=[ls[13],ls[3],[ls[4],ls[5]],[ls[8],ls[9]],ls[10],'--','--','--','--',ls[23],'--',ls[26],'--',ls[28],ls[29],'--',ls[1],'\n']
    for i in ls:
        print(str(i).center(13).replace('[','').replace(']',''),end='')

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
    print(str(i).center(13).replace('[','').replace(']',''),end='')