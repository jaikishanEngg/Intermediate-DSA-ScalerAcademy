# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:29:32 2022

@author: Kishan
Problem Description
You are given an integer T denoting the number of test cases. For each test case, you are given an integer array A.
You have to put the odd and even elements of array A in 2 separate arrays and print the new arrays.
NOTE: Array elements should have the same relative order as in A.

Problem Constraints
1 <= T <= 10
1 <= |A| <= 105
1 <= A[i] <= 109

Input Format
First line of the input contains a single integer T.
For each test case:
First line consists of a single integer |A| denoting the length of array.
Second line consists of |A| space separated integers denoting the elements of array A.

Output Format
For each test case:
First line should contain an array of space separated integers containing all the odd elements of array A
Second line should contain an array of space separated integers containing all the even elements of array A
"""
def splitOddEvenElements(arr):
    n = len(arr)
    odd_arr = []
    even_arr = []
    for i in range(n):
        if(arr[i]&1 == 1):
            #odd number
            odd_arr.append(arr[i])
        else:
            even_arr.append(arr[i])
    return odd_arr, even_arr
            

def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        odd_arr, even_arr = splitOddEvenElements(A)
        for ele in odd_arr:
            print(ele, end= " ")
        print("")
        for ele in even_arr:
            print(ele, end= " ")
        print("")
    return 0

if __name__ == '__main__':
    main()