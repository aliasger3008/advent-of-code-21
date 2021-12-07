#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:57:14 2021

@author: aliasger
"""

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split(",")
positions = list(map(int,content_lines))

# Start and end for positions
start = min(positions)
end = max(positions)

fuel_list = []

# Checking positions for fuel used
for i in range(start, end+1):
    fuel = 0
    for pos in positions:
        charge = abs(pos-i)
        fuel += charge*(charge+1)/2
    
    fuel_list.append(fuel)
    
print(min(fuel_list))