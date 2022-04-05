#
# Created on Tue Apr 05 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#

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
