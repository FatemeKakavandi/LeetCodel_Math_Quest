#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 09:45:21 2026

@author: fkaka
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (0<=x):
            if (int(str(x)[::-1])==x):
                return True
            else:
                return False
        else:
            return False