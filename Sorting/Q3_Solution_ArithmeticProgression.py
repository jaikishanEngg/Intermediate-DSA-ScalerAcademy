# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 23:14:26 2022

@author: Kishan
Problem Description
Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Problem Constraints
2 <= N <= 105

-109 <= A[i] <= 109
"""
class Solution:

    def solve(self, A):
        #since we need to check if the elements of A are in AP
        #series of AP looks like a, a+d, a+2d, a+3d.... a+(n-1)d
        n = len(A)
        
        A.sort()
        _diff = A[0] - A[1]
        
        for i in range(1, n-1):
            if A[i] - A[i+1] != _diff:
                return 0 #if the series difference is not same then return False, as its not in AP
        else:
            return 1 #exhausting the all elements and we didn't find any discrepancy, the difference between 
                    #each two consecutive elements is same. so, return True

s = Solution()

#test case 1
A = [3, 5, 1]
ans = s.solve(A)
assert ans == 1

#test case 2: negative test case
A = [2, 4, 1]
ans = s.solve(A)
assert ans == 0