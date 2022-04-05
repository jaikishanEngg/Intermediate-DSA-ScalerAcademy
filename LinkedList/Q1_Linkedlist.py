#
# Created on Tue Apr 05 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Design and implement a Linked List data structure.
A node in a linked list should have the following attributes - an integer value and a pointer to the next node. It should support the following operations:

insert_node(position, value) - To insert the input value at the given position in the linked list.
delete_node(position) - Delete the value at the given position from the linked list.
print_ll() - Print the entire linked list, such that each element is followed by a single space.
Note:

If an input position does not satisfy the constraint, no action is required.
Each print query has to be executed in a new line.


Problem Constraints
1 <= position <= n where, n is the size of the linked-list.

Input Format
First line contains an integer denoting number of cases, let's say t.
Next t line denotes the cases.

Output Format
When there is a case of print_ll(),  Print the entire linked list, such that each element is followed by a single space.
NOTE: You don't need to return anything.

Example Input
5
i 1 23
i 2 24
p
d 1
p

Example Output
23 24
24

Example Explanation
After first two cases linked list contains two elements 23 and 24.
At third case print: 23 24.
At fourth case delete value at first position, only one element left 24.
At fifth case print: 24.
'''
# Definition for singly-linked list.
class ListNode:
    head = None
    def __init__(self, x):
        self.val = x
        self.next = None

def insert_node(position, value):
    if(position == 1):
        ListNode.head = ListNode(value)
    else:
        ptr = ListNode.head
        for i in range(position-2):
            ptr = ptr.next
        newNode = ListNode(value)
        if(ptr):
            newNode.next = ptr.next
            ptr.next = newNode    

def delete_node(position):
    ptr = ListNode.head 
    if(position == 1):
        #removing at beginning
        if(ptr):
            ListNode.head = ptr.next
    
    else:
        #removing element at position p, hold the pointer for position (p-1) 
        for i in range(position-2):
            if(ptr):
                ptr = ptr.next
            else:
                return
        if(ptr):
            if(ptr.next):
                ptr.next = ptr.next.next
            else:
                ptr.next = None


def print_ll():
    # Output each element followed by a space
    ptr = ListNode.head
    if(ptr):
        while(ptr.next != None):
            print(ptr.val, end= " ")
            ptr = ptr.next
        print(ptr.val)
