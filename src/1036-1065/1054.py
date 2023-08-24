"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

m, n = map(int, input().split())
for i in range(min(m, n), 0, -1):
    if m % i == 0 and n % i == 0:
        print(i)
        break
