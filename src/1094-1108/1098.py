"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str1 = input()
str2 = input()

if str1 in str2:
    print(f"{str1} is substring of {str2}")
elif str2 in str1:
    print(f"{str2} is substring of {str1}")
else:
    print("No substring")
