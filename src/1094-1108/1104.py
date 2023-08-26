"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

c_reserved_words = (
    "auto", "break", "case", "char",
    "const", "continue", "default", "do",
    "double", "else", "enum", "extern",
    "float", "for", "goto", "if",
    "int", "long", "register", "return",
    "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
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
