class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1=sorted(nums1+nums2)
        mid = len(nums1) // 2
        if len(nums1) % 2 == 0:
            return (nums1[mid-1] + nums1[mid]) / 2.0
        return float(nums1[mid])
        

s=Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))
        