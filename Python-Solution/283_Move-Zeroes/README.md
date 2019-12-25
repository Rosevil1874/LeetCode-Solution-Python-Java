# 283 - 移动零

## 题目描述
![problem](images/283.png)

## 题解一
**这个思路不是严格意义上的in-place**  

思路：  
1. 计算0出现的次数cnt；
2. 从数组头部开始查找0的位置并删除，在数组末尾添加0，进行cnt次。

> Runtime: 104 ms, faster than 20.53% of Python3 online submissions

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        for i in range(cnt):
            idx = nums.index(0)
            del nums[idx]
            nums.append(0)
```


## 题解二
**in-place**  

思路：  
1. 一个变量记录0元素的位置；
2. 每次将0与后一个不是0的元素交换位置，直到换到最后。

> Runtime: 52 ms, faster than 74.92% of Python3 online submissions 

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
```