# 47 - 全排列-II


## 题解一：回溯/DFS

>**思路：** 
1. 固定第一位，对剩余序列进行全排列；
2. 固定前两位，对剩余序列进行全排列；
.
.
4. 直到最后一位；
5. 全排列是上面每一步的结果的集合。

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, res)
        return res
        
        
    def helper(self, nums: List[int], begin: int, res: List[List[int]]):
        # 全部数值已加入当前排列，当前排列完成
        if begin == len(nums):
            res.append(nums[:])
            return
        
        # 递归全排列
        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.helper(nums, begin + 1, res)
            nums[begin], nums[i] = nums[i], nums[begin]     # 回溯：还原数组

```


## 题解二： 回溯/DFS

>reference: [全排列](https://leetcode.windliang.cc/leetCode-46-Permutations.html)

```python
class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, temp = [], []
        self.permuteHelp(nums, temp, result)
        return result


    def permuteHelp(self, nums: List[int], temp: List[int], result: List[List[int]]):
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
```