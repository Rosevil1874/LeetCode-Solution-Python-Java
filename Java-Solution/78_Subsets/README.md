# 78 - 子集

## 题目描述
![problem](images/78.png)

>关联题目： [90. 子集II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/90_Subsets-II)

## 回溯法
确切地说是dfs，因为这里没有回溯操作。

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, [], 0)
        return res
        
    def dfs(self, nums, res, path, start):
        res.append(path)
        for i in range(start, len(nums)):   
            self.dfs(nums, res, path + [nums[i]], i + 1)
```


## 迭代

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in sorted(nums):
            res += [subset + [x] for subset in res]
        return res
```


## 位运算
>'To give all the possible subsets, we just need to exhaust all the possible combinations of the numbers. And each number has only two possibilities: either in or not in a subset. And this can be represented using a bit.'

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(1 << len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & 1 << j:
                    temp.append(nums[j])
            res.append(temp)
        return res
```