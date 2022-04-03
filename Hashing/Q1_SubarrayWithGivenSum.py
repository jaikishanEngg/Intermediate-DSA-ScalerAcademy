#
# Created on Wed Mar 30 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:
 A = [5, 10, 20, 100, 105]
 B = 110

Example Output
Output 1:
 [2, 3]
Output 2:
 -1
 '''
from sys import prefix


class Solution:
    def solve(self, A, B):
        #A is an interger array
        #B is the sum 
        n = len(A)
        prefixSum = list()
        prefixSumHashmap = dict()

        #Build prefixSum array
        prefixSum.append(A[0])
        for i in range(1, n):
            prefixSum.append(prefixSum[i-1] + A[i])
        
        #Build prefixSum hashmap<prefixsumElement, indexTillWhereItsSum>
        for i in range(n):
            if(prefixSum[i] in prefixSumHashmap):
                prefixSumHashmap[prefixSum[i]].append(i)
                pass
            else:
                prefixSumHashmap[prefixSum[i]] = [i,]
        
        print(A)
        print(prefixSum)
        print(prefixSumHashmap)

        if(B in prefixSumHashmap):
            index = min(prefixSumHashmap[B])
            return A[0:index+1]

        else:
            for i in range(n):
                a = prefixSum[i]
                b = a - B
                # we need to find b
                if b in prefixSumHashmap:
                    index = min(prefixSumHashmap[b])
                    if(index < i):
                        return A[index+1:i+1]
            else:
                return [-1,]


s = Solution()
A = [1, 2, 3, 4, 5]
B = 5
ans = s.solve(A,B)
print("ans: ", ans)
A = [5, 10, 20, 100, 105]
B = 110
ans = s.solve(A,B)
print("ans: ", ans)

