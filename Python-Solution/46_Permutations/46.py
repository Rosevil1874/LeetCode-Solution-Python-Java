class Solution(object):
    def permuteHelp(self, nums, temp, result):
        # 所有数已经排列完成，得到全排列中的一种情况
        if len(temp) == len(nums):
            result.append(temp[:])
            return

        # 递归全排列
        for i in range(len(nums)):
            if nums[i] in temp: continue
            temp.append(nums[i])                            # 加入当前元素
            self.permuteHelp(nums, temp, result)            # 继续向后添加
            temp.pop()     # 删除刚刚添加的最后一个元素，尝试其他的数字即得到新的排列


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, temp = [], []
        self.permuteHelp(nums, temp, result)
        return result



nums = [1,2,3]
s = Solution()
r = s.permute(nums)
print(r)
