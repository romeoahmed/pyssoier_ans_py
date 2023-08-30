"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

pi = 3.14159
r = float(input())
if r > 0 and r <= 10000:
    d = 2 * r
    c = pi * d
    s = pi * (r ** 2)

    print(f"{d:.4f} {c:.4f} {s:.4f}")
