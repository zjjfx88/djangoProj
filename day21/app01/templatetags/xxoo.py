#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '创建自定义模板使用函数'
__author__ = 'zhangjingjun'
__mtime__ = '2018/3/23'
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

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def ooo():
    return "123"