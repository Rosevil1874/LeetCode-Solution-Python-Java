# 239 - [滑动窗口最大值](https://leetcode.com/problems/sliding-window-maximum/)

## 题目描述
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

**Example:**
input:
	nums = [1,3,-1,-3,5,3,6,7], and k = 3
output:
	[3,3,5,5,6,7] 

**Note:**
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

**Follow up:**
Could you solve it in linear time?


## 题解一

最蠢的办法，直接用max函数求得每个窗口的最大值。  
max函数的时间复杂度为O(n)，因此整个算法的时间复杂度为O(nk)。

> Runtime: 724 ms, faster than 7.04% of Python3 online submissions.

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        res = []
        for i in range(k, len(nums) + 1):
            res.append(max(nums[i - k:i]))
        return res
```


## 题解二
queue中降序存放当前窗口中元素的下标，queue[0]为当前窗口最大值的下标。  
时间复杂度O(n)

> Runtime: 176 ms, faster than 43.72% of Python3 online submissions.

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, res = [], []
        for i, x in enumerate(nums):
            # 弹出所有比当前元素小的元素的下标，保证降序
            while queue and nums[queue[-1]] < x:
                queue.pop()
            
            # 将当前元素下标加入队尾
            queue.append(i)
            
            # 若最大值坐标不在窗口内，将其去除
            if i - k + 1 > queue[0]:
                queue.pop(0)
                
            # 每滑动到一个窗口末尾试保存其最大值
            if i + 1 >= k:
                res.append(nums[queue[0]])
        return res
```