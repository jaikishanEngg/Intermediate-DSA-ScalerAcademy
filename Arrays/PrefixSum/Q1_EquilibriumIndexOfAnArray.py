#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

NOTE:
Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.

Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105

Input Format
First arugment is an array A .

Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.

Example Input
Input 1:
A=[-7, 1, 5, 2, -4, 3, 0]

Input 2:
A=[1,2,3]

Example Output
Output 1:
    3
Output 2:
    -1

Example Explanation
Explanation 1:
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Explanation 2:
There is no such index.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        arr = A
        leftsum = list()
        rightsum = list()
        n = len(arr)

        #Generating the prefix array 
        prefix_sum = list()
        prefix_sum.append(arr[0])
        for i in range(1, n):
            prefix_sum.append(prefix_sum[i-1] + arr[i])

        #Generate left and right sum arrays
        for i in range(n):
            if(i ==0):
                leftsum.append(0)
            else:
                leftsum.append(prefix_sum[i-1])
            rightsum.append(prefix_sum[n-1] - prefix_sum[i])

        #return if there is an equilibrium index else -1
        for i in range(n):
            if(leftsum[i] == rightsum[i]):
                return i
        else:
            return -1

s = Solution()
#Test case 1: positive test case
A = [-7, 1, 5, 2, -4, 3, 0]
ans = s.solve(A)
assert ans == 3

#Test case 2: Negative test case
A = [1,2,3]
ans = s.solve(A)
assert ans == -1

