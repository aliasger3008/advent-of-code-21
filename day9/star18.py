#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:36:57 2021

@author: aliasger
"""

def findbasin(heightmap, i, j):
    if 0 <= i < len(heightmap) and 0 <= j < len(heightmap[i]) and heightmap[i][j] != 9:
        heightmap[i][j] = 9
        return (
            1
            + findbasin(heightmap, i - 1, j)
            + findbasin(heightmap, i + 1, j)
            + findbasin(heightmap, i, j - 1)
            + findbasin(heightmap, i, j + 1)
        )
    return 0

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")

heightmap = []

for line in content_lines:
    heightmap.append(list(map(int, line)))
    
basins = []

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        basins.append(findbasin(heightmap, i, j))
        
basins = sorted(basins, reverse=True)
print(basins[0] * basins[1] * basins[2])