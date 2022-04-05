#
# Created on Tue Apr 05 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def solve(self, A):
        head = None
        n = len(A)
        #print(A)
        for i in range(n):
            if A[i][0] == 0:
                #insert at beginning: just need to add the new element and point it as header
                item = A[i][1]
                new_node = ListNode(item)
                new_node.next = head
                head = new_node

                #print("Insert at beginning!")
                #self.printList(head)

            elif A[i][0] == 1:
                #insert at the end or appending; check if there any existing element in the list 
                # if not then its the first element to be added
                item = A[i][1]
                ptr = head
                new_node = ListNode(item)
                
                if(ptr == None):
                    #first element inserting
                    new_node.next = head
                    head = new_node
                else:
                    while(ptr.next != None):
                        ptr = ptr.next
                    
                    ptr.next = new_node
                
                #print("Insert at end!")
                #self.printList(head)

            elif A[i][0] == 2:
                #insert before index i
                item = A[i][1]
                index = A[i][2]
                
                new_node = ListNode(item)
                
                #if we want to insert before index 0 means that's the head node
                if index == 0:
                    #inserting element at beginning
                    new_node.next = head
                    head = new_node
                #else, iterate the list till index (i-1) and hold the pointer, 
                # so that we can add new item at ith index and link i-1 node to ith node
                # Note: its 0 indexed.
                #Eg: If I have to insert at index 2, I'll hold the pointer at index 1 and now newnode.next = index1.next and index1.next = newnode

                else:
                    ptr = head
                    for curr_index in range(index-1):
                        if(ptr):
                            ptr = ptr.next
                    if(ptr):
                        new_node.next = ptr.next
                        ptr.next = new_node
                    else:
                        #this is the case for if I have to insert item before index 1, its nothing but adding the head node
                        head = new_node
                
                #print("Insert before index: ",index)
                #self.printList(head)


            else: #if A[i][0] == 3
                index = A[i][1]
                #delete the node at index; if its a starting node (0 index) then head needs to be updated
                #others we can handle
                ptr = head
                if(ptr):
                    if(index == 0):
                        #remove at first place
                        if(ptr.next):
                            head = ptr.next
                        else:
                            head = None
                    else:
                        for curr_index in range(index-1):
                            if(ptr):
                                ptr = ptr.next
                        if(ptr.next):
                            ptr.next = ptr.next.next
                        else:
                            ptr.next = None
                
                #print("After deleting at index: ",index)
                #self.printList(head)
        
        #print("End")
        self.printList(head)
    def printList(self, head):
        ptr = head
        if(ptr):
            while ptr.next != None:
                print(ptr.val, end = " -> ")
                ptr = ptr.next
            print(ptr.val, end = " ")

                


#A = [ [1, 13, -1],  [3, 0, -1],  [3, 1, -1],  [2, 15, 0],  [3, 0, -1],  [1, 12, -1],  [3, 0, -1],  [1, 19, -1],  [1, 13, -1],  [3, 0, -1], [0, 12, -1],  [1, 13, -1],  [3, 2, -1]]
#A = [  [2, 6, 0],  [1, 17, -1],  [1, 19, -1],  [2, 16, 1],  [1, 13, -1],  [3, 3, -1],  [1, 19, -1]]
#A = [  [0, 11, -1],  [0, 1, -1],  [0, 4, -1],  [3, 1, -1],  [0, 11, -1],  [3, 0, -1],  [3, 0, -1],  [1, 4, -1]]
#A = [  [1, 13, -1],  [3, 0, -1],  [3, 1, -1],  [2, 15, 0],  [3, 0, -1],  [1, 12, -1],  [3, 0, -1],  [1, 19, -1],  [1, 13, -1],  [3, 0, -1],  [0, 12, -1],  [1, 13, -1], [3, 2, -1]]
A = [  [2, 18, 0],  [2, 5, 1],  [2, 8, 0],  [1, 7, -1],  [1, 5, -1]]
s = Solution()
s.solve(A)
