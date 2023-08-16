#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1021.py
@Time    :   2023/08/16 12:02:09
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

from math import floor

a, b, c = map(int, input().split())
score = a * 0.2 + b * 0.3 + c * 0.5
print(floor(score))
