# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:27:41 2022

@author: Kishan
Problem Description
Alex has a cat named Boomer. He decides to put his cat to the test for eternity.
He starts on day 1 with a stash of food unit, every next day, the stash doubles.
If Boomer is well behaved during a particular day, she receives food worth equal to the stash on that day.
Boomer receives a net worth of A units of food. What is the number of days he was well behaved?

Problem Constraints
1 <= A <= 231-1

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the number of days Boomer was well behaved.

Example Input
Input 1:
A = 5
Input 2:
A = 8

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
 To eat a total of 5 units of food, Boomer behaved normally on Day 1 and on the Day 3.
Explanation 2:
 To eat a total of 8 units of food, Boomer behaved normally only on day 4.
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
