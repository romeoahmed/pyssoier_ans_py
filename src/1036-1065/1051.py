"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

true_num = int(input())
while (input_num := int(input())) != true_num:
    if input_num < true_num:
        print("偏小")
    else:
        print("偏大")
print("正确")
