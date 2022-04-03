# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 23:22:59 2022

@author: Kishan
Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*
Hint: https://portingguide.readthedocs.io/en/latest/comparisons.html
"""
#This code only works on Python 3.x
#This code takes O(n^2)

class Solution:

    def largestNumber(self, A):
        A = list(map(str, A)) #convert the int list into str list
        A.sort(reverse = True)
        #print("Before Loop: ", A)

        n = len(A) - 1

        for i in range(n):
            j = i + 1
            while(j <= n and A[i][0] == A[j][0]):
                if(int(A[i] + A[j]) < int(A[j] + A[i])):
                    #place A[j] element at ith position
                    temp = A[j]
                    del A[j:j+1]
                    A.insert(i, temp)
                j += 1
        #print(A)            
        return str(int("".join(A)))

s = Solution()

#test case 1
A = [3, 30, 34, 5, 9]
ans = s.largestNumber(A)
assert ans ==  "9534330"

#test case 2
A = [0,0,0,0]
ans = s.largestNumber(A)
assert ans ==  "0"
