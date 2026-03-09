class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
            
        i=1
        while i*i <=x:
            i+=1
        return i-1

s= Solution()
print(s.mySqrt(x=9))
            
            
            
        