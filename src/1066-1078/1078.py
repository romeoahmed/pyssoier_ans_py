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

n, m = map(int, input().split())
persons = [str(i) for i in range(1, n + 1)]
out_persons = []
del_num = m - 1
for i in range(n):
    out_persons.append(persons[del_num])
    del persons[del_num]
    if len(persons) != 0:
        del_num = (del_num + m - 1) % len(persons)

print(*out_persons, sep=" ")
