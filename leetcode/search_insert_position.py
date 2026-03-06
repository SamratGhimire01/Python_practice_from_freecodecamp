class Solution(object):
    def searchInsert(self, nums, target):
        for index,value in enumerate(nums):
            if value >= target:
                return index
        return len(nums)
   
s = Solution()
print(s.searchInsert([1,3,5,6],5))