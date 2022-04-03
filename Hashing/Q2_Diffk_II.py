#
# Created on Wed Mar 30 2022
#
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
Example :
Input :
A : [1 5 3]
k : 2

Output :
1
as 3 - 1 = 2
Return 0 / 1 for this problem.
'''
class Solution:
    def diffPossible(self, A, B):
        #A is an integer array -- input
        #B is a desired sum to be obtained which equals to A[i] - A[j]
        n = len(A)
        
        #Build a hashmap
        freqHashmap = dict()
        for i in range(n):
            if A[i] in freqHashmap:
                freqHashmap[A[i]] += 1
            else:
                freqHashmap[A[i]] = 1

        for i in range(n):
            #we know A[i]
            #B  = A[i] - A[j];  A[j] = A[i] - B. So we will find if A[j] is it present in our hashmap.
            #Also, if both A[j] and A[i] are same then their indexes must be different (i & j).
                #So, in that case - we will check if frequency > 1 then we will pass
            if(A[i] - B == A[i]):
                if(A[i] - B) in freqHashmap and freqHashmap[A[i]] > 1:
                    return 1
                else:
                    return 0
            else:
                if(A[i] - B) in freqHashmap:
                    return 1
        else:
            return 0

s = Solution()
A = [1, 5, 3]
k = 2
ans = s.diffPossible(A, k)
print(ans)

A = [0]
k = 0
ans = s.diffPossible(A, k)
print(ans)

