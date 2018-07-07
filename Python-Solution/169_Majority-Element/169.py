class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        cnt = 0
        for i in range(1, len(nums)):
        	if nums[i] == candidate:
        		cnt += 1
        	elif cnt == 0:
        		candidate = nums[i]
        	else:
        		cnt -= 1
        return candidate

nums = [-1, 1,1,1, 2]
s = Solution()
r = s.majorityElement(nums)
print(r)