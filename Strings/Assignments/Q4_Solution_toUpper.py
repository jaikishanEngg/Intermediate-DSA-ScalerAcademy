# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:44:32 2022

@author: Kishan
"""
class Solution:

    def to_upper(self, A):
        # Lets say 'a' ASCII value is 97 = 64 + 32 + 1
        # convert it into 'A' its ASCII value is 65 = 64 + 1
        # only 1 bit is different from these two. So, we can XOR with 32 to get it doen
        n = len(A)
        
        for i in range(n):
            if(ord(A[i]) >= 97 and ord(A[i]) <= 122):
                A[i] = chr(ord(A[i]) ^ 32)
        
        return A

s = Solution()

#test case1
A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
ans = s.to_upper(A)
assert ans ==  ['S', 'C', 'A', 'L', 'E', 'R', 'A', 'C', 'A', 'D', 'E', 'M', 'Y']

#test case2: with special chars
A = ['S', 'c', 'A', 'l', 'e', 'r', '#', 'A', 'c', 'a', 'D', 'e', 'm', 'y', '2','0','2','2']
ans = s.to_upper(A)
assert ans ==  ['S', 'C', 'A', 'L', 'E', 'R', '#','A', 'C', 'A', 'D', 'E', 'M', 'Y', '2','0','2','2']
