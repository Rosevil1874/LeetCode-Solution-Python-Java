class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        beg, end = -1, -2
        left_max, right_min = nums[0], nums[n - 1]

        for i in range(1, n):
            left_max = max(left_max, nums[i])
            right_min = min(right_min, nums[n - 1 - i])
            if nums[i] < left_max:
                end = i
            if nums[n - 1 - i] > right_min: 
                beg = n - 1 - i

        return end - beg + 1

nums = [2, 6, 4, 8, 10, 9, 15]
s = Solution()
res = s.findUnsortedSubarray(nums)
print(res)