class Solution:

    def pow(self, A, B, C):
        if B == 0:
            return 1%C
        half_power = self.pow(A, B//2, C)
        if(B%2 == 0):
            return (half_power%C * half_power%C)%C
        else:
            return (half_power%C * half_power%C * A%C)%C
        

s = Solution()
ans = s.pow(10**9,10**9,3)
print(ans)