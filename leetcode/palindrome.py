class Solution(object):
    
    def isPalindrome(self, x):
        temp = x
        rem =0
        while x > 0:
            num = x%10
            rem =(rem*10) + num
            x = x//10
        if temp == rem:
            return True
        else:
            return False
        
        
s=Solution()
print(s.isPalindrome(121))     