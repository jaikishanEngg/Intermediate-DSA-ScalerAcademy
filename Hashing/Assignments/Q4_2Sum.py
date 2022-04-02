#
# Created on Fri Apr 01 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description

Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
'''

class Solution:

    def twoSum(self, A, B):
        #A is the integer list: input
        #B is the target sum where B = A[i] + A[j] and i < j
        n = len(A)

        #Lets maintain a hashmap of indices where each element of A present in the array
        hashmapIndices = dict()
        for i in range(n):
            if(A[i] in hashmapIndices):
                hashmapIndices[A[i]].append(i)
            else:
                hashmapIndices[A[i]] = [i,]
        
        print(hashmapIndices)
        ans = []

        for i in range(n):
            # B = A[i] + A[j]
            # When A[i] is the current ele we're scanning through, we need to find A[j]
            # So,sub to A[j] = B - A[i] and also i < j
            x = B - A[i] # x is A[j]
            
            #print("A[i] = ", A[i])
            #print("B = ", B)
            #print("X: ", x)

            if x in hashmapIndices:
                if x == A[i] and len(hashmapIndices[x]) > 1:
                    j = hashmapIndices[x][1]
                    ans.append([i+1, j+1])
                else:
                    j = min(hashmapIndices[x])

                if i < j:
                    #print("i ",i, "j ", j)
                    ans.append([i+1, j+1])
        
        ans.sort(key = lambda a:a[1])
        
        if(ans):
            return ans[0]
        else:
            return []

s = Solution()
A = [2, 7, 11, 15]
target = 9

A  = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
target = -3
A = [ 1, 1, 1 ]
target = 2
A = [ -10, -10, -10 ]
target = -5
ans = s.twoSum(A, target)
print(ans)
