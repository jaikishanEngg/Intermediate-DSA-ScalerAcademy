#
# Created on Sat Apr 02 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
Given row A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.) (1 indexed).

Problem Constraints
    1 <= A <= 20
    1 <= B <= 2A - 1

Input Format
    First argument is an integer A.
    Second argument is an integer B.
Output Format
    Return an integer denoting the Bth indexed symbol in row A.

Example Input
Input 1:
    A = 2    B = 1
Input 2:
    A = 2    B = 2

Example Output
Output 1:    0
Output 2:    1

Example Explanation
Explanation 1:
    Row 1: 0
    Row 2: 01
Explanation 2:
    Row 1: 0
    Row 2: 01

observations:
0
01
0110
01101001
0110100110010110

fun(n):
    if n == 1:
        return "0"
    else:
        return fun(n-1) concat inversefunc(n-1)

inversefunct(n):
    l = len(n)
    1111111's of length l ===> "1" * l
    bitwise or of above with n results into 1's complement
'''
class Solution:
    def kthSymbol(self, n):
        if n == 1:
            return "0"
        else:
            return self.kthSymbol(n-1) + 

    def solve(self, A, B):
        pass
