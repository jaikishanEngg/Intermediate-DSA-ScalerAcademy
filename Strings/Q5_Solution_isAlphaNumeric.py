# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:46:10 2022

@author: Kishan
Problem Description

You are given a function isalpha() consisting of a character array A.

Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z and 0-9), else return 0.

Problem Constraints

1 <= |A| <= 105
"""
class Solution:

    def isAlphaNumeric(self, char):
        if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 57)):
            return True
        else:
            return False
        
    def solve(self, A):
        # isAlphaNumeric
        # Check is it 65 to 90 for A-Z.  97 to 122 a-z. for 0 to 9 48-57
        n = len(A)
        
        for i in range(n):
            if(not self.isAlphaNumeric(A[i])):
                return 0
        else:
            return 1

s = Solution()

#test case1: positive test case
A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
ans = s.solve(A)
assert ans == 1

#test case2: with special chars 
A = ['S', 'c', 'A', 'l', 'e', 'r', '#', 'A', 'c', 'a', 'D', 'e', 'm', 'y', '2','0','2','2']
ans = s.solve(A)
assert ans ==  0
