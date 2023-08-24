"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
doors = [True for i in range(n)]

for i in range(2, n + 1):
    for j in range(n):
        if (j + 1) % i == 0:
            doors[j] = not doors[j]

opened_doors = []
for index, value in enumerate(doors):
    if value:
        opened_doors.append(str(index + 1))

print(*opened_doors, sep=" ")
