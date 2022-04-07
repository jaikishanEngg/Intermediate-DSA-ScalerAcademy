#
# Created on Thu Apr 07 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:
All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.

Problem Constraints
1 <= Number of Function calls <= 107

Input Format
Functions will be called by the checker code automatically.

Output Format
Each function should return the values as defined by the problem statement.

Example Input
Input 1:
    push(1)
    push(2)
    push(-2)
    getMin()
    pop()
    getMin()
    top()
Input 2:
    getMin()
    pop()
    top()

Example Output
Output 1:
    -2 1 2
Output 2:
    -1 -1

Example Explanation
Explanation 1:
    Let the initial stack be : []
    1) push(1) : [1]
    2) push(2) : [1, 2]
    3) push(-2) : [1, 2, -2]
    4) getMin() : Returns -2 as the minimum element in the stack is -2.
    5) pop() : Return -2 as -2 is the topmost element in the stack.
    6) getMin() : Returns 1 as the minimum element in stack is 1.
    7) top() : Return 2 as 2 is the topmost element in the stack.
Explanation 2:
    Let the initial stack be : []
    1) getMin() : Returns -1 as the stack is empty.
    2) pop() :  Returns nothing as the stack is empty.
    3) top() : Returns -1 as the stack is empty.
'''
class MinStack:
    inputStack = [None]*10**7
    stackTop = -1
    minStack = [None]*10**7
    minStackTop = -1

    minValue = None
    # @param x, an integer
    # @return an integer
    def push(self, x):
        MinStack.stackTop += 1
        MinStack.minStackTop += 1

        if MinStack.minValue == None or x <= MinStack.minValue:
            #first element we're inserting
            MinStack.minValue = x
            MinStack.inputStack[MinStack.stackTop] = x
            MinStack.minStack[MinStack.minStackTop] = x
        else:
            MinStack.inputStack[MinStack.stackTop] = x
            MinStack.minStack[MinStack.minStackTop] = MinStack.min_value

    # @return nothing
    def pop(self):
        if(MinStack.minStackTop != -1 and MinStack.stackTop != -1):
            MinStack.stackTop -= 1
            MinStack.minStackTop -= 1
        
    # @return an integer
    def top(self):
        if(MinStack.minStackTop != -1 and MinStack.stackTop != -1):
            return MinStack.inputStack[MinStack.stackTop]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if(MinStack.minStackTop != -1 and MinStack.stackTop != -1):
            return MinStack.minStack[MinStack.minStackTop]
        else:
            return -1