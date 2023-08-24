"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentence = input()
eng = space = num = others = 0
for c in sentence:
    if "a" <= c <= "z" or "A" <= c <= "Z":
        eng += 1
    elif c == " ":
        space += 1
    elif "0" <= c <= "9":
        num += 1
    else:
        others += 1

print(eng, "\n", space, "\n", num, "\n", others, sep="")
