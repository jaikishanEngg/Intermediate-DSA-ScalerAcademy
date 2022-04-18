#
# Created on Mon Apr 18 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given an array of integers A of size N.
The value of a subarray is defined as BITWISE OR of all elements in it.
Return the sum of value of all subarrays of A % 109 + 7.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 108

Input Format
The first argument given is the integer array A.

Output Format
Return the sum of Value of all subarrays of A % 109 + 7.

Example Input
Input 1:
    A = [1, 2, 3, 4, 5]
Input 2:
    A = [7, 8, 9, 10]

Example Output
Output 1:
    71
Output 2:
    110

Example Explanation
Explanation 1:

 Value([1]) = 1
 Value([1, 2]) = 3
 Value([1, 2, 3]) = 3
 Value([1, 2, 3, 4]) = 7
 Value([1, 2, 3, 4, 5]) = 7
 Value([2]) = 2
 Value([2, 3]) = 3
 Value([2, 3, 4]) = 7
 Value([2, 3, 4, 5]) = 7
 Value([3]) = 3
 Value([3, 4]) = 7
 Value([3, 4, 5]) = 7
 Value([4]) = 4
 Value([4, 5]) = 5
 Value([5]) = 5
 Sum of all these values = 71

Explanation 2:
    Sum of value of all subarray is 110.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0
        for i in range(n):
            orsum = 0
            for j in range(i,n):
                orsum |= A[j]
                ans += orsum
        return ans
            
s = Solution()

A = [ 347148, 221001, 394957, 729925, 276769, 40726, 552988, 29952, 184491, 146773, 418965, 
307, 219145, 183037, 178111, 81123, 109199, 683929, 422034, 346291, 11434, 7327, 340473, 
316152, 364005, 359269, 170935, 105784, 224044, 22563, 48561, 165781, 9329, 357681, 169473, 
175031, 605611, 374501, 6607, 329965, 76068, 836137, 103041, 486817, 195549, 107317, 34399, 
56907, 37477, 189690, 36796, 376663, 39721, 177563, 174179, 183646, 217729, 408031, 429122, 
631665, 282941, 526797, 262186, 306571, 63613, 57501, 70685, 226381, 1338, 9360, 130360, 20300, 
400906, 87823, 180349, 108813, 18181, 119185, 1, 102611, 63591, 12889, 311185, 383896, 8701, 
76077, 75481, 386017, 153553, 304913, 383455, 105948, 142885, 1, 12610, 137005, 
119185, 16948, 66171, 123683]

print(s.solve(A))
