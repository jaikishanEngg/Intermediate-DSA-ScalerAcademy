#
# Created on Tue Apr 12 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given the root of a tree A with each node having a certain value, find the count of nodes with more value than all its ancestor.

Problem Constraints
1 <= Number of Nodes <= 200000
1 <= Value of Nodes <= 2000000000

Input Format
The first and only argument of input is a tree node.

Output Format
Return a single integer denoting the count of nodes that have more value than all of its ancestors.

Example Input
Input 1:

     3

Input 2:

    4
   / \
  5   2
     / \
    3   6

Example Output
Output 1:
    1 
Output 2:
    3

Example Explanation
Explanation 1:
    There's only one node in the tree that is the valid node.
Explanation 2:
    The valid nodes are 4, 5 and 6.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.ans = 0

    def dfs(self, root,maxsofar):
        if root == None:
            return 0
        if(root.val > maxsofar):
            self.ans += 1
            maxsofar = root.val

        self.dfs(root.left, maxsofar)
        self.dfs(root.right, maxsofar)

        return self.ans

    def solve(self, A):
        return self.dfs(A, 0)