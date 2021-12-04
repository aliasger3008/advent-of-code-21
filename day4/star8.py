#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 20:47:47 2021

@author: aliasger
"""

import numpy as np

# Opening and read input file given 
file = open('input','r')
content = file.read()

# Shift to a list
content_list = content. split("\n")

# The list of numbers for the game 
pick_no = list(map(int, content_list[0].split(',')))



def boards(content_list, start, gap):
    i = start
    boards_list = []
    while(i<(len(content_list)-1)):
        x = np.empty(shape=(5,5))
        ind = 0
        for j in range(i,i+5):
            row = list(map(int, content_list[j].split()))
            x[ind] = row
            ind= ind+1
        boards_list.append(x)
        i = i + gap
    return boards_list

       
boards_list = boards(content_list,2,6)
total = len(boards_list)

loser = np.empty(shape=(5,5))

for num in pick_no:
    
    z = 0
    
    
    while z<len(boards_list):
        
        board = boards_list[z]
        
        if num == 81:
            print(z, len(boards_list), board)
        
        flag = 0
        if num in board:
            index_x, index_y = np.where(board == num)
            board[index_x, index_y] = np.nan
            
        for i in range(5):
            cnt = 0
            for j in range(5):
                if np.isnan(board[i,j]):
                    cnt = cnt + 1
            if cnt == 5:
                del boards_list[z]
                flag = 1
                break
        
        if flag == 1:
            z += 1
            continue
            
        for i in range(5):
            cnt = 0
            for j in range(5):
                if np.isnan(board[j,i]):
                    cnt = cnt + 1
            if cnt == 5:
                del boards_list[z]
                flag = 1
                break
        
        z += 1
               
    if len(boards_list) == 1:
        loser = boards_list[0]
        break

for n in pick_no[:pick_no.index(num)+1]:
    if n in loser:
        index_x, index_y = np.where(loser == n)
        loser[index_x, index_y] = np.nan
        
sum_mat = np.nansum(loser)
print(num*np.nansum(loser))