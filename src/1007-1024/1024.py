"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x, a, y, b = map(int, input().split())
z = (b * y - a * x) / (b - a)
print("%.2f" % z)
