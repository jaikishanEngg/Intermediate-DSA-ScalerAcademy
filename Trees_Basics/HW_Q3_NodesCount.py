#
# Created on Tue Apr 12 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given the root node of a binary tree A. You have to find the number of nodes in this tree.

Problem Constraints
1 <= Number of nodes in the tree <= 105
0 <= Value of each node <= 107

Input Format
    The first and only argument is a tree node A.

Output Format
    Return an integer denoting the number of nodes of the tree.

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
    3 
Output 2:
    4 

Example Explanation
Explanation 1:
    Clearly, there are 3 nodes 1, 4 and 3.
Explanation 2:
    Clearly, there are 4 nodes 1, 4, 3 and 2.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

class Solution:
    def __init__(self):
        sys.setrecursionlimit(10**5 + 4)
        
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if A == None:
            return 0
        return self.solve(A.left) + self.solve(A.right) + 1
