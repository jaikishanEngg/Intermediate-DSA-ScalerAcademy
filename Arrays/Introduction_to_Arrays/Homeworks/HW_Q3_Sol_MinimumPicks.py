# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:16:08 2022

@author: Kishan

Problem Description
You are given an array of integers A of size N.
Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.

"""
#maximum of all even numbers - min of all odd numbers
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.
        n = len(A)
        maxEvenVal = None
        minOddVal = None

        for i in range(n):
            if(A[i] & 1 == 1):
                #its an odd number
                if(minOddVal == None or A[i] < minOddVal):
                    minOddVal = A[i]
            
            else:
                #its an even number
                if(maxEvenVal == None or A[i] > maxEvenVal):
                    maxEvenVal = A[i]

        return maxEvenVal - minOddVal

s = Solution()

#test case 1
A = [ -98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ]
ans = s.solve(A)
assert ans == 151
