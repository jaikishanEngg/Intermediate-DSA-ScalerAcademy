#
# Created on Thu Apr 07 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a string A consisting only of '(' and ')'.

You need to find whether parentheses in A are balanced or not, if it is balanced then return 1 else return 0.

Problem Constraints
1 <= |A| <= 105

Input Format
First argument is an string A.

Output Format
Return 1 if parantheses in string are balanced else return 0.

Example Input
Input 1:
    A = "(()())"
Input 2:
    A = "(()"

Example Output
Output 1:
    1
Output 2:
    0

Example Explanation
Explanation 1:
    Given string is balanced so we return 1.
Explanation 2:
    Given string is not balanced so we return 0.
'''
class Solution:

    def solve(self, A):
        top = -1
        n = len(A)
        stack = [None]*n    #Initialize the stack with size 'n'

        for i in range(n):
            if(A[i] == '('):
                #Whenever we get open parantheses push it into the stack
                #push '(' open parantheses into the stack
                top += 1
                stack[top] = '('
            elif(A[i] == ')'):
                #Whenever we get closed parantheses pop it from the stack
                #pop ')' closed paranthesis from the stack
                if(top == -1):
                    #Check stack underflow
                    return 0
                else:
                    #else decrement the stack top pointer
                    top -= 1

        if(top == -1):
            #After all the push and pop operations, if the open and closed parantheses are equal 
                # then push and pop operations will sort out and top pointer remains to -1 (initial value)
                #for a Valid prantheses string
            return 1
        else:
            return 0

s = Solution()
#test case 1
A = "(()())"
ans = s.solve(A)
assert ans == 1

A = "(()"
ans = s.solve(A)
assert ans == 0
