"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = list(map(int, input().split()))
for i in range(len(l)):
    if i == 0:
        l[i] //= 3
        l[-1] += l[i]
        l[i+1] += l[i]
    elif i == len(l) - 1:
        l[i] //= 3
        l[0] += l[i]
        l[i-1] += l[i]
    else:
        l[i] //= 3
        l[i+1] += l[i]
        l[i-1] += l[i]

for j in l:
    print("%5d" % j, end="")
