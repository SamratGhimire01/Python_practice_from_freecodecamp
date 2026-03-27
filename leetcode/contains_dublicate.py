class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
s = Solution()
print(s.containsDuplicate([1,2,3,4]))