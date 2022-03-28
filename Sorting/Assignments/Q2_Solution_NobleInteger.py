# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:54:55 2022

@author: Kishan

Problem Description
Given an integer array A, find if an integer p exists in the array such that 
the number of integers greater than p in the array equals p.

Problem Constraints
1 <= |A| <= 2*105
1 <= A[i] <= 107
"""
class Solution:
    
    def solve(self, A):
        A.sort(reverse = True) #by sorting it in the descending order, 
            #first element is always greatest one. So, like-wise at index 'i' 0 to i-1 elements are >= A[i]
            
        n = len(A)
        
        nobleIntegerCount = 0

        temp = 0
        if(A[0] == 0):
            nobleIntegerCount += 1
        
        for i in range(1, n):
            if(A[i] != A[i-1]):
                temp = i
                if(A[i] == temp):
                    nobleIntegerCount += 1
        
        if(nobleIntegerCount):
            return 1 #as there is a noble integer, return True
        else:
            return -1 ##as there is no noble integer, return False

s = Solution()

#test case 1
A = [3, 2, 1, 3] # For integer 2, there are 2 greater elements in the array..
ans = s.solve(A)
assert ans == 1

#test case 2: Negative test case
A = [1, 1, 3, 3]
ans = s.solve(A)
assert ans == 0
