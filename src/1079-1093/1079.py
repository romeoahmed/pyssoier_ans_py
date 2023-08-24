"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n, a = 1):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return fact(n - 1, n * a)

result = fact(int(input()))
print(result)
