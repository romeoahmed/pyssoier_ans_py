#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1032.py
@Time    :   2023/08/16 14:01:05
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

n = int(input())
if n <= 5:
    money = 2
elif 5 < n <= 10:
    money = 3
elif 10 < n <= 16:
    money = 4
elif n > 16:
    money = 5

print("票价{}元".format(money))
