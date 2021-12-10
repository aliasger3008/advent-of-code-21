#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:37:05 2021

@author: aliasger
"""

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")

check = {"{":"}","[":"]","<":">","(":")"}

incomp = {")":1,"]":2,"}":3,">":4}

scores = []

for line in content_lines:
    
    exp = []
    score = 0
    flag = 0
    
    for i in line:
        
        if i in check.keys():
            exp.append(i)
        
        if i in check.values():
            if check[exp[-1]] == i:
                exp.pop(-1)
            else:
                flag = 1
                break
    if flag == 1:
        continue 
    
    close = [check[j] for j in exp]
    close = list(reversed(close))
    
    for k in close:
        score *= 5
        score += incomp[k]
        
    scores.append(score)
        
scores = sorted(scores) 
    
mid = int(len(scores)/2)

print(scores[int(len(scores)/2)])
            