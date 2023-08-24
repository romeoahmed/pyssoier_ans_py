"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

a, b, c = map(float, input().split())
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("%.3f" % s)
