class Solution(object):
    def climbStairs(self, n):
        if n<=2:
            return n
        a,b=1,2
        while n>2:
            way = a+b
            a=b
            b=way
            n-=1
        return way
s= Solution()
print(s.climbStairs(n=5))