"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = int(input())
quiet = int(input())
recommand_min = (220 - age - quiet) * 0.6 + quiet
recommand_max = (220 - age - quiet) * 0.8 + quiet
print(recommand_min, "~", recommand_max, sep="")
