# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:34:18 2022

@author: Kishan
Problem Description

Given a string A, you are asked to reverse the string and return the reversed string.

Problem Constraints

1 <= |A| <= 105

String A consist only of lowercase characters.
"""
class Solution:

    def reverse(self, _string, startIndex, endIndex):
        i = startIndex
        j = endIndex
        
        while(i < j):
            _string[i], _string[j] = _string[j], _string[i]
            i += 1
            j -= 1
        
        return _string

    def solve(self, A):
        A = A.strip()   #remove the white spaces in the input string
        A = list(A)  #convert the string into a list of chars
        n = len(A)

        #reverse the whole string, just a simple reverse
        self.reverse(A, 0, n - 1)

        return "".join(A)
    
s = Solution()

#test case1: two words
A = "Elon Musk"
ans = s.solve(A)
assert ans == "ksuM nolE"

#test case2: single word
A = "Python"
ans = s.solve(A)
assert ans == "nohtyP"

#test case 3: with white spaces around
A = "  Hello World  "
ans = s.solve(A)
assert ans == "dlroW olleH"