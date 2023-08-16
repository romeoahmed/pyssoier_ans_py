#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1079.py
@Time    :   2023/08/16 13:23:22
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

def fact(n, a = 1):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return fact(n - 1, n * a)

result = fact(int(input()))
print(result)
