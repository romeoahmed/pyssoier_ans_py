"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

rates = (0.0325, 0.03, 0.03, 0.02, 0.0175)
money = int(input())
for i in rates:
    money += money * i
print("%.2f" % money)
