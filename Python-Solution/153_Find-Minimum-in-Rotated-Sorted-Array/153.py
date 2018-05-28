class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
        	if nums[left] < nums[right]:
        		return nums[left]

        	mid = (left + right) // 2
        	if nums[left] <= nums[mid]:
        		left = mid + 1
        	else:
        		right = mid
        return nums[left]
        

s = Solution()
nums = [2, 1]

res = s.findMin(nums)
print(res)