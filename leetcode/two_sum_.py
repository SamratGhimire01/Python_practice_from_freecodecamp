class Solution(object):
    def addone(self,num):
        return num[1:]
    def check(self,a,b,nums,target,current_idx):
        if not a:
            return None
        left = target-a[0]
        if left in b:
            for i in range(current_idx+1,len(nums)):
                if nums[i]==left:
                    return i
        return None
    def twoSum(self, nums, target):
        a=[x for x in nums if x<=target]
        b=self.addone(a)
        current_idx = 0
        while len(a)>0:
            result = self.check(a,b,nums,target,current_idx)
            if result is not None:
                return [current_idx, result]
            print(current_idx)
            a=self.addone(a)
            b=self.addone(a)
            current_idx+=1
            
        first = [i for i in range(len(nums)) if nums[i] == a[0] ]
        value= first[0]
        
        print(f"addition is {nums[value] + nums[result]} ")
        return f"[{value}, {result}]"
        
        
        
s=Solution()
print(s.twoSum([3,3],6))
# this solution is not efficient, it is O(n^2) in the worst case, because for each element in a, we are checking if the complement exists in b, which is O(n) in the worst case.


# and this the optimized solution using a hash table, which is O(n) in the worst case, because we are only iterating through the list once and checking for the complement in the hash table, which is O(1) on average.

class Solution(object):
   
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            left = target - num
            if left in seen:
                return[seen[left],i]
            seen[num]=i
        
        
s=Solution()
print(s.twoSum([3,2,4],6))

# this solution is efficient, it is O(n) in the worst case, because we are only iterating through the list once and checking for the complement in the hash table, which is O(1) on average.