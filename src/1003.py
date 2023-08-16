#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1003.py
@Time    :   2023/08/16 11:27:51
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

f = float(input())
if f >= -459.67:
    c = 5 * (f - 32) / 9
    print("%.2f" % c)
