#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:49:55 2021

@author: aliasger
"""

# Opening and read input file given 
file = open('input','r')
content = file.read()

# Shift to a list
content_list = content. split("\n")

# Remove any blanks
if '' in content_list:
    content_list.remove('')
    
# Map to int to perform operation
content_list = list(map(int,content_list))

# Increase counter
cnt = 0

# Logic to check increase 
for i in range(len(content_list)-3):
    total_current = content_list[i] + content_list[i+1] + content_list[i+2]
    total_next = content_list[i+1] + content_list[i+2] + content_list[i+3]
    if total_current<total_next:
        cnt = cnt+1

print(cnt)