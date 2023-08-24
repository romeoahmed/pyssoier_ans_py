"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dna_rule = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

dna = input()
for i in dna:
    print(dna_rule[i], end="")
