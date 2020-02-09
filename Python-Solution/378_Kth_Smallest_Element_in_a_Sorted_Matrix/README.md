# 378 - 有序矩阵中第k小的元素

## 题目描述
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

**Example:**

	matrix = [
	   [ 1,  5,  9],
	   [10, 11, 13],
	   [12, 13, 15]
	],
	k = 8,

	return 13.

**Note:**
You may assume k is always valid, 1 ≤ k ≤ n2.


**[ref](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/)**

## 1. heap
这个代码没有AC，需要debug。
```python
from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        
        # 将第一行的元素放入最小堆中（堆中不需要超过k个元素）
        # 由于输出的是第k小的元素而不是第k小的不同的值，需要同时记录元素位置以区分值相同的元素
        for j in range(len(matrix[0])):
            heappush(min_heap, (0, j, matrix[0][j]))
            
        k_count = 0 
        while min_heap:
            i, j, num = heappop(min_heap)
            k_count += 1
            if k_count == k:
                break
            if i + 1 < len(matrix):
                heappush(min_heap, (i + 1, j, matrix[i + 1][j]))
        return num
```


## 2. binary search