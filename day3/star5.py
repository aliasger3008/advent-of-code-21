#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:13:58 2021

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

epsilon = ""
gamma = ""

for i in range(len(content_list[0])):
    cnt_0 = 0
    cnt_1 = 0
    
    for j in content_list:
        if j[i] == '0':
            cnt_0 = cnt_0 + 1
        else:
            cnt_1 = cnt_1 + 1
            
    if cnt_0>cnt_1:
        epsilon = epsilon + "1"
        gamma = gamma + "0"
    else:
        epsilon = epsilon + "0"
        gamma = gamma + "1"

epsilon = int(epsilon,2)
gamma = int(gamma,2)

power_cons = epsilon*gamma

print(power_cons)



        
        