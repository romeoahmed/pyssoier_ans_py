"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

pi = 1
for i in range(1,20001):
    if i % 2 != 0:
        pi *= (i + 1) / i
    else:
        pi *= i / (i + 1)
pi *= 2

print("%.4f" % pi)
