"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sentence_1 = input()
sentence_2 = input()

sentence_1 = sentence_1.replace(" ", "")
sentence_2 = sentence_2.replace(" ", "")
sentence_1 = sentence_1.lower()
sentence_2 = sentence_2.lower()

if sentence_1 == sentence_2:
    print("YES")
else:
    print("NO")
