"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def rmFileInfo(path):
    with open(path, 'r', encoding="utf-8") as r:
        lines = r.readlines()
    with open (path, 'w', encoding="utf-8") as w:
        mark = False
        for i in range(0, len(lines)):
            if ("\"\"\"" in lines[i]) and ("@File" in lines[i + 1]):
                mark = True
                continue
            elif ("@Time" in lines[i]) or ("@Author" in lines[i]) or ("@Version" in lines[i]):
                continue
            elif ("@Desc" in lines[i]):
                mark = True
                continue
            elif mark:
                mark = False
                continue
            w.write(lines[i])

dir_list = os.listdir(".")
for dir in dir_list:
    if dir == "rmFileInfo.py":
        continue
    file_list = os.listdir(dir)
    for file in file_list:
        path = dir + "/" + file
        rmFileInfo(path)
        print(f"Removed file info from {path}")
