#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1033.py
@Time    :   2023/08/16 14:01:50
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

height = float(input())
weight = float(input())
bmi = weight / (height ** 2)

if bmi < 18.5:
    situation = "偏瘦"
elif 18.5 <= bmi < 25:
    situation = "正常"
elif 25 <= bmi < 30:
    situation = "偏胖"
elif 30 <= bmi < 35:
    situation = "肥胖"
elif 35 <= bmi < 40:
    situation = "重度肥胖"
else:
    situation = "极度肥胖"

print("%.1f" % bmi)
print(situation)
