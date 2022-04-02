#
# Created on Sat Apr 02 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a number A, we need to find the sum of its digits using recursion.

Problem Constraints
1 <= A <= 109

Input Format
The first and only argument is an integer A.

Output Format
Return an integer denoting the sum of digits of the number A.

Example Input
Input 1:
    A = 46
Input 2:
    A = 11

Example Output
Output 1:
    10
Output 2:
    2

Example Explanation
Explanation 1:
    Sum of digits of 46 = 4 + 6 = 10
Explanation 2:
    Sum of digits of 11 = 1 + 1 = 2
'''
class Solution:
    def sumofDigits(self, n):
        if n == 0:
            return 0
        else:
            return self.sumofDigits(n//10) + n%10

    def solve(self, A):
        if(A >= 0):
            return self.sumofDigits(A)

s = Solution()
n = 46
ans = s.solve(n)
assert ans == 10

n = 11
ans = s.solve(n)
assert ans == 2
