#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1030.py
@Time    :   2023/08/16 13:56:36
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

n = int(input())

isLeapYear = lambda n: True if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0) else False
if isLeapYear(n):
    print("{}年是闰年".format(n))
else:
    print("{}年不是闰年".format(n))
