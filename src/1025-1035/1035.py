#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1035.py
@Time    :   2023/08/16 14:03:31
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

x = int(input())
k = x // 4
y = x % 4

if y == 0:
    m = n = 0
elif y == 1:
    m = 0
    n = 1
    k -= 1
elif y == 2:
    m = 1
    n = 0
    k -= 1
else:
    m = n = 1
    k -= 2

print(m, "\n", n, "\n", k, sep="")
