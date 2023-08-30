"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

isLeapYear = lambda n: True if n % 400 == 0 or (n % 100 != 0 and n % 4 == 0) else False
if isLeapYear(n):
    print(f"{n}年是闰年")
else:
    print(f"{n}年不是闰年")
