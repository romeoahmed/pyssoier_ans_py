"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor

a, b, c = map(int, input().split())
score = a * 0.2 + b * 0.3 + c * 0.5
print(floor(score))
