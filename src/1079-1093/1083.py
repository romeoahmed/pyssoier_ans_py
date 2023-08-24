"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

m, n = map(int, input().split())
facts_m = []
facts_n = []

for i in range(1, m + 1):
    if m % i == 0:
        facts_m.append(i)

for i in range(1, n + 1):
    if n % i == 0:
        facts_n.append(i)

num = 1
for i in facts_m:
    if i > num and i in facts_n:
        num = i

result = int(m * n / num)
print(result)
