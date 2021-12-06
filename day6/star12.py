#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:38:27 2021

@author: aliasger
"""

from collections import Counter, defaultdict

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split(",")
state = list(map(int,content_lines))

n = 256 # No. of days

state = Counter(state)

for i in range(n):
    
    temp = defaultdict(int)
    
    for k, v in sorted(state.items()):
        if k == 0:
            temp[6] += v
            temp[8] = v
        else:
            temp[k-1] += v
    state = temp
    
print(sum(state.values()))