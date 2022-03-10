# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:51:28 2022
@author: Kishan

Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer which occurs once.
NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Problem Constraints
2 <= |A| <= 2000000
0 <= A[i] <= INTMAX

Input Format
First and only argument of input contains an integer array A.

Output Format
Return a single integer denoting the single element.

Example Input
Input 1:
 A = [1, 2, 2, 3, 1]
Input 2:
 A = [1, 2, 2]

Example Output
Output 1:
 3
Output 2:
 1
"""
#Property1 of XOR(^): A^A = 0. XOR of same bits is 0 and XOR of different bits is 1
#Property2: A^0 = A 
#XOR holds associative property; A^B^C = (A^B)^C = (A^C)^B = (B^C)^A
#If A^B = k then A^k = B and B^k = A
#Hint - We can use bitwise XOR operator and when XOR operation perfomed 
    #amoung the numbers occur even number of times, the result will be 0 (as per the property#1)
    #and there is only one number occuring one time, when the result of above(0) XOR with number occuring only one time(or odd number of times) the result will be that number itself (per the property #2) 
             
class Solution:
    # @param A : tuple of integers where every number occurs twice except one number
    # @return an integer, which occurs only one time in the input A
    def singleNumber(self, A):
        #check the hints and properties aboves
        n = len(A)
        if(n > 0):
            ans = A[0]
            for i in range(1, n):
                ans  ^= A[i]
            return ans

s = Solution()

#test case 1
A = [1, 2, 2, 3, 1]
ans = s.singleNumber(A)
print("for input: {A} output is: {ans}".format(A = A, ans = ans))
assert ans == 3

#test case 2
A = [1, 2, 2]
ans = s.singleNumber(A)
print("for input: {A} output is: {ans}".format(A = A, ans = ans))
assert ans == 1

#test case 3
A = [3]
ans = s.singleNumber(A)
print("for input: {A} output is: {ans}".format(A = A, ans = ans))
assert ans == 3

#test case 4
A = []
ans = s.singleNumber(A)
print("for input: {A} output is: {ans}".format(A = A, ans = ans))
        
