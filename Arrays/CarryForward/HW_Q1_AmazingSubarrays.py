#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
You are given a string S, and you have to find all the amazing substrings of S.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input
Only argument given is string S.

Output
Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.

Constraints
    1 <= length(S) <= 1e6
    S can have special characters

Example
Input
    ABEC
Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.
'''
class Solution:

    def solve(self, A):
        n = len(A)
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        count = 0

        for i in range(n):
            if(A[i] in vowels):
                count += ((n - 1) - i + 1)
        
        return count%10003

s = Solution()
A = "ABEC"
ans = s.solve(A)
assert ans == 6

