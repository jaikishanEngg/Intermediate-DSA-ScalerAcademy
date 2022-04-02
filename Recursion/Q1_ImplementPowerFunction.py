#
# Created on Sat Apr 02 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).

Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.

Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109

Input Format
Given three integers A, B, C.

Output Format
Return an integer.

Example Input
A = 2, B = 3, C = 3

Example Output
2

Example Explanation
23 % 3 = 8 % 3 = 2
'''
class Solution:

    def pow(self, A, B, C):
        if B == 0:
            return 1%C
        half_power = self.pow(A, B//2, C)
        if(B%2 == 0):
            return (half_power%C * half_power%C)%C
        else:
            return (half_power%C * half_power%C * A%C)%C
        
s = Solution()
ans = s.pow(2,3,3)  # 2**3 %3 
assert ans == 2
