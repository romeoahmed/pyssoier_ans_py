#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1022.py
@Time    :   2023/08/16 12:03:41
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

from math import floor

# Suppose a cow eats x grass every day, and the pasture grows y grass every day.
# 20y-(15*20)x = 10y-(20*10)x => y/x = (15*20-20*10)/(20-10)
day = (15 * 20 - 20 * 10) / (20 - 10)
print(floor(day))
