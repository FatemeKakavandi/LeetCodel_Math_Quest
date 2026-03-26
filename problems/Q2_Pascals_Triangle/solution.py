#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:28:33 2026

@author: fkaka
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out_list = [[1],[1,1]]
        if numRows==1:
            return [out_list[0]]
        elif numRows==2:
            return out_list
        else:
            for i in range(1,numRows-1):
                new_row = [1]
                for idx in range(len(out_list[-1])-1):
                    new_row+=[out_list[-1][idx]+out_list[-1][idx+1]]
                
                new_row+=[1]
                out_list+=[new_row]
            return out_list