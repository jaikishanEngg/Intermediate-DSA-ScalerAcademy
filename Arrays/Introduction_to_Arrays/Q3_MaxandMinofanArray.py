# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:39:34 2022

@author: Kishan
Problem Description

Write a program to print maximum and minimum elements of the input array A of size N where you have to take integer N and further N elements as input from user.

Input Format

A single line representing N followed by N integers of the array A



Output Format

A single line containing two space separated integers representing maximum and minimum elements of the input array.
"""
import sys

def getMinMaxfromArray(arr):
    #assuming 1 <= len(arr) <= 1000
    n = len(arr)
    if(n == 0):
        raise TypeError("Invalid Input.  Input array must contain at least 1 element")
    #initialize min max variables with first element
    _min = _max = arr[0]
    
    if(n == 1):
        return _min, _max
    
    for i in range(1,n):
        if(arr[i] < _min):
            _min = arr[i]
        if(arr[i] > _max):
            _max = arr[i]
    return _min, _max

#test case1: empty array 
try:
    _min, _max = getMinMaxfromArray([])
except:
    assert str(sys.exc_info()[1]) == "Invalid Input.  Input array must contain at least 1 element"

#test case2: trivial case with negative and positive elements
_min, _max = getMinMaxfromArray([-1,-2,3,4,-5])
assert _min, _max == (-5,4)

#test case3: trivial case with all negative elements
_min, _max = getMinMaxfromArray([-1,-2,-3,-4,-5])
assert _min, _max == (-5,-1)

#test case4: trivial case with all positive elements
_min, _max = getMinMaxfromArray([1,2,3,4,5])
assert _min, _max == (1,5)
