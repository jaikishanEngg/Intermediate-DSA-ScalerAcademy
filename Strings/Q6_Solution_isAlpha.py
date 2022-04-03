# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:58:53 2022

@author: Kishan
Problem Description

You are given a function isalpha() consisting of a character array A.

Return 1 if all the characters of the character array are alphabetical (a-z and A-Z), else return 0.

Problem Constraints

1 <= |A| <= 105
"""
class Solution:

    def isAlpha(self, char):
        if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
            return True
        else:
            return False
        
    def solve(self, A):
        # isAlphaNumeric
        # Check is it 65 to 90 for A-Z.  97 to 122 a-z. for 0 to 9 48-57
        n = len(A)
        
        for i in range(n):
            if(not self.isAlpha(A[i])):
                return 0
        else:
            return 1


s = Solution()

#test case 1
A = ['S', 'c', 'a', 'l', 'e', 'r']
ans = s.solve(A)
assert ans == 1

#Test case 2
A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
ans = s.solve(A)
assert ans == 0
