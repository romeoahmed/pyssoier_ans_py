"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x, y = map(int, input().split())
score = (x * 87 + y * 85) / (x + y)
print(f"{score:.4f}")
