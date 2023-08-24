"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a, b, c = map(float, input().split())

max = lambda a, b, c: (a if a > c else c) if a > b else (b if b > c else c)
m = max(a, b, c) / (max(a + b, b, c) * max(a, b, b + c))

print("%.3f" % m)
