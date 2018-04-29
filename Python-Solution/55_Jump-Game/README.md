# 55 - 跳跃游戏

## 题目描述
![problem](images/55.png)

>关联题目：[45. 跳跃游戏II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/45_Jump-Game-II)

## 题解

思路：
1. 从后往前判断，即从倒数第二个位置开始，以最大步数判断前面的位置能否跳到后面来，如果可以继续往前判断；
2. 若最后能走到第一个位置，则说明从第一个位置也能走到最后。

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = n - 2
        last = n - 1
        while i >= 0:
        	if nums[i] + i >= last:
        		last = i
        	i -= 1
        return last <= 0

```
