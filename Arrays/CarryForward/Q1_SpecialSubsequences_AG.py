#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You have given a string A having Uppercase English letters.
You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.

Problem Constraints
1 <= length(A) <= 105

Input Format
    First and only argument is a string A.

Output Format
    Return an integer denoting the answer.

Example Input
Input 1:
    A = "ABCGAG"
Input 2:
    A = "GAB"

Example Output
Output 1:
    3
Output 2:
    0

Example Explanation
Explanation 1:
    Subsequence "AG" is 3 times in given string 

Explanation 2:
    There is no subsequence "AG" in the given string.
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 0
        n = len(A) - 1
        count_g = 0
        for i in range(n, -1, -1):
            if(A[i] == 'G'):
                count_g += 1
            if(A[i] == 'A'):
                ans += count_g
        return ans%(10**9 + 7)

s = Solution()
#Test case 1: positive test case
A = "ABCGAG"
ans = s.solve(A)
assert ans == 3

#Test case 1: negative test case
A = "GAB"
ans = s.solve(A)
assert ans == 0