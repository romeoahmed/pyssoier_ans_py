"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
if n <= 5:
    money = 2
elif 5 < n <= 10:
    money = 3
elif 10 < n <= 16:
    money = 4
elif n > 16:
    money = 5

print("票价{}元".format(money))
