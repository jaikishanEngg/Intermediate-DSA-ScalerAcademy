# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:50:46 2022

@author: Kishan
Problem Description
Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

Note: Using the library sort function is not allowed.

Problem Constraints
1 <= N <= 1000000
0 <= A[i] <= 2
"""
#Hint: We will use courting sort technique
class Solution:

    def sortColors(self, A):
        #red, while, blue = 0, 1, 2
        n = len(A)
        
        count_zeros = 0
        count_ones = 0
        count_twos = 0
        
        for i in range(n):
            if(A[i] == 0):
                count_zeros += 1
            elif(A[i] == 1):
                count_ones += 1
            else:
                count_twos += 1
        
        return [0]*count_zeros + [1]*count_ones + [2]*count_twos

#test case 1
s = Solution()
A = [0, 1, 2, 0, 1, 2]
ans = s.sortColors(A)        
assert ans == [0, 0, 1, 1, 2, 2]

#test case 2
A = [0]
ans = s.sortColors(A)        
assert ans == [0]
