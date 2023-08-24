"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

money = 100000
year = 0
while money > 0:
    year += 1
    money *= 1.037
    money -= 20000

print(year)
