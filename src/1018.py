#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1018.py
@Time    :   2023/08/16 11:59:03
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

from math import sqrt

a, b, c = map(float, input().split())
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("%.3f" % s)
