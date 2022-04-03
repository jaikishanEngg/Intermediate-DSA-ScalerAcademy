#
# Created on Tue Mar 29 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description

You are given an array of N integers, A1, A2 ,…, AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE: if B > N, return an empty array.

Input Format
First argument is an integer array A
Second argument is an integer B.

Output Format
Return an integer array.

Example Input
Input 1:
 A = [1, 2, 1, 3, 4, 3]
 B = 3
Input 2:
 A = [1, 1, 2, 2]
 B = 1

Example Output
Output 1:
 [2, 3, 3, 2]
Output 2:
 [1, 1, 1, 1]

Example Explanation
Explanation 1:
 A=[1, 2, 1, 3, 4, 3] and B = 3
 All windows of size B are
 [1, 2, 1]
 [2, 1, 3]
 [1, 3, 4]
 [3, 4, 3]
 So, we return an array [2, 3, 3, 2].

Explanation 2:
 Window size is 1, so the output array is [1, 1, 1, 1].
 '''

class Solution:

    def dNums(self, A, B):
        n = len(A)
        freqHashmap = dict()
        ans = [] #distinct number of element in each sliding window

        #Build first sliding window hashmap of size B
        for i in range(B):
            if(A[i] in freqHashmap):
                freqHashmap[A[i]] += 1
            else:
                freqHashmap[A[i]] = 1
        
        ans.append(len(freqHashmap.keys()))

        #sliding window approach
        i = 1
        while(i <= n-B):
            tobe_removed = A[i-1]
            tobe_added = A[i+B-1]

            #print("tobe_added: ", tobe_added)
            #print("tobe_removed: ",tobe_removed)

            freqHashmap[tobe_removed] -= 1  #remove the previous slide's element
            if(tobe_added in freqHashmap):
                freqHashmap[tobe_added] += 1
            else:
                freqHashmap[tobe_added] = 1
            
            #if the frequency of removed element is 0, then it doesn't make sense keep it in the frequencyHashmap
            if(freqHashmap[tobe_removed] == 0):
                freqHashmap.pop(tobe_removed)
            
            #print("Hashmap: ",freqHashmap)
            ans.append(len(freqHashmap.keys()))

            i += 1
        return ans

s = Solution()
A = [1, 2, 1, 3, 4, 3]
B = 3
ans = s.dNums(A,B)
assert ans == [2, 3, 3, 2]

A = [1, 1, 2, 2]
B = 1
ans = s.dNums(A,B)
assert ans == [1, 1, 1, 1]