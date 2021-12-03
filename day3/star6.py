#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:36:44 2021

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

oxygen_list = content_list
co2_list = content_list

for i in range(len(content_list[0])):
    cntO_0 = 0
    cntO_1 = 0
    cntC_0 = 0
    cntC_1 = 0
    
    if len(oxygen_list)>1:
    
        for j in oxygen_list:
            if j[i] == '0':
                cntO_0 = cntO_0 + 1
            else:
                cntO_1 = cntO_1 + 1
            
        if cntO_0>cntO_1:
            oxygen_list = [o for o in oxygen_list if o[i] == "0"]
        else:
            oxygen_list = [o for o in oxygen_list if o[i] == "1"]
            
    if len(co2_list)>1:
        
        for k in co2_list:
            if k[i] == '0':
                cntC_0 = cntC_0 + 1
            else:
                cntC_1 = cntC_1 + 1
    
        if cntC_0>cntC_1:
            co2_list = [c for c in co2_list if c[i] == "1"]
        else:
            co2_list = [c for c in co2_list if c[i] == "0"]
            
    
    
oxy = int(oxygen_list[0],2)
co2 = int(co2_list[0],2)    

life_supp = oxy*co2

print(life_supp)

