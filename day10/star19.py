#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:25:45 2021

@author: aliasger
"""

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")


check = {"{":"}","[":"]","<":">","(":")"}

err = {")":3,"]":57,"}":1197,">":25137}

score = 0


for line in content_lines:
    
    exp = []
    
    for i in line:
        
        if i in check.keys():
            exp.append(i)
        
        if i in check.values():
            if check[exp[-1]] == i:
                exp.pop(-1)
            else:
                score += err[i]
                break

print(score)
            
        