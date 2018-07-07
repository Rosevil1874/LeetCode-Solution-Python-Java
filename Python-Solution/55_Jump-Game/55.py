class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = n - 2
        last = n - 1
        while i >= 0:
        	if nums[i] + i >= last:
        		last = i
        	i -= 1
        return last <= 0
        

nums = [2,3,1,1,4]
s = Solution()
r = s.canJump(nums)
print(r)
