# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:23:42 2022

@author: Kishan
Problem Description
Little Ponny is given an array, A, of N integers. In a particular operation, he can set any element of the array equal to -1.
He wants your help for finding out the minimum number of operations required such that the maximum element of the resulting array is B. If it is not possible then return -1.
Input Format
The first argument of input contains an integer array, A.
The second argument of input contains an integer, B.
Output Format
Return an integer representing the answer.

Example Input
Input 1:
 A = [2, 4, 3, 1, 5] B = 3 
Input 2:
 A = [1, 4, 2] B = 3 

Example Output
Output 1: 2 
Output 2: -1 

Example Explanation
Explanation 1: We need to remove 4 and 5 to make 3 the biggest element. 
Explanation 2: As 3 doesn't exist in the array, the answer is -1.
"""
#My approach is we will first see if B is exists in A, if not exists then return -1
#if B exists in A then see how many items are there in A which are >B = return that number
def isElementExists(arr, search_item):
    n = len(arr)
    for i in range(n):
        if(arr[i] == search_item):
            return True
            break
    else:
        return False

def maxElementsThanB(arr, B):
    count = 0
    for e in arr:
        if(e > B):
            count += 1
    return count
    
def solution(arr, element):
    if(isElementExists(arr, element)):
        return maxElementsThanB(arr, element)
    else:
        return -1

#test case 1: Trivial case    
A = [2, 4, 3, 1, 5]
B = 3 
assert solution(A,B) == 2


#test case 2: negative case
A = [1, 4, 2]
B = 3
assert solution(A,B) == -1