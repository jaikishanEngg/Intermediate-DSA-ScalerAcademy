#
# Created on Wed Mar 26 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
"""
Problem Description

Given an array A of N integers.
Find the largest continuous sequence in a array which sums to zero.

Problem Constraints

1 <= N <= 106

-107 <= A[i] <= 107
"""
class Solution:

    def lszero(self, A):
        n = len(A)

        #Build prefixSum Array
        prefixSumArr = [A[0]]
        for i in range(1, n):
            prefixSumArr.append(prefixSumArr[i-1] + A[i])
                
        #result
        longest_sequence_distance = 0
        longest_sequence_i_j = None
        
        #Build hashmap <element of prefixSumEle, firstOccuranceIndex>
        hashmapPrefixA = dict()
        hashmapPrefixA[0] = -1 #logically the prefixsum is zero before starting the array. 
                                #it would be easy when we see another 0 in the prefix Sum array; we can directly fetch the distance

        for r in range(n):
            if prefixSumArr[r] in hashmapPrefixA:
                l = hashmapPrefixA[prefixSumArr[r]]
                curr_distance = r - l
                if(curr_distance > longest_sequence_distance):
                    longest_sequence_distance = curr_distance
                    longest_sequence_i_j = (l + 1, r)
            else:
                hashmapPrefixA[prefixSumArr[r]] = r
        
        if longest_sequence_distance:
            i = longest_sequence_i_j[0]
            j = longest_sequence_i_j[1]
            return A[i:j+1] #list slicing
        else:
            return [] #return blank when there is no sub seq., with sum 0

s = Solution()
#test case 1
A = [2,-2,4,-4]
ans = s.lszero(A)                    
assert ans == [2,-2,4,-4]

#test case 2: negative test case: where there is no subsequence array of sum zero
A = [1,2,3,4]
ans = s.lszero(A)
assert ans == []

#test case 3:
A = [ 1, 2, -2, 4, -4 ]
ans = s.lszero(A)
assert ans == [2,-2,4,-4]

#test case 4:
A  = [ 1, 2, -3, 3 ]
ans = s.lszero(A)
assert ans == [1, 2, -3]

A = [2, 2, 1, -3, 4, 3, 1, -8, 6, -2, -1]
ans = s.lszero(A)                    
assert ans == [-3, 4, 3, 1, -8, 6, -2, -1]
            
            
