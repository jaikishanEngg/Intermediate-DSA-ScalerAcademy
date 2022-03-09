# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:02:23 2022

@author: Kishan
Problem Description

You are given an integer T (Number of test cases). For each test case, you are given array A and an integer B. You have to tell whether B is present in array A or not.
Input Format

First line of the input contains a single integer T.
Next, each of the test case consists of 2 lines:
First line begins with an integer |A| denoting the length of array, and then |A| integers denote the array elements.
Second line contains a single integer B

Output Format

For each test case, print on a separate line 1 if the element exists, else print 0.
"""
def isElementExists():
    t = int(input())    #input number of test cases
    result_array = []
    
    #read_input
    for i in range(t):
        #iterate through each test case
        
        input_array = list(map(int, input().split()))   #read input array
        search_item = int(input())  #read search item
        
        for i in range(len(input_array)):
            #if the search item found in the array then add '1' to the results array
            if(input_array[i] == search_item):
                result_array.append(1)
                break
        else:
            #if the search item found in the array then add '0' to the results array
            result_array.append(0)
            
    for res in result_array:
        print(res)

#test case1: 
isElementExists()