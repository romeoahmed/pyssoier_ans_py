"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input()
s_new = ""
for i in range(len(s) - 1):
    s_new += chr(ord(s[i]) + ord(s[i + 1]))
s_new += chr(ord(s[-1]) + ord(s[0]))
print(s_new)
