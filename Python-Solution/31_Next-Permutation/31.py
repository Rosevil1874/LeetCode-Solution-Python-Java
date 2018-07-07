class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l - 2
        while i >= 0:
            for j in range(i+1, l):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i+1:] = sorted(nums[i+1:])
                    return
            # 当前位不可替换，则对后面的元素排序，以直接找到大值中的最小值
            nums[i:] = sorted(nums[i:])
            i -= 1
        nums[0:].sort()
        
nums = [1,1,5]
s = Solution()
s.nextPermutation(nums)
for i in range(len(nums)):
	print(nums[i])
