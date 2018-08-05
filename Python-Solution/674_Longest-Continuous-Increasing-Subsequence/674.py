class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        longest = 0
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                longest = max(longest, cnt)
                cnt = 1
        return max(longest, cnt)
        
# nums = [1,3,5,4,7]       
nums = [1, 3, 5, 7]
s = Solution()
r = s.findLengthOfLCIS(nums)
print(r)
   