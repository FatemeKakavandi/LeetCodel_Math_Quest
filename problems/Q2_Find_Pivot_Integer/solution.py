#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:11:43 2026

@author: fkaka
"""
import numpy as np 

class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = 0
        if n==1:
            return 1
        else:
            for i in range(n):

                right_sum += (n-i)

                for j in range(n):
                    left_sum +=j
                    if (left_sum==right_sum)&((n-i)==j):
                        return j
                left_sum=0
            
            return -1
    def math_pvi(self,n:int)->int:
        sqr_value = n*(n+1)/2
        sqrt_value =int(np.sqrt(sqr_value))
        if sqr_value == sqrt_value*sqrt_value:
            return sqrt_value
        else:
            return -1
        

print(Solution().math_pvi(n=8))