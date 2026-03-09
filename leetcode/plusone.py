class Solution(object):
    def plusOne(self, digits):
        digits = [str(x) for x in digits]
        addition = str(int(''.join(digits)) +1)
        addition = [int(x) for x in addition]
        return addition
        

s_obj = Solution()
print(s_obj.plusOne([4,3,2,1])) 
