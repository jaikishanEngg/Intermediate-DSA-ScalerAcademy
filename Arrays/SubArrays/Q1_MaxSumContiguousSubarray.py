#
# Created on Sun Apr 03 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.

Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000

Input Format
The first and the only argument contains an integer array, A.

Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.

Example Input
Input 1:
    A = [1, 2, 3, 4, -10] 
Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
Example Output
Output 1:
    10 
Output 2:
    6 

Example Explanation
Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6. 
'''

from cmath import inf


class Solution:
    def maxSubArray1(self, A):
        n = len(A)
        max_sum = - float('inf')
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += A[j]
                if(s > max_sum):
                    max_sum = s
        
        return max_sum

    def maxSubArray(self, A):
        n = len(A)
        
        #Build prefixsum array
        prefixsumArray = []
        prefixsumArray.append(A[0])
        for i in range(1, n):
            prefixsumArray.append(A[i] + prefixsumArray[i-1])
        
        #Initialize max value from prefixsumArray - this is = max sum formed from the subarray starting with 0th element
        max_element = max(prefixsumArray)

        #now let's iterate the subarrays from 1-index to n-1 index and see if we have any subarray with larger sum than the previous one
        for i in range(1, n):
            for j in range(i, n):
                if (prefixsumArray[j] - prefixsumArray[i-1]) > max_element:
                    max_element = prefixsumArray[j] - prefixsumArray[i-1]
        
        return max_element

s = Solution()

#test case 1: simple 
A = [1, 2, 3, 4, -10]
ans = s.maxSubArray(A)
ans1 = s.maxSubArray1(A)
assert ans == 10
print(ans1)

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
ans = s.maxSubArray(A)
ans1 = s.maxSubArray1(A)
assert ans == 6
print(ans1)



        
        
