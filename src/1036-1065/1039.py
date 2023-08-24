"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = int(input())
h = int(input())

if l >= h:
    print("输入的下限应该小于上限")
else:
    for f in range(l, h):
        c = 5 * (f - 32) / 9
        print("%8d%10.2f" % (f, c))
