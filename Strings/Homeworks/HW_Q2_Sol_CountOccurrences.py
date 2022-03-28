# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:23:49 2022

@author: Kishan
Q2. Count Occurrences
Problem Description

Find number of occurrences of bob in the string A consisting of lowercase english alphabets.

Problem Constraints

1 <= |A| <= 1000
"""
class Solution:
    def bobCount(self, _str, index):
        count = 0
        n = len(_str)
        i = 0
        
        while(i < n):
            try:
                i = _str.index('bob', i) + 1
                count += 1

            except ValueError:
                return count
            
        return count
    
    def solve(self, A):        
        return self.bobCount(A, 0)
        
s = Solution()
#test case 1
A = "abobc"
ans = s.solve(A)
assert ans == 1

#test case 2
A = "bobob"
ans = s.solve(A)
assert ans == 2
