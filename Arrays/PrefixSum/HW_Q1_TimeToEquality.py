#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.

Problem Constraints
    1 <= N <= 1000000
    1 <= A[i] <= 1000

Input Format
    First argument is an integer array A.

Output Format
    Return an integer denoting the minimum time to make all elements equal.

Example Input
    A = [2, 4, 1, 3, 2]

Example Output
    8

Example Explanation
    We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        _max = max(A)
        noOfSecs = 0
        for i in range(len(A)):
            noOfSecs += abs(A[i] - _max)
        return noOfSecs

s = Solution()
A = [2, 4, 1, 3, 2]
ans = s.solve(A)
assert ans == 8