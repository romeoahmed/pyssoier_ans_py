"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for f in range(100, 106):
    c = 5 * (f - 32) / 9
    print("%8d%10.2f" % (f, c))
