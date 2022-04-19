#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.



Problem Constraints
1 <= A <= 16



Input Format
The first argument is an integer A.



Output Format
Return an array of integers representing the gray code sequence.



Example Input
Input 1:

A = 2
Input 1:

A = 1


Example Output
output 1:

[0, 1, 3, 2]
output 2:

[0, 1]


Example Explanation
Explanation 1:

for A = 2 the gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
So, return [0,1,3,2].
Explanation 1:

for A = 1 the gray code sequence is:
    00 - 0
    01 - 1
So, return [0, 1].
'''
class Solution:
    # @param A : integer
    # @return a list of integers

    def grayCode(self, n):
        #as per the constrains n >= 1 where n indicates the number of bits.
        #so, the number of gray codes that can be generated will be 2**n
        grayCodes = [0] 
        for i in range(n):
            currSize = len(grayCodes)
            for j in range(currSize -1, -1, -1):
                nextGrayCode = grayCodes[j] + (1<<i)
                grayCodes.append(nextGrayCode)
        
        return grayCodes

s = Solution()
ans = s.grayCode(n = 2)
assert ans == [0, 1, 3, 2]

ans = s.grayCode(n = 1)
assert ans == [0, 1]


