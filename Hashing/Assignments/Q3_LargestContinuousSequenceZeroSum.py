# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:28:16 2022

@author: Kishan
Problem Description

Given an array A of N integers.
Find the largest continuous sequence in a array which sums to zero.

Problem Constraints

1 <= N <= 106

-107 <= A[i] <= 107
"""
class Solution:

    def lszero(self, A):
        prefixSumArr = [A[0]]
        n = len(A)
        
        _lszeroSumLength = 0
        _lszeroSumCoord = None #Coordinates of i, j
        
        for i in range(1, n):
            prefixSumArr.append(prefixSumArr[i-1] + A[i])
        
        hashSetPrefixA = set(prefixSumArr) #Unique elements of prefixSumArr
        
        if(n > len(hashSetPrefixA)):
            #when they're duplicates in the prefix sum array, then there is a sub array of sum 0
            i = n - 1
            while i >= 0:
                j = prefixSumArr.index(prefixSumArr[i]) #find the index of the same element from beginning
                if (prefixSumArr[i] == prefixSumArr[j]  and i != j) or prefixSumArr[i] == 0:
                    if _lszeroSumLength < i - j:
                        _lszeroSumLength = i - j
                        if prefixSumArr[i] == 0:
                            if()
                            _lszeroSumCoord = (0, i)
                        else:
                            _lszeroSumCoord = (j + 1, i)
                i -= 1
        
        print("prefix array: ",prefixSumArr)
        print(_lszeroSumLength)
        print(_lszeroSumCoord)
        return A[_lszeroSumCoord[0]: _lszeroSumCoord[1]+1]

s = Solution()
#A = [2,-2,4,-4]

#A = [ 1, 2, -2, 4, -4 ]
A  = [ 1, 2, -3, 3 ]

ans = s.lszero(A)                    
print(ans)
            
            
