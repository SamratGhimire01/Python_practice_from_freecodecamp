class Solution(object):
    def maximumCount(self, nums):
        n =len(nums)
        low =0
        high = n-1
        neg=-1
        while low <=high:
            mid = (low+high)//2
            if nums[mid]<0:
                neg = mid
                low = mid+1
            else:
                high=mid-1
        
        low = 0
        high = n-1
        pos=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>0:
                pos = mid
                high = mid -1
            else:
                low = mid+1
        
        if neg+1 > n-pos:
            return neg+1
        else:
            return n-pos
                
            
s=Solution()
print(s.maximumCount([-2,-1,-1,1,2,3]))
