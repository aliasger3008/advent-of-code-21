#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:41:40 2021

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
    
    


winner = np.empty(shape=(5,5))
win = 0

for num in pick_no:
    for board in boards_list:
        
        if num in board:
            index_x, index_y = np.where(board == num)
            board[index_x, index_y] = np.nan
            
        for i in range(5):
            cnt = 0
            for j in range(5):
                if np.isnan(board[i,j]):
                    cnt = cnt + 1
            if cnt == 5:
                winner = board
                win = 1
                break
                
        for i in range(5):
            cnt = 0
            for j in range(5):
                if np.isnan(board[j,i]):
                    cnt = cnt + 1
            if cnt == 5:
                winner = board
                win = 1
                break
            
    if win == 1:
        break

print(num*np.nansum(winner))
                
                
        
    