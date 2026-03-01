#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 09:50:36 2026

@author: fkaka
"""

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        i=1
        if (k%2==0)|(k%5==0):
            return -1
        else:
            while n%k!=0:
                n = n*10 + 1
                i+=1
            
            return i
    