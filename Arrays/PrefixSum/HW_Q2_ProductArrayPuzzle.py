#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.
Note: It is always possible to form the product array with integer (32 bit) values.

Input Format
    The only argument given is the integer array A.
Output Format
    Return the product array.

Constraints
    1 <= length of the array <= 1000
    1 <= A[i] <= 10

For Example
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    [120, 60, 40, 30, 24]

Input 2:
    A = [5, 1, 10, 1]
Output 2:
    [10, 50, 5, 50]
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def productPrefixArray(self, arr):
        n = len(arr)
        productPrefixArr = [arr[0],]
        
        for i in range(1, n):
            productPrefixArr.append(productPrefixArr[i-1] * arr[i])
        
        return productPrefixArr
    
    def solve(self, arr):
        n = len(arr)
        _result = []
        
        #compute the product of all the elments of the array
        productOfElements = 1
        for i in range(n):
            productOfElements *= arr[i]
        
        #create the result array where the ith element = (productOfElements) divided by the ith element of the original array.
        for i in range(n):
            _result.append(productOfElements//arr[i])
        
        return _result

s = Solution()
A = [1, 2, 3, 4, 5]
ans = s.solve(A)
assert ans == [120, 60, 40, 30, 24]

A = [5, 1, 10, 1]
ans = s.solve(A)
assert ans == [10, 50, 5, 50]
