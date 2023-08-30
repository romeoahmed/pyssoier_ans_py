"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
l1, l2, l3, l4, l5 = map(float, input().split())

p1 = (l1 + l2 + l5) / 2
p2 = (l3 + l4 + l5) / 2
s = sqrt(p1*(p1-l1)*(p1-l2)*(p1-l5)) + sqrt(p2*(p2-l3)*(p2-l4)*(p2-l5))

print(f"{s:.2f}")
