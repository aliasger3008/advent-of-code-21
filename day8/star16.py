#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:23:16 2021

@author: aliasger
"""

from collections import Counter    

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")

total = 0

for line in content_lines:
    num = ""
    
    split = line.split(" | ")
    output = split[1]
    key = split[0]
    output_list = output.split()
    key_list = key.split()
    key_list = sorted(key_list, key=len)
    
    d = {}
    d[1] = "".join(sorted(key_list[0]))
    d[4] = "".join(sorted(key_list[2]))
    d[7] = "".join(sorted(key_list[1]))
    d[8] = "".join(sorted(key_list[-1]))
    
    for j in range(6,9):
        let = "".join(sorted(key_list[j]))
        if not Counter(d[4]) - Counter(let):
            d[9] = let
        elif not Counter(d[1]) - Counter(let):
            d[0] = let
        else:
            d[6] = let
    for k in range(3,6):
        let = "".join(sorted(key_list[k]))
        if not Counter(d[1]) - Counter(let):
            d[3] = let
        elif not Counter(let) - Counter(d[6]):
            d[5] = let
        else:
            d[2] = let
            
    for i in output_list:
        i = "". join(sorted(i))
        n = list(d.keys())[list(d.values()).index(i)]
        num += str(n)
        
    total += int(num)  

print(total)