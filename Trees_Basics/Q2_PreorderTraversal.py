#
# Created on Tue Apr 12 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a binary tree, return the preorder traversal of its nodes' values.

NOTE: Using recursion is not allowed.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return an integer array denoting the preorder traversal of the given binary tree.

Example Input
Input 1:

   1
    \
     2
    /
   3
Input 2:

   1
  / \
 6   2
    /
   3

Example Output
Output 1:
    [1, 2, 3]
Output 2:
    [1, 6, 2, 3]

Example Explanation
Explanation 1:
    The Preoder Traversal of the given tree is [1, 2, 3].
Explanation 2:
    The Preoder Traversal of the given tree is [1, 6, 2, 3].
'''
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def __init__(self):
        self.preorder = []

    def preorderTraversal(self, A):
        if A == None:
            return 
        self.preorder.append(A.val)
        self.preorderTraversal(A.left)
        self.preorderTraversal(A.right)
        return self.preorder
        