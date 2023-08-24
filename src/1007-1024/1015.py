"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = int(input())

a = num // 100
b = num // 10 - a * 10
c = num - (num // 10) * 10
new = c * 100 + b * 10 + a

print(new)
