#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:24:40 2021

@author: aliasger
"""

import numpy as np

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")

lightmap = []

n = 1000

flashes = 0

step = 0

for line in content_lines:
    lightmap.append(list(map(int, line)))
  
h = len(lightmap)
w = len(lightmap[0])    

lightmap  = np.array(lightmap)
    

def adj(i,j):
    global lightmap
    
    for di,dj in [ [-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1] ]:
        ni,nj=i+di,j+dj
        if 0<=ni<10 and 0<=nj<10:
            if lightmap[ni, nj]!=10 and lightmap[ni, nj]!=0:
                lightmap[ni, nj]+=1	
            
                                
def flash(it):
    global lightmap
    global step
    
    n = 0
    
    if np.all(lightmap == 0):
        if step == 0:
            step = it+1
    
    if np.any(lightmap>9):
        
        for i in range(h):
            for j in range(w):
                if lightmap[i,j] == 10:
                    lightmap[i, j] = 0
                    n += 1
                    adj(i,j)   
        
        return n + flash(it)
    
    else:
        return 0


for it in range(n):
    
    lightmap += 1
    
    flashes += flash(it)
    
print(step)