

#如果使用python2执行一下变量的定义，则会报错，说明python2无法对中文直接支持,默认使用的字符集是ascii
#所以需要进行声明# -*- coding:utf-8 -*-,python3里面直接支持utf8编码格式，所以无需声明

name = '你好，世界'
print(name)