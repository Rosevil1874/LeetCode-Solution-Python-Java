# 215 - [数组中的第K个最大元素](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## 题目描述
![problem](images/215.png)

>关联题目： [414. 第三大的数](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/414_Third-Maximum-Number)   
此题中的k是变量，大小未知，继续用414题中的方法肯定就行不通了。
所幸这题不用去重也没有时间复杂度限制嘿嘿嘿(ღ˘︶˘ღ)，恩思路基本就是排序了。

## 一、原生sort函数
一行代码，实际上是作弊。。。

> 时间复杂度：O(nlogn).   
Runtime: 64 ms, faster than 77.80% of Python3 online submissions. 

```python
class Solution(object):
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
```


## 二、冒泡排序
> 时间复杂度：O(nk).   
Runtime: 2490 ms, faster than 5.03% of Python3 online submissions.

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(k):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[-k]
```


## 三、选择排序
> 时间复杂度：O(nk).  
Runtime: 2484 ms, faster than 5.03% of Python3 online submissions.

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = []
        for i in range(n, n - k, -1):
            max_idx = 0
            for j in range(i):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            # 将未排序子序列中的最大元素移到排序子序列相应位置上
            nums[max_idx], nums[i - 1] = nums[i - 1], nums[max_idx]
        return nums[-k]
```


## 四、堆排序

python的heapq模块默认实现最小堆。
> 时间复杂度O(n+klogn). 
Runtime: 64 ms, faster than 77.80% of Python3 online submissions

```python
from heapq import heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heappush(heap, x)
        for _ in range(len(nums) - k):
            heappop(heap)
        return heappop(heap)
```

取负的方法实现最大堆：
```python
from heapq import heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heappush(heap, -x)
        for _ in range(k - 1):
            heappop(heap)
        return -heappop(heap)
```

直接用内置方法，作弊行为+1.

> 时间复杂度O(n+klogn).  
Runtime: 68 ms, faster than 55.95% of Python3 online submissions

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```


## 五、快速选择 Quick Select

**Quick Select算法：**  
1. Quick select算法通常用来在未排序的数组中寻找第k小/第k大的元素。其方法类似于Quick sort。
2. Quick select算法因其高效和良好的average case时间复杂度而被广为应用。Quick select的average case时间复杂度为O(n)，然而其worst case时间复杂度为O(n^2)。
3. 总体而言，Quick select采用和Quick sort类似的步骤。首先选定一个pivot，然后根据每个数与该pivot的大小关系将整个数组分为两部分。与Quick sort不同的是，Quick select只考虑所寻找的目标所在的那一部分子数组，而非像Quick sort一样分别再对两边进行分割。正是因为如此，Quick select将平均时间复杂度从O(nlogn)降到了**O(n)**。

以下代码cr: [C++ Solutions](https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60309/4-C++-Solutions-using-Partition-Max-Heap-priority_queue-and-multiset-respectively)  

>思路：  
1. Initialize left to be 0 and right to be len(nums) - 1;
2. Partition the array, if the pivot is at the k-1-th position, return it (we are done);
3. If the pivot is right to the k-1-th position, update right to be the left neighbor of the pivot;
4. Else update left to be the right neighbor of the pivot.
Repeat 2.

> Runtime: 2572 ms, faster than 5.03% of Python3 online submissions.

```python
class Solution(object):
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 找到第k大的数，就是找到在降序排列后坐标在k-1位置的元素
        left, right = 0, len(nums) - 1
        while left <= right:
            pos = self.partition(nums, left, right)
            if pos > k - 1:          
                right = pos - 1
            elif pos < k - 1:
                left = pos + 1
            else:
                return nums[pos]
        
    # 把大于pivot的元素移到pivot左边，小于pivot的元素移到pivot右边
    # 返回pivot的坐标，其现在的坐标和在排序后数组中的坐标相同
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]
        l, r = left + 1, right
        while  l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] >= pivot:
                l += 1
            elif nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r
```