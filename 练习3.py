# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#3题
#1.通过复制联网代码获得天气(老家)字典数据
#2.打印温度temp,天气情况description,天气气压pre
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
print(data['main']['temp'])
print(data['weather'][0]['description'])
print(data['main']['pressure'])
