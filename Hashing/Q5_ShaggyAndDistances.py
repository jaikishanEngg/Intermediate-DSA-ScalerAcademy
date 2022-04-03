'''
Problem Description:
Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.
Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.

Problem Constraints
1 <= |A| <= 105

Input Format
The first and only argument is an integer array A.

Output Format
Return one integer corresponding to the minimum possible distance between a special pair.

Example Input
Input 1:
A = [7, 1, 3, 4, 1, 7]

Input 2:
A = [1, 1]

Example Output
Output 1:
3
Output 2:
1

Example Explanation
Explanation 1:
Here we have 2 options:
1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
Therefore the minimum possible distance is 3. 

Explanation 2:
Only possibility is choosing A[1] and A[2].
'''
class Solution:

    def solve(self, A):
        frequencyHashMap_A = dict() #hashMap<element(int), frequency(int)>
        indicesHashMap_A = dict() #hashMap<element(int), elementOccuredIndices(list)>
        n = len(A)

        for i in range(n):
            if A[i] in frequencyHashMap_A:
                frequencyHashMap_A[A[i]] += 1
                indicesHashMap_A[A[i]].append(i)
            else:
                frequencyHashMap_A[A[i]] = 1
                indicesHashMap_A[A[i]] = [i,]
        
        min_distance = None

        for k,v in indicesHashMap_A.items():
            if(len(v) > 1):
                i = v[0]
                j = v[1]
                if(min_distance):
                    min_distance = min(min_distance, j-i)
                else:
                    min_distance = j - i
        
        #print(frequencyHashMap_A)
        #print(indicesHashMap_A)    
        #print(min_distance)
       
        if(min_distance):
            return min_distance
        else:
            return -1
        


s = Solution()
#test case 1
A = [7, 1, 3, 4, 1, 7]
ans = s.solve(A)
assert ans == 3

#test case 2
A = [1,1]
ans = s.solve(A)
assert ans == 1

#test case 3
A = [1,2,3,4]
ans = s.solve(A)
assert ans == -1

