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

c_reserved_words = (
    "auto", "break", "case", "char", "const",
    "continue", "default", "do", "double", "else", "enum", 
    "extern","float", "for", "goto", "if", "int", "long", "register", 
    "return","short", "signed", "sizeof", "static", "struct", 
    "switch", "typedef","union", "unsigned", "void", "volatile", "while"
)

def isLegitID(n):
    for word in c_reserved_words:
        if n == word:
            return False
    
    if "0" <= n[0] <= "9":
        return False
    
    for i in n:
        if i == "_" or "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9":
            continue
        return False
    return True

n = input()
if isLegitID(n):
    print("yes")
else:
    print("no")
