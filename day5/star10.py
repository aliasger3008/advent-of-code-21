#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:13:27 2021

@author: aliasger
"""

import numpy as np

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")
if '' in content_lines:
    content_lines.remove('')

#print(content)

path = np.zeros(shape=(1000,1000))

for line in content_lines:
    points = line.split(" -> ")
    coords1 = list(map(int, points[0].split(",")))
    coords2 = list(map(int, points[1].split(",")))
    
    if coords1[0]>coords2[0] and coords1[1]>coords2[1]:
        for i,j in zip(range(coords1[1],coords2[1]-1,-1),range(coords1[0],coords2[0]-1,-1)):
            path[i,j] += 1
            
    elif coords1[0]>coords2[0]:
        if coords1[1] == coords2[1]:
            for i in range(coords2[0], coords1[0]+1):    
                path[coords1[1],i] += 1
        else:
            for i,j in zip(range(coords1[1],coords2[1]+1),range(coords1[0],coords2[0]-1,-1)):
                path[i,j] += 1
            
    elif coords1[1]>coords2[1]:
        if coords1[0] == coords2[0]:
            for i in range(coords2[1], coords1[1]+1):    
                path[i,coords1[0]] += 1
        else:
            for i,j in zip(range(coords1[1],coords2[1]-1,-1),range(coords1[0],coords2[0]+1)):
                path[i,j] += 1       
    else:
        if coords1[1] == coords2[1]:
            for i in range(coords1[0], coords2[0]+1):    
                path[coords1[1],i] += 1
                
        elif coords1[0] == coords2[0]:
            for i in range(coords1[1], coords2[1]+1):    
                path[i,coords1[0]] += 1
        
        else:
            for i,j in zip(range(coords1[1],coords2[1]+1),range(coords1[0],coords2[0]+1)):
                path[i,j] += 1
            
cnt = 0    
for i in range(1000):
    for j in range(1000):
        if path[i][j]>1:
            cnt += 1

print(cnt)