#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 12:20:54 2026

@author: fkaka
"""

import pytest 

from problems.Q1_Permutation_Sequence.solution import Solution 

def test_correctness():
    perm_cls = Solution()
    assert perm_cls.getPermutation(n=3,k=3)=="213"
    assert perm_cls.getPermutation(n=4,k=9)=="2314"
    assert perm_cls.getPermutation(n=3,k=1)=="123"
    

