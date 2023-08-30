"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

max_score = 9.6 * 6 - 9.4 * 5
min_score = 9.6 * 6 - 9.8 * 5
mean_score = (9.6 * 6 - max_score - min_score) / (6 - 2)
print(f"{mean_score:5.2f}")
