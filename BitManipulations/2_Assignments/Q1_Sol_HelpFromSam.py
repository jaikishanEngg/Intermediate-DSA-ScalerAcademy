# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:53:47 2022

@author: Kishan
Problem Description
Alex and Sam are good friends. Alex is doing a lot of programming these days. He has set a target score of A for himself.
Initially, Alex's score was zero. Alex can double his score by doing a question, or Alex can seek help from Sam for doing questions that will contribute 1 to Alex's score. Alex wants his score to be precisely A. Also, he does not want to take much help from Sam.

Find and return the minimum number of times Alex needs to take help from Sam to achieve a score of A.

Problem Constraints
0 <= A <= 10^9

Input Format
The only argument given is an integer A.

Output Format
Return the minimum number of times help taken from Sam.

Example Input
Input 1:
A = 5
Input 2:
A = 3

Example Output
Output 1:
2
Output 2:
2

Example Explanation
Explanation 1:
Initial score : 0
Takes help from Sam, score : 1
Alex solves a question, score : 2
Alex solves a question, score : 4
Takes help from Sam, score: 5
Explanation 2:

Initial score : 0
Takes help from Sam, score : 1
Alex solves a question, score : 2
Takes help from Sam, score : 3
"""
#Hint: Count number of 1's in the binary representation of A

class Solution:
    # @param A : integer
    # @return an integer
    def countOnes_BasicApproach(self, n):
        #We can check if the LSB bit is set or not using '&' 
        #so, we will keep right shifting all the bits to LSB and count if the LSB bit is 1 by doing (& 1)
        #it will iterate through each bit, so complexity is log N base 2, where N is the number of bits 
        count_ones = 0

        while(n):
            if n & 1:
                count_ones += 1
            n = n >> 1

        return count_ones
    
    def countOnes_IntuitiveApproach(self, n):
        #this approach will only count the number of 1s in the binary rep., 
        #rather it will not iterate over all the bits like the basic approach
        #in worst case both approaches give O(log N) but this approach is efficient in case of avg and best cases
        count_ones = 0

        while(n > 0):
            n = n & (n-1)
            count_ones += 1
        
        return count_ones
            
    def solve(self, A):
        if(A == 0):
            return A
        #return self.countOnes_BasicApproach(A)
        return self.countOnes_IntuitiveApproach(A)

s = Solution()

#test case 1: when it is 0
ans = s.solve(0)
assert ans == 0

#test case 2
ans = s.solve(1)
assert ans == 1

#test case 3
ans = s.solve(2)
assert ans == 1

#test case 4
ans = s.solve(17)
assert ans == 2
