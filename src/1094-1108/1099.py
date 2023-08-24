"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentence = input()

num = 0
for i in sentence:
    if "0" <= i <= "9":
        num += 1

print(num)
