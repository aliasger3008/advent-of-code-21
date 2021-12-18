#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:08:31 2021

@author: aliasger
"""

import numpy as np

# Opening and read input file given 
file = open('input','r')
content = file.read()
content_lines = content.split("\n")

lightmap = []

n = 100

flashes = 0

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
                                
def flash():
    global lightmap 
    
    n = 0
    
    if np.any(lightmap>9):
        
        for i in range(h):
            for j in range(w):
                if lightmap[i,j] == 10:
                    lightmap[i, j] = 0
                    n += 1
                    adj(i,j)   
        
        return n + flash()
    
    else:
        return 0


for it in range(n):
    
    lightmap += 1
    
    flashes += flash()
    
print(flashes)