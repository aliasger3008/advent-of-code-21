#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:53:15 2021

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
    
# Position coordinates   
hor_pos = 0
depth = 0
 
# Logic for calculating position
for command in content_list:
    temp = list(command.split())
    move = temp[0]
    magnitude = int(temp[1])
    if(move == "forward"):
        hor_pos = hor_pos + magnitude
    else:
        if(move == "down"):
            depth = depth + magnitude
        else:
            depth = depth - magnitude
            
# Final position
final_pos = hor_pos*depth

print(final_pos)
        
    
    
    

