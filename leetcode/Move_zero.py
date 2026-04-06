class Solution(object):
    def moveZeroes(self, nums):
        index_value=0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[index_value] = nums[i]
                index_value+=1

        for i in range(index_value,len(nums)):
            nums[i]=0
            
        return nums


s= Solution()
print(s.moveZeroes([0,1,0,3,12]))
        
        
