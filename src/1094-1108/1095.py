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

sentence = input()
eng = space = num = others = 0
for c in sentence:
    if "a" <= c <= "z" or "A" <= c <= "Z":
        eng += 1
    elif c == " ":
        space += 1
    elif "0" <= c <= "9":
        num += 1
    else:
        others += 1

print(eng, "\n", space, "\n", num, "\n", others, sep="")
