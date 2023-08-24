"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = input()
s2 = input()

s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")
s1 = s1.lower()
s2 = s2.lower()

if s1 == s2:
    print("YES")
else:
    print("NO")
