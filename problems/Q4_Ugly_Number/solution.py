#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 11:03:26 2026

@author: fkaka
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        prime_factors = {2,3,5}
        remaining=n
        if n==1:
            return True
        elif n<=0:
            return False
        else: 
            for pf in prime_factors:
                if remaining%pf==0:
                    
                    while remaining%pf==0:
                        remaining = remaining/pf
    
            if remaining==1:
                return True
            else:
                return False
