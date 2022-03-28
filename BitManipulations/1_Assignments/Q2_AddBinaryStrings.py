# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 12:54:52 2022

@author: Kishan
Problem Description
Given two binary strings, return their sum (also a binary string).

Example:
a = "100"
b = "11"

Return a + b = "111".
"""
class Solution:
	# @param A : string representing a binary number
	# @param B : string representing a binary number
	# @return a string which is binary addition of A + B
    def addBinary(self, A, B):
        #returns a string, addition of two binary numbers. i.e., A+B 
        _sum = 0    #holds the sum of the bits of (A[i] + B[i])%2 and mod 2 as it is a binary number
        _carry = 0  #holds the carry. i.e., integer division(with 2 as base is 2) of the sum of bits (A[i] + B[i])//2 
        len_a = len(A)
        len_b = len(B)
        
        #balance the number of digits; i.e., prefix the less number of digits with 0s
        if(len_a > len_b):
            B = "0"*(len_a-len_b) + B
            len_b = len_a
        elif(len_b > len_a):
            A = "0"*(len_b-len_a) + A
            len_a = len_b
        
        result = '' #result of A+B
        
        #As A and B are strings; we have to convert it into the numeric to perform the arithemetic op.,
        A = list(map(int,A))
        B = list(map(int,B))
        
        i = len_a-1     #or i = len_b -1 also works as len_a and len_b are equal at this point
        while(i >= 0):
            #iterate through each bit from units place to Most significant bit and add A[i], B[i]
            _sum = (_carry + A[i] + B[i])
            _carry = (_sum//2)
            _sum = _sum%2
            result = str(_sum) + result
            i -= 1

        #Check overflow condition            
        if(_carry == 1):            
            #if we get a carry then we will prefix the Most significant bit with a '1'
            result = '1' + result
        
        return result

s = Solution()

#test case 1 - overflow case
a = "111"
b = "111"            
ans = s.addBinary(a,b)
assert ans == "1110"

#test case 2 - adding with a 0
a = "0"
b = "11"
ans = s.addBinary(a,b)
assert ans == "11"

#test case 3 - different lengths
a = "010"
b = "1111"
ans = s.addBinary(a,b)
assert ans == "10001"
