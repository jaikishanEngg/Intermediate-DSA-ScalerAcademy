#
# Created on Mon Apr 18 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a Binary Tree A containing N nodes, you need to find the path from Root to a given node B.

NOTE:

No two nodes in the tree have the same data values.
You can assume that B is present in tree A and a path always exists.


Problem Constraints
1 <= N <= 105

1 <= Data Values of Each Node <= N

1 <= B <= N



Input Format
First Argument represents pointer to the root of binary tree A.

Second Argument is an integer B denoting the node number.



Output Format
Return an one-dimensional array denoting the path from Root to the node B in order.



Example Input
Input 1:

 A =     
           1
         /   \
        2     3
       / \   / \
      4   5 6   7 

 B = 5
Input 2:

 A = 
            1
          /   \
         2     3
        / \ .   \
       4   5 .   6

 B = 1   


Example Output
Output 1:

 [1, 2, 5]
Output 2:

 [1]


Example Explanation
Explanation 1:

 We need to find the path from root node to node with data value 5.
 So the path is 1 -> 2 -> 5 so we will return [1, 2, 5]
Explanation 2:

 We need to find the path from root node to node with data value 1.
 As node with data value 1 is the root so there is only one node in the path.
 So we will return [1]
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def __init__(self):
        self.path = []
        self.flag = False

    def solve(self, A, B):
        if A == None:
            return

        if A.val == B:
            self.flag = True
            self.path.append(A.val)
            return True

        if self.solve(A.left, B) or self.solve(A.right, B):
            self.path.append(A.val)
        
        return self.path[::-1]
