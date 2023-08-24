"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

unitDigit = 1
tenDigit = 0
for i in range(n):
    carry = 0
    tmp = unitDigit * 1992
    unitDigit = tmp % 10
    carry = tmp // 10
    tmp = tenDigit * 1992 + carry
    tenDigit = tmp % 10

print(tenDigit, unitDigit, sep="")
