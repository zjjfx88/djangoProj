#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2018/6/12'
# ----------Dragon be here!----------
              ┏━┓      ┏━┓
            ┏━┛ ┻━━━━━━┛ ┻━━┓
            ┃       ━       ┃
            ┃  ━┳━┛   ┗━┳━  ┃
            ┃       ┻       ┃
            ┗━━━┓      ┏━━━━┛
                ┃      ┃神兽保佑
                ┃      ┃永无BUG！
                ┃      ┗━━━━━━━━━┓
                ┃                ┣━┓
                ┃                ┏━┛
                ┗━━┓ ┓ ┏━━━┳━┓ ┏━┛
                   ┃ ┫ ┫   ┃ ┫ ┫
                   ┗━┻━┛   ┗━┻━┛
"""
import requests,urllib


inputHost = 'http://webqo01.web.djt.ted:8012/request'
data='parity=%65%00%39%00%37%00%37%00%34%00%36%00%35%00%64%00%2d%00%31%00%36%00%35%00%66%00%2d%00%34%00%35%00%31%00%31%00%2d%00%38%00%34%00%35%00%61%00%2d%00%30%00%31%00%62%00%38%00%35%00%33%00%62%00%66%00%32%00%66%00%66%00%65%00%5f%00%66%00%6f%00%72%00%77%00%65%00%62%00&userIP=%35%00%38%00%2e%00%32%00%34%00%38%00%2e%00%31%00%32%00%2e%00%32%00%35%00%34%00&queryString=%a2%7e%e7%70%21%9e&userArea=&queryType=%71%00%75%00%65%00%72%00%79%00'

headers ={"Content-type": "application/x-www-form-urlencoded;charset=UTF-16LE"}
resp = requests.post(inputHost, data=data,headers=headers)
#print(resp.text)
query = '%a2%7e%e7%70%21%9e'
#print(query.encode('utf-16LE'))
#print(urllib.parse.unquote(query))
query2='红烧鸡'
#unicode_query = query2.encode('utf-8')
# a= query2.encode('utf-16LE','ignore')
# print(a)
print(urllib.parse.urlencode(query2))
