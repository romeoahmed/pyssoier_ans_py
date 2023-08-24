"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t = int(input())
v = (25000 / t) * 3.6

if v > 100:
    print("超速")
else:
    print("正常")
