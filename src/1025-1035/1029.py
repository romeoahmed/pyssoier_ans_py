"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x, y, z = map(float, input().split())
max = lambda x, y, z: (x if x > z else z) if x > y else (y if y > z else z)
print(max(x, y, z))
