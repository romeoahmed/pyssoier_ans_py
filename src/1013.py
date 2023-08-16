#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1013.py
@Time    :   2023/08/16 11:49:03
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

from math import floor

x, y = map(int, input().split())
d = 4 - 2
d1 = x * 4 - y
d2 = y - x * 2
print(floor(d1 / d), floor(d2 / d))
