class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ret = i = 0
        while i < len(nums):
        	ret += nums[i]
        	i += 2
        return ret

nums = [1,4,3,2]      
s = Solution()
r = s.arrayPairSum(nums)
print(r)