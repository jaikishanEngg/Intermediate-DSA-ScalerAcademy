#
# Created on Tue Apr 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that 
removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.

Problem Constraints
1 <= n <= 105
-105 <= A[i] <= 105

Input Format
First argument contains an array A of integers of size N

Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.

Example Input
Input 1:
    A=[2, 1, 6, 4]

Input 2:
    A=[1, 1, 1]

Example Output
Output 1:
    1
Output 2:
    3

Example Explanation
Explanation 1:
    Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
    Therefore, the required output is 1. 

Explanation 2:
    Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
    Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
    Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
    Therefore, the required output is 3.
'''

class Solution:
    # @param A : list of integers
    # @return an intege
    def computeEvenOddPrefixArray(self, arr):
        n = len(arr) #Assuming n >= 1
        
        _evenPreArr = [0,]
        _oddPreArr = [arr[0],]
        
        if( n > 0):
            for i in range(1, n):
                j = i + 1
                if(j & 1 == 1):
                    #odd index
                    _oddPreArr.append(arr[i] + _oddPreArr[i-1])
                    _evenPreArr.append(_evenPreArr[i-1])
                else:
                    #even index
                    _evenPreArr.append(arr[i] + _evenPreArr[i-1])
                    _oddPreArr.append(_oddPreArr[i-1])
        
        _evenPreArr.append(_evenPreArr[-1])
        _oddPreArr.append(_oddPreArr[-1])
    
        #print("Even Prefix Array: ",_evenPreArr)
        #print("Odd Prefix Array: ", _oddPreArr)
    
        return _evenPreArr, _oddPreArr
    
    def computeEvenOddSumMatchingCounts(self, arr):
        _evenPreArr , _oddPreArr = self.computeEvenOddPrefixArray(arr)
        n = len(arr)
        count_ans = 0 
        
        for i in range(len(arr)):
            j = i + 1
            #print("Array: ",arr)
            if(j&1 == 1):
                #odd index number
                #print("i: ", i, "j: ",j)
                oddSum = (_oddPreArr[i] - arr[i]) + (_evenPreArr[n] - _evenPreArr[i])
                evenSum = _evenPreArr[i] + (_oddPreArr[n] - _oddPreArr[i])
                #print("Odd sum: ", oddSum, "Even sum: ",evenSum)
            else:
                #even index number
                #print("i: ", i, "j: ",j)
                evenSum = (_evenPreArr[i] - arr[i]) + (_oddPreArr[n] - _oddPreArr[i])
                oddSum = _oddPreArr[i] + (_evenPreArr[n] - _evenPreArr[i])
                #print("Odd sum: ", oddSum, "Even sum: ",evenSum)
            
            if(oddSum == evenSum):
                count_ans += 1
                
        return count_ans

    
    def solve(self,arr):
        return self.computeEvenOddSumMatchingCounts(arr)

s = Solution()
A = [2, 1, 6, 4]
ans =  s.solve(A)
assert ans == 1

A = [1, 1, 1]
ans = s.solve(A)
assert ans == 3

