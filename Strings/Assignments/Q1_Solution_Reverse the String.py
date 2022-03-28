# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:02:01 2022

@author: Kishan

Problem Description

You are given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

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
        A = A.strip() #removes the white spaces at both ends of the input string
        A = list(A) #convert the string into a list of chars
        n = len(A)
        
        #reverse the whole string, so that the words are in-place but just that they're in reversed
        self.reverse(A, 0, n - 1)
        l = 0; r = 0
        
        #as the words are in reveresed order, lets fix them in the following loop
        for i in range(n):
            #find the occurance of a space then if we reverse it from l to space index it will be intact.
            #an edge case is end of string will never have a space, so consider r == n-1
            if(A[i] == ' ' or r == n - 1):
                if(i == n-1):
                    self.reverse(A, l, r)
                else:
                    self.reverse(A, l, r - 1)
                l = r + 1
            
            r += 1
        
        return "".join(A)               

s = Solution()

#test case1: two words
A = "Elon Musk"
ans = s.solve(A)
assert ans == "Musk Elon"

#test case2: single word
A = "Python"
ans = s.solve(A)
assert ans == "Python"

#test case 3: with white spaces around
A = "  Hello World  "
ans = s.solve(A)
assert ans == "World Hello"