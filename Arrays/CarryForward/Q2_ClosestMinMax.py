#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.

Problem Constraints
1 <= |A| <= 2000

Input Format
First and only argument is vector A

Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array

Example Input
Input 1:
    A = [1, 3]
Input 2:
    A = [2]

Example Output
Output 1:
    2
Output 2:
    1

Example Explanation
Explanation 1:
    Only choice is to take both elements.
Explanation 2:
    Take the whole array.
'''
import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        Amin = min(A)
        Amax = max(A)
        n = len(A)
        last_max_index = -1
        last_min_index = -1
        distance = math.inf
        if(Amin == Amax):
            return 1 #distance would be that segment itself and its 1
        for i in range(n):
            if(A[i] == Amax):
                last_max_index = i
            if(A[i] == Amin):
                last_min_index = i
            if(last_max_index != -1 and last_min_index != -1):
                distance = min(distance, abs(last_max_index - last_min_index) + 1)
        
        return distance

s = Solution()
A = [1, 3]
ans = s.solve(A)
assert ans == 2

A = [2]
ans = s.solve(A)
assert ans == 1


