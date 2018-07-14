class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range( 1, len(nums) ):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt > 1:
                    return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else: 
                    nums[i] = nums[i - 1]
        return True

        
# nums = [4,2,3]
nums = [4, 4, 2, 3, 3, 6]
s = Solution()
res = s.checkPossibility(nums)
print(res)