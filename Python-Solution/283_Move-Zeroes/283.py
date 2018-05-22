class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
        	if nums[i] != 0:
        		nums[i], nums[idx] = nums[idx], nums[i]
        		idx += 1


nums = [0,1,0,3,12]
s = Solution()
s.moveZeroes(nums)
print(nums)
