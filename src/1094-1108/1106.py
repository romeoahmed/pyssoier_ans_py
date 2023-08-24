"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str_raw = input()
str_encrypted = ""

for i in str_raw:
    if "A" <= i < "Z" or "a" <= i < "z":
        str_encrypted = str_encrypted + chr(ord(i) + 1)
    elif i == "Z" or i == "z":
        str_encrypted = str_encrypted + chr(ord(i) - 25)
    else:
        str_encrypted = str_encrypted + i

print(str_encrypted)
