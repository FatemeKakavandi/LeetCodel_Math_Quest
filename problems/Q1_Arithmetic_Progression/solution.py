#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:37:43 2026

@author: fkaka
"""

import numpy as np 

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        
        sub = arr[1] - arr[0]
        for i in np.arange(len(arr)-1):

            if sub == (arr[i+1] - arr[i]):
                sub = arr[i+1] - arr[i]
                output = True
            else:
                return False
        return output
