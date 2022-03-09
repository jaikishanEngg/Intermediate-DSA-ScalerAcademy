# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:47:50 2022

@author: Kishan
Problem Description

Given an array A and a integer B. A pair(i,j) in the array is a good pair if i!=j and (A[i]+A[j]==B). Check if any good pair exist or not.

Input Format

First argument is an integer array A.

Second argument is an integer B.


Output Format

Return 1 if good pair exist otherwise return 0.

"""

def isGoodPair(arr, x):
    #returns 1 if there is pair with sum = x; else return 0
    #this is a naive brute force approach so time complexity would be O(N**2)
    if(len(arr) < 2):
        #returns 0 when it has <=1 elements in the input array as it will not be possible to make a pair with <= 1 elements
        return 0
    j = len(arr) - 1
    while(j > 0):
        i = j - 1
        while(i >= 0):
            if(arr[i] + arr[j] == x):
                return 1
            i -= 1
        j -= 1
        
    else:
        return 0
            
            
#case1: empty array
ans = isGoodPair([],3)
assert ans == 0

#case2: only 1 item in array
ans = isGoodPair([1],1)
assert ans == 0

#case3: postivie test case
ans = isGoodPair([1,2], 3)
assert ans == 1

#case4:  negative test case
ans = isGoodPair([1,2,3,4], 100)
assert ans == 0
