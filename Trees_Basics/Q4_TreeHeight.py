#
# Created on Tue Apr 12 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given the root node of a binary tree A. You have to find the height of the given tree.

A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.

Problem Constraints
1 <= Number of nodes in the tree <= 105
0 <= Value of each node <= 109

Input Format
The first and only argument is a tree node A.

Output Format
Return an integer denoting the height of the tree.

Example Input
Input 1:

 Values =  1 
          / \     
         4   3                        

Input 2:

 Values =  1      
          / \     
         4   3                       
        /         
       2                                     

Example Output
Output 1:
    2 
Output 2:
    3 

Example Explanation
Explanation 1:
 Distance of node having value 1 from root node = 1
 Distance of node having value 4 from root node = 2 (max)
 Distance of node having value 3 from root node = 2 (max)

Explanation 2:
 Distance of node having value 1 from root node = 1
 Distance of node having value 4 from root node = 2
 Distance of node having value 3 from root node = 2
 Distance of node having value 2 from root node = 3 (max)
'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import sys
#To determine the height of a binary tree we have two approaches
# i. we can define either using edge count
# ii. or we can define using node counts
 
class Solution:
    def __init__(self):
        sys.setrecursionlimit(10**5 + 4)

    def height_usingNodeCount_postOrder(self, root):
        if root == None:
            return 0
        lst_height = self.height_usingNodeCount_postOrder(root.left)
        rst_height = self.height_usingNodeCount_postOrder(root.right)
        return max(lst_height,rst_height) + 1
    
    def height_usingEdgeCount_postOrder(self, root):
        if root == None:
            return -1
        lst_height = self.height_usingEdgeCount_postOrder(root.left)
        rst_height = self.height_usingEdgeCount_postOrder(root.right)
        return max(lst_height,rst_height) + 1
    
    def solve(self, A):
        return self.height_usingNodeCount_postOrder(A)
        #return self.height_usingEdgeCount_postOrder(A)
