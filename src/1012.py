#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1012.py
@Time    :   2023/08/16 11:47:19
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

n, m = map(int, input().split())
m *= 0.8
n -= m
print("%.2f" % n)
