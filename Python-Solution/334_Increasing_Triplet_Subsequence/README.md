# 334 - [递增的三元子序列](https://leetcode.com/problems/increasing-triplet-subsequence/)


## 题解
需要判断序列中是否有三个递增的数，只需先找到两个数具有递增关系，且第三个数同时大于前两个数，那么这三个数就是递增的。
```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```
