# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:38:06 2018

@author: Administrator
"""
第八题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格
import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E8%80%B3%E7%8E%AF&suggest=history_1&_input_charset=utf-8&wq=erhuan&suggest_query=erhuan&source=suggest&loc=%E6%B7%B1%E5%9C%B3&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
f=open('./z.csv','a')
for a in range(0,36):
    q=data['mods']['itemlist']['data']['auctions'][a]['raw_title']
    w=data['mods']['itemlist']['data']['auctions'][a]['view_price']
    e=data['mods']['itemlist']['data']['auctions'][a]['view_sales']
    r=data['mods']['itemlist']['data']['auctions'][a]['nick']
    t=data['mods']['itemlist']['data']['auctions'][a]['item_loc']

    f.write('商品名：{},价格：{},付款人数：{},店铺名：{},地址：{}\n'.format(q,w,e,r,t))
f.close()

f=open('./z.csv','a')
for i in range(1,100): 
    q=i*44
    import urllib.request as r
    url='https://s.taobao.com/search?q=%E8%80%B3%E7%8E%AF&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E6%B7%B1%E5%9C%B3&bcoffset=3&ntoffset=3&p4ppushleft=1,48&s={}&ajax=true'.format(q)
    print(url)
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    for a in range(0,44):
        q=data['mods']['itemlist']['data']['auctions'][a]['raw_title']
        w=data['mods']['itemlist']['data']['auctions'][a]['view_price']
        e=data['mods']['itemlist']['data']['auctions'][a]['view_sales']
        r=data['mods']['itemlist']['data']['auctions'][a]['nick']
        t=data['mods']['itemlist']['data']['auctions'][a]['item_loc']        
        f.write('商品名：{},价格：{},付款人数：{},店铺名：{},地址：{}\n'.format(q,w,e,r,t))
f.close()











    