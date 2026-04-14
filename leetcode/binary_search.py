class Solution(object):
    def search(self, nums, target):
        low =0
        high = len(nums)-1

        while low <= high :
            mid=(low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                high = mid -1
            else :
                low = mid+1
        return -1
            
s= Solution()
print(s.search([-1,0,3,5,9,12],9))

#          or

# class Solution(object):
#     def search(self, nums, target):
#         if target not in nums:
#             return -1
#         for key,value in enumerate(nums):
#             if value == target:
#                 return key
            
# s= Solution()
# print(s.search([-1,0,3,5,9,12],5))