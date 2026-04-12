class Solution(object):
    def twoSum(self, numbers, target):
        prev = {}
        
        for key,value in enumerate(numbers):
            diff = target - value
            if diff in prev:
                return [prev[diff]+1,key+1]
            prev[value] = key

s= Solution()
print(s.twoSum([2,7,11,15],9))