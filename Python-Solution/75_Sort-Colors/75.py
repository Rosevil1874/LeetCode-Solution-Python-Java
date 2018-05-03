class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red = 0
        blue = n - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                i -= 1
                blue -= 1
            i += 1
        
       
# nums = [2,0,2,1,1,0]
nums = [1,2,0]
s = Solution()
s.sortColors(nums)
print(nums)
