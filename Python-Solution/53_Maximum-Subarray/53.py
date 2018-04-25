class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.maxSubSum(nums, 0, n - 1)

    def maxSubSum(self, nums, left, right):
    	# base case
    	if left == right:
    		# if nums[left] > 0:
    		return nums[left]
    		# else:
    			# return 0

    	mid = (left + right) // 2
    	maxLeftSum = self.maxSubSum(nums, left, mid)
    	maxRightSum = self.maxSubSum(nums, mid + 1, right)

    	# 求跨边界最优值的左右子序列
    	# maxLeftBorderSum = maxRightBorderSum = 0	
    	# leftBorderSum = rightBorderSum = 0

    	maxLeftBorderSum = leftBorderSum = nums[mid]
    	i = mid - 1
    	while i >= left:
    		leftBorderSum += nums[i]
    		maxLeftBorderSum = max(maxLeftBorderSum, leftBorderSum)
    		i -= 1

    	maxRightBorderSum = rightBorderSum = nums[mid + 1]
    	i = mid + 2
    	while i <= right:
    		rightBorderSum += nums[i]
    		maxRightBorderSum = max(maxRightBorderSum, rightBorderSum)
    		i += 1

    	maxBorderSum = maxLeftBorderSum + maxRightBorderSum

    	return max(maxLeftSum, maxRightSum, maxBorderSum)


nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
r = s.maxSubArray(nums)
print(r)
