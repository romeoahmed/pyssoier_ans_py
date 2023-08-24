"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor

# Suppose a cow eats x grass every day, and the pasture grows y grass every day.
# 20y-(15*20)x = 10y-(20*10)x => y/x = (15*20-20*10)/(20-10)
day = (15 * 20 - 20 * 10) / (20 - 10)
print(floor(day))
