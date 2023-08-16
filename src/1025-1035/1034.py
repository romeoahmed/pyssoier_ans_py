#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1034.py
@Time    :   2023/08/16 14:02:32
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

t = int(input())
v = (25000 / t) * 3.6

if 100 < v < 120:
    situation = "超过规定时速且不足20%"
elif 120 <= v < 150:
    situation = "超过规定时速20%以上且不足50%"
elif 150 <= v < 170:
    situation = "超过规定时速50%以上且不足70%"
elif v >= 170:
    situation = "超过规定时速70%以上"
else:
    situation = "正常"

print(round(v, 1))
print(situation)
