class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums[mid1] > nums[mid2]:
                right = mid1
            else:
                left = mid2
        return left
        
        
nums = [1,2,3,1]
s = Solution()
res = s.findPeakElement(nums)
print (res)