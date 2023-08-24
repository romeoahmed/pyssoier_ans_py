"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = input()
num_new = ""

for i in range(len(num) - 1, -1, -1):
    num_new += num[i]

num_new = int(num_new)
print(num_new)
