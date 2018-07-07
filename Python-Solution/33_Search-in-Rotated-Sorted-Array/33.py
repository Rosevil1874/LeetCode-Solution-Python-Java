class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        while left <= right:
        	mid = (left + right) // 2
        	if target == nums[mid]:
        		return mid
        	elif nums[left] <= nums[mid]:
        		if target >= nums[left] and target < nums[mid]:
        			right = mid - 1
        		else:
        			left = mid + 1
        	else:
        		if target > nums[mid] and target <= nums[right]:
        			left = mid + 1
        		else:
        			right = mid - 1
        return -1

nums = [4,5,6,7,0,1,2]
s = Solution()
r = s.search(nums, 0)
print(r)
