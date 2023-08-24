"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str1 = input()
str2 = input()

if str1 in str2:
    print("{0} is substring of {1}".format(str1, str2))
elif str2 in str1:
    print("{0} is substring of {1}".format(str2, str1))
else:
    print("No substring")
