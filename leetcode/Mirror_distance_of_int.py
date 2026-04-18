class Solution(object):
    def mirrorDistance(self, n):
        r_n = int(str(n)[::-1])
        return abs(n-r_n)
        
s=Solution()
print(s.mirrorDistance(25))