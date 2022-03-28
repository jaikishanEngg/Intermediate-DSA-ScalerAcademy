# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:51:11 2022

@author: Kishan
Problem Description

You are given a constant array A.

You are required to return another array which is the reversed form of input array.

Input Format

First argument is a constant array A.

Output Format

You have to return an integer array.
"""

def reverseArray(arr):
    #returns the reversed array
    
    n = len(arr) #assuming 1 <= n <= 10000
    
    if(n <= 1):
        return arr
    
    #initializing the front and end pointers
    i = 0
    j = n - 1
    
    while (i < j):
        #start swapping from the edge elements until cross the pointers over the one another.
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
    return arr

#test case1: empty array
ans = reverseArray([])
assert ans == []

#test case2: array with only 1 element
ans = reverseArray([9])
assert ans == [9]

#test case 3: trivial case; odd size 
ans = reverseArray([1,2,3,2,1])
assert ans == [1,2,3,2,1]

#test case 4: trivial case; even size
ans = reverseArray([1,2,3,4])
assert ans == [4,3,2,1]