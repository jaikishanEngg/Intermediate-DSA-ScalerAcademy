# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:23:24 2022

@author: Kishan
Q2. First Repeating element

Problem Description

Given an integer array A of size N, find the first repeating element in it.
We need to find the element that occurs more than once and whose index of first occurrence is smallest.
If there is no repeating element, return -1.

Problem Constraints

1 <= N <= 105
1 <= A[i] <= 109
"""
class Solution:

    def solve(self, A):
        frequencyHashMap = dict()
        
        for i in A:
            if i in frequencyHashMap:
                frequencyHashMap[i] += 1
            else:
                frequencyHashMap[i] = 1
        
        for ele in A:
            if frequencyHashMap[ele] > 1:
                return ele
        else:
            return -1

s = Solution()
#test case 1
A = [10, 5, 3, 4, 3, 5, 6]
ans = s.solve(A)
assert ans == 5

#test case 2
A = [6, 10, 5, 4, 9, 120]
ans = s.solve(A)
assert ans == -1
