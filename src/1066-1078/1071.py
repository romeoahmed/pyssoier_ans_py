"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

matches = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
for i in range(112):
    if i < 10 and matches[i] == 6:
        print(i)
    elif 10 <= i < 100 and matches[i // 10] + matches[i % 10] == 6:
        print(i)
    elif i >= 100 and matches[i // 100] + matches[(i // 10) % 10] + matches[i % 10] == 6:
        print(i)
