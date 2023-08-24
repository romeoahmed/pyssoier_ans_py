"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

money = money_sum = 20
who = 1
while money_sum < 500:
    who += 1
    money += 5
    money_sum += money

print(who)
