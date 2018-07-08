class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for x in nums:
        	nums[x - 1] = - nums[x - 1]

        for i in range(len(nums)):
        	if nums[i] >= 0:
        		res.append(i + 1)

        return res