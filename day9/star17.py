#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:28:11 2021

@author: aliasger
"""

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")

heightmap = []

for line in content_lines:
    heightmap.append(list(map(int, line)))

risk = 0

def checkhor(i,j):
    
    hor = []
    
    if j == 0:
        right = heightmap[i][1]
        hor.append(right)
           
    elif j == len(heightmap[0])-1:
        left = heightmap[i][-2]
        hor.append(left)
        
    else:
        left = heightmap[i][j-1]
        right = heightmap[i][j+1]
        hor.append(left)
        hor.append(right)
    
    return hor

def checkver(i,j):
    
    ver = []
    
    if i == 0:
        bottom = heightmap[1][j]
        ver.append(bottom)
        
    elif i == len(heightmap)-1:
        top = heightmap[-2][j]
        ver.append(top)
        
    else:
        top = heightmap[i+1][j]
        bottom = heightmap[i-1][j]
        ver.append(top)
        ver.append(bottom)
    
    return ver

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        check = []
        el = heightmap[i][j]
        
        hor = checkhor(i,j)
        ver = checkver(i,j)
        
        check = hor + ver
        
        if el not in check:
            check.append(el)
            if min(check) == el:
                risk += el+1

print(risk)