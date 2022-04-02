#
# Created on Sat Apr 02 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Write a program to find the factorial of the given number A.

Problem Constraints
0 <= A <= 12

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the factorial of the number A.

Example Input
Input 1:
    A = 4
Input 2:
    A = 1

Example Output
Output 1:
    24
Output 2:
    1

Example Explanation
Explanation 1:
    Factorial of 4 = 4 * 3 * 2 * 1 = 24
Explanation 2:
    Factorial of 1 = 1
 '''
class Solution:

    def factorial(self, n):
        #base condition
        if n == 0:
            return 1
        else:
            #recurrence relation
            return self.factorial(n-1) * n

    def solve(self, A):
        if(A >= 0):
            return self.factorial(A)

s = Solution()
n = 4
ans = s.solve(n)
assert ans == 24

n = 0
ans = s.solve(n)
assert ans == 1
