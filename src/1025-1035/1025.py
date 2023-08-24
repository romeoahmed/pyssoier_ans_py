"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = int(input())
p = float(input())

if 6 <= s <= 10:
    money = 0.9 * s * p
elif s >= 11:
    money = 0.8 * s * p
else:
    money = s * p

print("%.1f" % money)
