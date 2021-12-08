#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:54:10 2021

@author: aliasger
"""

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")

cnt = 0

for line in content_lines:
    output = line.split(" | ")[1]
    output_list = output.split()
    for i in output_list:
        leng = len(i)
        if leng == 2 or leng == 3 or leng == 4 or leng == 7:
            cnt += 1

print(cnt)
            
    