# 26 - 删除排序数组中的重复项

## 题目描述
![problem](images/26.png)

>审题：
1. 原地操作
2. 要注意返回的是数组的长度而不是数组

## 题解
思路：
1. 从下标1开始，依次和前面的元素比较；
2. 若相同，则删除当前元素，并更新数组长度（减一）；
3. 若不相同，下标后移一位。

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        newLen = length
        i = 1
        while i < length:
        	if nums[i] == nums[i-1]:
        		del nums[i]
        		length -= 1
        	else:
        		i += 1
        return length
```