class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left


nums = [9,6,4,2,3,5,7,0,1]
s = Solution()
r = s.moveZeroes(nums)
print(r)
