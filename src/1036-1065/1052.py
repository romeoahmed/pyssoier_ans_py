"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

pi = 0
for i in range(1, 10000):
    pi += 1 / (i ** 2)
pi = math.sqrt(6 * pi)

print("%.4f" % pi)
