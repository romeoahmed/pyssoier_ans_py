"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = 0
while True:
    n += 1
    if n % 2 == 1 and n % 3 == 1 and n % 4 == 1 and n % 5 == 1 and n % 6 == 1 and n % 7 == 0:
        break
print(n)
