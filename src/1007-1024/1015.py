#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1015.py
@Time    :   2023/08/16 11:55:36
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

num = int(input())
a = num // 100
b = num // 10 - a * 10
c = num - (num // 10) * 10
new = c * 100 + b * 10 + a
print(new)
