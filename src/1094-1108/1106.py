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

str_raw = input()
str_encrypted = ""

for i in str_raw:
    if "A" <= i < "Z" or "a" <= i < "z":
        str_encrypted = str_encrypted + chr(ord(i) + 1)
    elif i == "Z" or i == "z":
        str_encrypted = str_encrypted + chr(ord(i) - 25)
    else:
        str_encrypted = str_encrypted + i

print(str_encrypted)
