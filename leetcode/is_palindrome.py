class Solution(object):
    def isPalindrome(self, s):
        s = "".join([char.lower() for char in s if char.isalnum()])
        temp = []
        for i in range(-1, -len(s) - 1, -1):
            temp.append(s[i])
        return "".join(temp) == s
        
s= Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))