#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1031.py
@Time    :   2023/08/16 13:59:38
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

age = float(input())
quiet = float(input())
sex = input()

if sex == "male":
    recommand_min = (220 - age - quiet) * 0.6 + quiet
    recommand_max = (220 - age - quiet) * 0.8 + quiet
else:
    recommand_min = (210 - age - quiet) * 0.6 + quiet
    recommand_max = (210 - age - quiet) * 0.8 + quiet

print(recommand_min, "~", recommand_max, sep="")
