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
#This code only works on Python 2.x
#This takes O(n logn) time complexity;
class Solution:

    def cmp_item(self, a, b):
        if long(a+b) > long(b+a):
            return -1
        elif long(a+b) == long(b+a):
            return 0
        else:
            return 1

    def largestNumber(self, A):
        A = list(map(str, A))

        A = sorted(A, cmp = self.cmp_item)
        
        return str(long("".join(A)))

s = Solution()

#test case 1
A = [3, 30, 34, 5, 9]
ans = s.largestNumber(A)
assert ans ==  "9534330"

#test case 2
A = [0,0,0,0]
ans = s.largestNumber(A)
assert ans ==  "0"
