#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:50:11 2026

@author: fkaka
"""

class Solution:
    def calcPermutation(self, n: int) -> int:
        output = 1
        for i in range(1, n + 1):
            output *= i
        return output

    def getPermutation(self, n: int, k: int) -> str:
        k -= 1  # convert to zero-based index
        
        all_str = [str(num) for num in range(1, n + 1)]
        out = ''
        
        factorial = self.calcPermutation(n)
        
        for i in range(n, 0, -1):
            factorial //= i  # (i-1)!
            
            index = k // factorial
            out += all_str[index]
            
            del all_str[index]
            
            k %= factorial
        
        return out