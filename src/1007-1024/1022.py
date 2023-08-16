"""
Copyright 2023 Romeo Ahmed <ahmedorqwn@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1022.py
@Time    :   2023/08/16 12:03:41
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

from math import floor

# Suppose a cow eats x grass every day, and the pasture grows y grass every day.
# 20y-(15*20)x = 10y-(20*10)x => y/x = (15*20-20*10)/(20-10)
day = (15 * 20 - 20 * 10) / (20 - 10)
print(floor(day))
