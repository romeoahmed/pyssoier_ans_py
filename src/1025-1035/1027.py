#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1027.py
@Time    :   2023/08/16 13:50:00
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

t = int(input())
v = (25000 / t) * 3.6

if v > 100:
    print("超速")
else:
    print("正常")
