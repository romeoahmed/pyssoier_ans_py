#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1029.py
@Time    :   2023/08/16 13:52:06
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

x, y, z = map(float, input().split())
max = lambda x, y, z: (x if x > z else z) if x > y else (y if y > z else z)
print(max(x, y, z))
