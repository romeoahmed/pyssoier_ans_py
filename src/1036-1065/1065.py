"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

m = n = int(input())
facts = []
i = 2
while i <= n:
    if n % i == 0:
        facts.append(i)
        n /= i
    else:
        i += 1
facts.sort()

print(m, "=", "*".join(map(str, facts)), sep="")
