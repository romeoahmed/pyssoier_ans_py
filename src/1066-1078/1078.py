"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
persons = [str(i) for i in range(1, n + 1)]
out_persons = []
del_num = m - 1
for i in range(n):
    out_persons.append(persons[del_num])
    del persons[del_num]
    if len(persons) != 0:
        del_num = (del_num + m - 1) % len(persons)

print(*out_persons, sep=" ")
