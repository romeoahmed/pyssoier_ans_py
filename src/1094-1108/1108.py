"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
medicines = []

for i in range(n):
    medicine = input()
    if "a" <= medicine[0] <= "z" or "A" <= medicine[0] <= "Z":
        medicine = medicine.capitalize()
    else:
        medicine = medicine.lower()
    
    medicines.append(medicine)

print(*medicines, sep="\n")
