class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0: return False
        temp=n
        i=0
        while n % 2 == 0 :
            n=n//2
            i+=1
        check = pow(2,i)
        if check == temp:
             return True
        else:
            return False

s= Solution()
print(s.isPowerOfTwo(3))