"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def getGCD(m, n):
    return m if n == 0 else getGCD(n, m % n)

def getLCM(m, n):
    return m * n / getGCD(m, n)

m, n = map(int, input().split())
result = getLCM(m, n)

print(result)
