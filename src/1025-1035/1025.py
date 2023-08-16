#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1025.py
@Time    :   2023/08/16 13:18:59
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

s = int(input())
p = float(input())

if 6 <= s <= 10:
    money = 0.9 * s * p
elif s >= 11:
    money = 0.8 * s * p
else:
    money = s * p

print("%.1f" % money)
