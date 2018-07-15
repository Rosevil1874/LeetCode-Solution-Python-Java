class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = str(num)
        n = len(nums)
        maximum = n - 1
        maxs = [0 for i in range(n)]

        # 找到每个元素后的最大值所在位置
        for i in range(n-1, -1, -1):
            if nums[i] > nums[maximum]:
                maximum = i
            maxs[i] = maximum

        # 交换
        for i in range(n):
            if nums[i] != nums[maxs[i]]:
                nums = nums[:i] + nums[maxs[i]] +nums[i+1:maxs[i]] + nums[i] + nums[maxs[i]+1:]
                break
        return int(nums)

s = Solution()
res = s.maximumSwap(2736)
print(res)