"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
persons = [i for i in range(1, n + 1)]
outPersons = []
delNum = m - 1
for i in range(n):
    outPersons.append(persons[delNum])
    del persons[delNum]
    if len(persons) != 0:
        delNum = (delNum + m - 1) % len(persons)

print(*outPersons, sep=" ")
