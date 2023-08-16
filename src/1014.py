#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1014.py
@Time    :   2023/08/16 11:53:17
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

x, y = map(int, input().split())
score = (x * 87 + y * 85) / (x + y)
print("%.4f" % score)
