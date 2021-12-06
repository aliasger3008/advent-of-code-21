#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:08:24 2021

@author: aliasger
"""

import numpy as np

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split(",")
state = list(map(int,content_lines))

state = np.array(state)

n = 80 # No. of days

for i in range(n):
    cnt = np.count_nonzero(state == 0)
    
    state = state - 1
    state[state == -1] = 6
    
    l = np.empty(cnt)
    l.fill(8)
    state = np.concatenate((state,l))

print(len(state))
        
            
