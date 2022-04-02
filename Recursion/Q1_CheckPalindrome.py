#
# Created on Sat Apr 02 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Note: A palindrome is a string that's the same when read forward and backward.

Problem Constraints
1 <= A <= 50000
String A consists only of lowercase letters.

Input Format
The first and only argument is a string A.

Output Format
Return 1 if the string A is a palindrome, else return 0.

Example Input
Input 1:
A = "naman"
Input 2:
A = "strings"

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
    "naman" is a palindomic string, so return 1.
Explanation 2:
    "strings" is not a palindrome, so return 0.
'''

import sys

class Solution:

    def isPalindrome(self, string, i, j):
        #returns 1 if the string is palindrome else 0; using recursion
        if(i > j):
            return 1
        elif(string[i] != string[j]):
            return 0
        else:
            return self.isPalindrome(string, i+1, j-1)

    def solve(self, A):
        n = len(A)
        if(n > sys.getrecursionlimit()):
            sys.setrecursionlimit(n+2) #setting the default recursion limit
        return self.isPalindrome(A, 0, n - 1)
        
s = Solution()
A = "naman"
ans = s.solve(A)
assert ans == 1

A = "strings"
ans = s.solve(A)
assert ans == 0

A = "a"*50000
ans = s.solve(A)
assert ans == 1



