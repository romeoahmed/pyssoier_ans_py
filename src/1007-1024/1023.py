#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1023.py
@Time    :   2023/08/16 13:36:33
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

l = list(map(int, input().split()))
for i in range(len(l)):
    if i == 0:
        l[i] //= 3
        l[-1] += l[i]
        l[i+1] += l[i]
    elif i == len(l) - 1:
        l[i] //= 3
        l[0] += l[i]
        l[i-1] += l[i]
    else:
        l[i] //= 3
        l[i+1] += l[i]
        l[i-1] += l[i]

for j in l:
    print("%5d" % j, end='')
