# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:02:56 2022

@author: Kishan
Q1. Common Elements

Problem Description

Given two integer array A and B of size N and M respectively. Your task is to find all the common elements in both the array.

NOTE:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Problem Constraints
1 <= N, M <= 105

1 <= A[i] <= 109
"""
class Solution:

    def solve(self, A, B):
        hashMap_A = dict()
        hashMap_B = dict()
        
        for i in A:
            if i in hashMap_A:
                hashMap_A[i] += 1
            else:
                hashMap_A[i] = 1

        for i in B:
            if i in hashMap_B:
                hashMap_B[i] += 1
            else:
                hashMap_B[i] = 1
        
        common_items = list(set(A).intersection(set(B)))
        
        ans = []
        
        for ele in common_items:
            ans += [ele,] * min(hashMap_A[ele], hashMap_B[ele]) 
        
        ans.sort()
        return ans

s = Solution()
#test case 1
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
ans = s.solve(A, B)       
assert ans == [1, 2, 2]

#test case 2
A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]
ans = s.solve(A, B)       
assert ans == [2, 10]
