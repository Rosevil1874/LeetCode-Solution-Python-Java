# 231 - 打家劫舍-II

## DP
将序列围成环，保证相邻位置不能同时选中，其实就是将其拆成两个序列nums[1:]和nums[:n-1]。再使用198题的方法分别解出最优值，选出其中的最大值。
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        def helper(nums):
            if not nums or len(nums) == 0:
                return 0

            n = len(nums)
            if n == 1:
                return nums[0]
            elif n == 2:
                return max(nums[0], nums[1])

            dp = [0] * (n)      # 到第i家的时候的最高金额
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
```
