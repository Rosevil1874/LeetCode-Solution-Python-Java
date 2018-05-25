class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                maxLen = max(maxLen, cnt)
            else:
                cnt = 0
        return maxLen

        
nums = [1,1,0,1,1,1]
s = Solution()
r = s.findMaxConsecutiveOnes(nums)
print(r)
