#
# Created on Mon Apr 18 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a set of distinct integers A, return all possible subsets.

NOTE:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.


Problem Constraints
1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX


Input Format
First and only argument of input contains a single integer array A.



Output Format
Return a vector of vectors denoting the answer.



Example Input
Input 1:

A = [1]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:

[
    []
    [1]
]
Output 2:

[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]


Example Explanation
Explanation 1:

 You can see that these are all possible subsets.
Explanation 2:

You can see that these are all possible subsets.
'''
#Hint: No.of possible subsets are 2**n where n is the number of elements in the input array
    #I'll take a binary representation of numbers from 0 to 2**n 
    # and whenever the bit is set I'll keep adding the corresponding element from A

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def subsets(self, A):
        A = list(set(A)) #remove duplicates if any
        A.sort()    #sort the elements in lexigographic (ascending) order
        n = len(A)
        subsets = [[],] #output list of subsets

        for set_i in range(1, 2**n):    #no.of subsets possible are 2**n
            temp_set = []
            i = 0
            while(set_i):
                if (set_i) & 1:
                    temp_set.append(A[i])
                i += 1
                set_i >>= 1
            subsets.append(temp_set)
        subsets.sort()
        return subsets

s = Solution()
A = [1, 2, 3]
A = [ 15, 20, 12, 19, 4 ]
ans = s.subsets(A)
print(ans)