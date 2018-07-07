# 162 - 寻找峰值

## 题目描述
![problem](images/162.png)

## 题解
**时间复杂度O(logN)**
>看到要求时间复杂度O(logN)就立马想到了binary search。

思路：  
如果

## 一、递归
```python
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binSearch(nums, 0, len(nums) - 1)

    def binSearch(self, nums, left, right):
        if left == right:
            return left

        mid1 = (left + right) // 2
        mid2 = mid1 + 1
        if nums[mid1] > nums[mid2]:
            return self.binSearch(nums, left, mid1)
        else:
            return self.binSearch(nums, mid2, right)
```

## 二、迭代
**迭代1**
```python
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            elif  nums[mid] < nums[mid + 1]:
                left = mid + 1

        return left if nums[left] >= nums[right] else right
```

**迭代2**
```python
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums[mid1] > nums[mid2]:
                right = mid1
            else:
                left = mid2
        return left
```