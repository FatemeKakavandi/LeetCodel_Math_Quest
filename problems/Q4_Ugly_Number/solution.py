#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 11:03:26 2026

@author: fkaka
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        prime_factors = {2,3,5}
        all_prime_factors=[]
        remaining=n
        if n==1:
            return True
        else: 
            for pf in prime_factors:
                if remaining%pf==0:
                    remaining = int(remaining/pf)
                    s = 2
                    pf_power = pow(pf,s)
                    while pf_power<(int(n/2)+1):
                        if n%pf_power==0:
                            remaining = int(n/pf_power)
                            print(remaining)
                            s+=1
                            pf_power = pow(pf,s)
                        else:
                            break
                        
            if remaining==1:
                return True
            else:
                return False
                        
# Tests cases: 36, 8
ugly_num = Solution()
print(ugly_num.isUgly(8))