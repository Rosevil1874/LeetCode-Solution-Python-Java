class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        i = n - 1
        while i >= 0:
            res[i] *= right
            right *= nums[i]
            i -= 1
        return res
        
nums = [1,2,3,4]
s = Solution()
r = s.productExceptSelf(nums)
print(r)