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
@File    :   1102.py
@Time    :   2023/08/16 21:14:06
@Author  :   romeoahmed 
@Version :   1.0
@Desc    :   None
"""

n = int(input())
win_combinations = (("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock"))
results = []

for i in range(n):
    a, b = input().split()

    if a == b:
        result = "Tie"
    elif (a, b) in win_combinations:
        result = "Player1"
    else:
        result = "Player2"
    results.append(result)

print(*results, sep="\n")
