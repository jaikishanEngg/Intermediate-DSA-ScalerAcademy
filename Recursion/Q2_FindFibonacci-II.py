#
# Created on Sat Apr 02 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:

Fn = Fn-1 + Fn-2

Given a number A, find and return the Ath Fibonacci Number.

Given that F0 = 0 and F1 = 1.

Problem Constraints
0 <= A <= 20

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the Ath term of the sequence.


Example Input
Input 1:
A = 2
Input 2:
A = 9

Example Output
Output 1:
    1
Output 2:
    34

Example Explanation
Explanation 1:
    f(2) = f(1) + f(0) = 1
Explanation 2:
    f(9) = f(8) + f(7) = 21 + 13  = 34
'''
class Solution:

    def findAthFibonacci(self, A):
        if(A >= 0):     #to check if A is a positive integer or not
            #base cases
            if(A == 0):     #fibonacci of 0 is 0
                return 0
            if(A == 1):     #fibonacci of 1 is 1
                return 1

            #recurrence relation                
            return self.findAthFibonacci(A - 1) + self.findAthFibonacci(A - 2)

s = Solution()
n = 2
ans = s.findAthFibonacci(n)
assert ans == 1

n = 9
ans = s.findAthFibonacci(n)
assert ans == 34

