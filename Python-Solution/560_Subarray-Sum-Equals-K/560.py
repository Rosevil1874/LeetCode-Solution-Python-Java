class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        theSum = 0
        preSum = {0:1}
        for x in nums:
            theSum += x
            cnt += preSum.get(theSum - k, 0)
            preSum[theSum] = preSum.get(theSum, 0) + 1
        return cnt

nums = [1, 1, 1]
s = Solution()
res = s.subarraySum(nums, 2)
print(res)