class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not len(nums):
            return res
        
        left, right = 0, len(nums) - 1

        # 左边界：left指针向左移动到第一个target出现的位置
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid

        # 找不到target
        if nums[left] != target:
            return res

        # 右边界：找最后一个target出现的位置
        res[0] = left
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1   # 令mid偏向右边
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        res[1] = right
        return res

nums = [5,7,7,8,8,10]
s = Solution()
r = s.searchRange(nums, 8)
print(r)
