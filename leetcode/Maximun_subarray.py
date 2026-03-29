class Solution(object):
    def maxSubArray(self, nums):
        max_total = nums[0]
        curr_sum = 0
        for i in nums:
            if curr_sum <0:
                curr_sum = 0
            curr_sum+=i
            if curr_sum > max_total:
                max_total = curr_sum
        return max_total
        
        
s=Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
