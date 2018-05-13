class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs( nums[idx] )
        print(nums)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        

nums = [4,3,2,7,8,2,3,1]  
s = Solution()
r = s.findDisappearedNumbers(nums)
print(r)