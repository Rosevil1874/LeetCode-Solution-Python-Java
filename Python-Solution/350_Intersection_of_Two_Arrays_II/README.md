# 350 - 两个数组的交集 II

## 题目描述
Given two arrays, write a function to compute their intersection.

**Example 1:**
	Input: nums1 = [1,2,2,1], nums2 = [2,2]
	Output: [2,2]
**Example 2:**
	Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
	Output: [4,9]

**Note:**
	Each element in the result should appear as many times as it shows in both arrays.
	The result can be in any order.

**Follow up:**
	What if the given array is already sorted? How would you optimize your algorithm?
	What if nums1's size is small compared to nums2's size? Which algorithm is better?
	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


## 1. collections.Counter

```python
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        C = Counter
        return list((C(nums1) & C(nums2)).elements())
```

## 2. dict
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = dict()
        res = []
        
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
            
        for num in nums2:
            if num in dict1 and dict1[num] > 0:
                res.append(num)
                dict1[num] -= 1
        return res
```


## 3. sort
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        p1, p2 = 0, 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res
```