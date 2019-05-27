# 46 - 全排列

## 题目描述
![problem](images/46.png)


## 题解一：递归

>**思路：** 
1. 固定第一位，对剩余序列进行全排列；
2. 固定前两位，对剩余序列进行全排列；
.
.
4. 直到最后一位；
5. 全排列是上面每一步的结果的集合。

>reference: [全排列算法思路解析](https://blog.csdn.net/summerxiachen/article/details/60579623)

```python
class Solution(object):
    def permuteHelp(self, nums, begin, result):
        # 所有数已经排列完成，得到全排列中的一种情况
        if begin == len(nums):
            result.append(nums[:])
            return

        # 递归全排列
        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.permuteHelp(nums, begin + 1, result)
            nums[begin], nums[i] = nums[i], nums[begin]     # 还原数组


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permuteHelp(nums, 0, result)
        return result
```


## 题解二： 回溯/DFS

>reference: [全排列](https://leetcode.windliang.cc/leetCode-46-Permutations.html)

```python
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
```