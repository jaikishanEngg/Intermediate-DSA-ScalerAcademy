# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 23:28:54 2022

@author: Kishan
Problem Description
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.

Problem Constraints
0 <= N <= 1000
1 <= A[i] <= 103
"""
#Hint: If we keep remving the biggest elements from the array, then 
#in the 1st iteration, if we remove it, in the total cost it is added once
#similarly the n-th element removed, will be added n-times in the total cost.

class Solution:

    def solve(self, A):
        A.sort(reverse = True)
        n = len(A)
        ans = 0

        for i in range(n):
            ans += (i+1)*A[i]
        
        return ans

s = Solution()

#Test case 1
A = [2, 1]
ans = s.solve(A)
assert ans == 4

#Test case 2
A = [5]
ans = s.solve(A)
assert ans == 5
