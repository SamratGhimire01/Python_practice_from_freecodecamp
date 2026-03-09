class Solution(object):
    def singleNumber(self, nums):
        res =0 
        for i in nums:
            res^=i
        return res
            
s=Solution()
print(s.singleNumber([4,1,2,1,2,2,5,6,6,5,7,7]))