class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxIdx = -1
        maxNum = float('-inf')
        secondNum = float('-inf')

        for i in range(len(nums)):
        	if nums[i] > maxNum:
        		secondNum = maxNum
        		maxNum = nums[i]
        		maxIdx = i
        	elif nums[i] > secondNum:
        		secondNum = nums[i]
        return maxIdx if maxNum >= (2 * secondNum) else -1

        
nums = [3, 6, 1, 0]
s = Solution()
r = s.dominantIndex(nums)
print(r)
