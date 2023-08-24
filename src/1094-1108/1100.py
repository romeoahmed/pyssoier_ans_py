"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findFirstUnique(n):
    for i in n:
        if n.count(i) == 1:
            return i
    return "no"

str_raw = input()
print(findFirstUnique(str_raw))
