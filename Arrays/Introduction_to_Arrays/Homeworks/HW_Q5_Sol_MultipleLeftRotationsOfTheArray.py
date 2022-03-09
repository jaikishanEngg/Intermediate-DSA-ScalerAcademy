# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:49:28 2022

@author: Kishan
"""
#Lists are passed to methods as pass-by-reference
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def reverse(self, arr,i = 0, j = 0):
    #this functions rotates the given array
        while(i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

    def leftRotate(self, arr, k):
        #rotate the array clockwise k times
        n = len(arr)
        k = k%n
        if(k == 0):
            return arr
        return self.reverse(self.reverse(self.reverse(arr, 0, n-1), 0, n-1-k), n-1-k+1, n-1)
    
    def solve(self, A, B):
        res = []
        for n in B:
            #print(self.leftRotate(A[:], n))
            res.append(self.leftRotate(A[:], n))
        return res

s = Solution()
A = [1, 2, 3, 4, 5]
B = [2, 3]
ans = s.solve(A, B)
assert ans == [[3, 4, 5, 1, 2], [4, 5, 1, 2, 3]]

A = [1, 2, 3, 4, 5]
B = [3, 2]
ans = s.solve(A, B)
assert ans == [[4, 5, 1, 2, 3], [3, 4, 5, 1, 2]]
        
            
        
