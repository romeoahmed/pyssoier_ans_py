#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1024.py
@Time    :   2023/08/16 13:45:48
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

x, a, y, b = map(int, input().split())
z = (b * y - a * x) / (b - a)
print("%.2f" % z)
