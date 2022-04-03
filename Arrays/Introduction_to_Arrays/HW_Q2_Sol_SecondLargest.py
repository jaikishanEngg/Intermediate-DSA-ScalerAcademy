# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:30:22 2022

@author: Kishan
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #returns the second largest element from the array
        
        #Store the first max element from A
        max_1 = max(A)

        #if we have only 1 element in the array then it is the first max element.  There cannot be second max element
        if(len(A) == 1):
            return -1
        else:
            #If there are 2 element in the array like [25,25] then max1 will 25 and max2 will be 25; as there are two elements
            max_2 = min(A)

            for i in range(len(A)):
                if(A[i] < max_1 and A[i] > max_2):
                    max_2 = A[i]
            
            return max_2

s = Solution()

#test case1
A = [54]
ans = s.solve(A)        
assert ans == -1 

#test case 2
A = [54,54]
ans = s.solve(A)
assert ans == 54

#test case 3
A = [52,51]
ans = s.solve(A)
assert ans == 51

#test case 4
A = [-1, -2, -3]
ans = s.solve(A)
assert ans == -2