#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1017.py
@Time    :   2023/08/16 11:58:04
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

pi = 3.14159
r = float(input())
if r > 0 and r <= 10000:
    d = 2 * r
    c = pi * d
    s = pi * (r ** 2)

    print("%.4f %.4f %.4f" % (d, c, s))
