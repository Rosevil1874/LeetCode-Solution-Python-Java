# 33 - 搜索旋转排序数组

## 题目描述
![problem](images/33.png)

>关联题目： [81. 删除排序数组中的重复项-II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/81_Search-in-Rotated-Sorted-Array-II)

>审题：
1. 返回目标索引，不存在则返回-1；
2. 时间复杂度O(log n)。

## 一、简单判断法
**时间复杂度O(n)**  
思路：
由于时间复杂度限制到了O(log n)，不能先排序，关键在于旋转点。旋转点左边子序列大于右边子序列。可以判断target，若其大于nums[0]，则从前往后查找，否则从后往前查找。  

> Runtime: 32 ms, faster than 98.17% of Python3 online submissions.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not n:
            return -1
        
        if nums[0] == target:
            return 0
        # target在前半段
        elif nums[0] < target:
            for i in range(1, n):
                if nums[i] == target:
                    return i
        # target在后半段
        else:
            for i in range(n - 1, -1, -1):
                if nums[i] == target:
                    return i

        # target不存在
        return -1
```

## 二、二分查找法
**时间复杂度O(log n)**  

思路：
1. 先将数组二分，判断target与nums[mid]的关系，若target == nums[mid]，直接返回下标，否则进入第二步；
2. 若nums[left] <= nums[mid]，则左子序列是排好序的。同时若target > nums[left] and target < nums[mid]，则且target在其中，对左子序列二分查找即可；否则从第一步开始递归处理右侧旋转数组。
3. 若nums[mid] <= nums[right]，则右子序列是排好序的。同时若target > nums[mid] and target < nums[right]，则target在其中，对右子序列二分查找即可；否则从第一步开始递归处理左侧旋转数组。

> Runtime: 36 ms, faster than 93.22% of Python3 online submissions .

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # 左子序列有序
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # 右子序列有序
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```