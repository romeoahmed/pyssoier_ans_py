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
@File    :   1031.py
@Time    :   2023/08/16 13:59:38
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

age = float(input())
quiet = float(input())
sex = input()

if sex == "male":
    recommand_min = (220 - age - quiet) * 0.6 + quiet
    recommand_max = (220 - age - quiet) * 0.8 + quiet
else:
    recommand_min = (210 - age - quiet) * 0.6 + quiet
    recommand_max = (210 - age - quiet) * 0.8 + quiet

print(recommand_min, "~", recommand_max, sep="")
