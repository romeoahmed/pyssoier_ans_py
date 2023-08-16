#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1010.py
@Time    :   2023/08/16 11:45:04
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

age = int(input())
quiet = int(input())
recommand_min = (220 - age - quiet) * 0.6 + quiet
recommand_max = (220 - age - quiet) * 0.8 + quiet
print(recommand_min, "~", recommand_max, sep="")
