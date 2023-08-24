"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

threshold = float(input())
dna_1 = input()
dna_2 = input()

count = 0
for i, j in zip(dna_1, dna_2):
    if i == j:
        count += 1

correlation = count / len(dna_1)
if correlation >= threshold:
    print("yes")
else:
    print("no")
