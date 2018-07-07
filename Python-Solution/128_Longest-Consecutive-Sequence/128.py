class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        nums = set(nums)
        for x in nums:
        	if x - 1 not in nums:
        		y = x + 1
        		while y in nums:
        			y += 1
        		maxLen = max(maxLen, y - x)
        return maxLen
        
nums = [100, 4, 200, 1, 3, 2]
s = Solution()
res = s.longestConsecutive(nums)
print (res)