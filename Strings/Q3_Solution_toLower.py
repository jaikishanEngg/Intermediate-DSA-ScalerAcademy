# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:34:34 2022

@author: Kishan

Problem Description
You are given a function to_lower() which takes a character array A as an argument.

Convert each character of A into lowercase character if it exists. If the lowercase of a character does not exist, it remains unmodified.
The uppercase letters from A to Z is converted to lowercase letters from a to z respectively.

Return the lowercase version of the given character array.
"""
class Solution:

    def to_lower(self, A):
        # Lets say 'A' ASCII value is 65 = 64 + 1
        # convert it into 'a' its ASCII value is 97 = 64 + 32 + 1
        # only 1 bit is different from these two. So, we can XOR with 32 to get it doen
        n = len(A)
        
        for i in range(n):
            if(ord(A[i]) >= 65 and ord(A[i]) <= 65+25):
                A[i] = chr(ord(A[i]) ^ 32)
        
        return A

s = Solution()

#test case1
A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
ans = s.to_lower(A)
assert ans ==  ['s', 'c', 'a', 'l', 'e', 'r', 'a', 'c', 'a', 'd', 'e', 'm', 'y']

#test case2: with special chars
A = ['S', 'c', 'A', 'l', 'e', 'r', '#', 'A', 'c', 'a', 'D', 'e', 'm', 'y', '2','0','2','2']
ans = s.to_lower(A)
assert ans == ['s', 'c', 'a', 'l', 'e', 'r', '#', 'a', 'c', 'a', 'd', 'e', 'm', 'y', '2','0','2','2']

