#
# Created on Tue Apr 05 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, arr):
        n = len(arr)
        prefixSumArr = [arr[0]]
        for i in range(1,n):
            prefixSumArr.append(arr[i] + prefixSumArr[i-1])
        
        _sumOfAllSubArrays = 0
        
        for i in range(n):
            for j in range(i,n):
                if(i == 0):
                    _sumOfAllSubArrays += prefixSumArr[j]
                else:
                    _sumOfAllSubArrays += (prefixSumArr[j] - prefixSumArr[i - 1])
        
        return _sumOfAllSubArrays