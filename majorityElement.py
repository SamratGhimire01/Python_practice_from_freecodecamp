class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for value in nums:
            if value in count:
                count[value]+=1
            else:
                count[value]=1
            if count[value] > len(nums)/2:
                return value
s= Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))
        