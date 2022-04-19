#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109
1 <= L <= R <= N

Input Format
The first argument is the integer array A.
The second argument is the 2D integer array B.

Output Format
Return an integer array of length M where ith element is the answer for ith query in B.

Example Input
Input 1:
    A = [1, 2, 3, 4, 5]
    B = [[1, 4], [2, 3]]

Input 2:
    A = [2, 2, 2]
    B = [[1, 1], [2, 3]]

Example Output
Output 1:
    [10, 5]

Output 2:
    [2, 4]

Example Explanation
Explanation 1:
    The sum of all elements of A[1 ... 4] = 1 + 2 + 3 + 4 = 10.
    The sum of all elements of A[2 ... 3] = 2 + 3 = 5.

Explanation 2:
    The sum of all elements of A[1 ... 1] = 2 = 2.
    The sum of all elements of A[2 ... 3] = 2 + 2 = 4.
'''
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        n = len(A)
        #Generate PreFixSum array
        prefixSumArr = []
        prefixSumArr.append(A[0])
        for i in range(1, n):
            prefixSumArr.append(A[i] + prefixSumArr[i-1])

        resultArr = []
        m = len(B)

        for i in range(m):
            L = B[i][0] - 1
            R = B[i][1] - 1
            if(L == 0):
                resultArr.append(prefixSumArr[R])
            else:
                resultArr.append(prefixSumArr[R] - prefixSumArr[L - 1])
        return resultArr

s = Solution()
A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3]]
ans = s.rangeSum(A, B)
assert ans == [10, 5]

A = [2, 2, 2]
B = [[1, 1], [2, 3]]
ans = s.rangeSum(A, B)
assert ans == [2, 4]
