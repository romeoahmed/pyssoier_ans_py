#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   1019.py
@Time    :   2023/08/16 11:59:36
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
'''

max_score = 9.6 * 6 - 9.4 * 5
min_score = 9.6 * 6 - 9.8 * 5
mean_score = (9.6 * 6 - max_score - min_score) / (6 - 2)
print("%5.2f" % mean_score)
