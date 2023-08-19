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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    :   1098.py
@Time    :   2023/08/16 20:47:05
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

str1 = input()
str2 = input()

if str1 in str2:
    print("{0} is substring of {1}".format(str1, str2))
elif str2 in str1:
    print("{0} is substring of {1}".format(str2, str1))
else:
    print("No substring")