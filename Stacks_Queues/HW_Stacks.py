#
# Created on Fri Apr 08 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#

class Stack:
    def __init__(self, size):
        #define the stack
        self.stack = [None]*size
        self.stackTop = -1
        self.stackSize = size
    
    def push(self, item):
        if(self.stackTop == self.stackSize - 1):
            #overflow
            return
        else:
            self.stackTop += 1
            self.stack[self.stackTop] = item
    
    def pop(self):
        if(self.stackTop == -1):
            #underflow
            return 0
        else:
            x = self.stack[self.stackTop]
            self.stackTop -= 1
            return x

class Solution:
    # @param A : string
	# @return an integer
    def solve(self, A):
        n = len(A)
        stackObj = Stack(n)

        for i in range(n):
            if A[i] == '{' or A[i] == '(' or A[i] == '[':
                #push into the stack
                stackObj.push(A[i])
            else:
                #pop the item
                if A[i] == '}':
                    #check for {
                    if stackObj.pop() != '{':
                        return 0
                elif A[i] == ')':
                    #check for '('
                    if stackObj.pop() != '(':
                        return 0
                elif A[i] == ']':
                    #check for '['
                    if stackObj.pop() != '[':
                        return 0

        if stackObj.stackTop == -1:
            return 1
        else:
            return 0

s = Solution()
A = "{([])}"
s.solve(A)
