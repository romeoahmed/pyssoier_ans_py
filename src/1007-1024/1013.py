"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor

x, y = map(int, input().split())
d = 4 - 2
d1 = x * 4 - y
d2 = y - x * 2
print(floor(d1 / d), floor(d2 / d))
