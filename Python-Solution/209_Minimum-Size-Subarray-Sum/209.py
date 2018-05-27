class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        # nums[i]为前i个数的和
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        minLen = float('inf')
        start = 0
        for i in range(len(nums)):
            if nums[i] >= s:
                start = self.findStart(start, i, nums[i], nums, s)
                minLen = min(minLen, i - start + 1)
        return 0 if minLen == float('inf') else minLen

    def findStart(self, left, right, sum_i, nums, s):
        while left < right:
            mid = (left + right) // 2
            if sum_i - nums[mid] >= s:
                left = mid + 1
            else:
                right = mid
        return left


solution = Solution()
nums = [5,1,3,5,10,7,4,9,2,8]
s = 15
# nums = [2,3,1,2,4,3]
# s = 7
# nums = [1, 4, 4]
# s = 4
res = solution.minSubArrayLen(s, nums)
print(res)