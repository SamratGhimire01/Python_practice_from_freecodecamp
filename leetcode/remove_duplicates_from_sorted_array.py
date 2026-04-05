class Solution(object):
    def removeDuplicates(self, nums):
        i  = 1
        for k in range(1,len(nums)):
            if nums[k] != nums[k-1]:
                nums[i] = nums[k]
                i+=1
        return i
        
        
s= Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))