# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:21:11 2022

@author: Kishan

You are given an integer array A and an integer B. You have to print the same array after rotating it B times towards right.

NOTE: You can use extra memory.
Input Format

First line begins with an integer |A| denoting the length of array, and then |A| integers denote the array elements.
Second line contains a single integer B


Output Format

Print an array of integers which is the Bth right rotation of input array A, on a separate line.
"""

def reverse(arr,i = 0, j = 0):
    #returns the reverse of the given array from index i to j
    while(i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

def rotate(arr, k):
    #returns an array by rotating the element clockwise by k times
    n = len(arr)
    k = k%n
    if(k == 0 or n<= 1):
        #return the original array, if either 0 rotations or only 1 or less elements in input array
        return arr
    else:
        return reverse(reverse(reverse(arr, 0, n-1), 0, k-1), k, n-1)
    
#case1: if array is empty
ans = reverse([], 2)
assert ans == []
#case2: if array is only 1 element
ans = rotate([1],4)
assert ans == [1]
#case3: a trivial case
ans = rotate([1,2,3,4,5],3)
assert ans == [3,4,5,1,2]