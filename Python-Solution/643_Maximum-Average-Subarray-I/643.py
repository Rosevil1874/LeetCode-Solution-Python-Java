class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        theSum = sum(nums[0 : k])
        maxinum = theSum

        for i in range(k, len(nums)):
            theSum += nums[i] - nums[i - k]
            maxinum = max(theSum, maxinum)
        return maxinum / k

        
nums = [1, 12, -5, -6, 50, 3]
s = Solution()
res = s.findMaxAverage(nums, 4)
print(res)