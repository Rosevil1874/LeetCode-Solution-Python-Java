# 768 - 最多能完成排序的块 II

## 题目描述
![problem](images/769.png)

>相似题目：  
[769.最多能完成排序的块](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/769_Max-Chunks-To-Make-Sorted)


## 题解一
>其实和769的区别就是这题有重复元素，恕我直言，上一题的解法就能解这题哈哈哈。

**思路：**  
1. 要每个块排序后连在一起和原list排序后相同，那么所分的块之间相对顺序也应该是严格递增；
2. 检查从第零个元素开始的每个“前i个元素”子数组，若其包含的元素为排序后list的前i个元素，则其属于同一块中，否则后面的需再加一块才能表示。

```python
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sortedArr = sorted(arr)
        i, cnt = 1, 0
        while i <= len(arr):
            while sorted(arr[:i]) != sortedArr[:i] and i <= len(arr):
                i += 1
            cnt += 1
            i += 1
        return cnt
```
然鹅，果然没有这么简单，超时了啊啊啊啊😫


## 题解二
思路是一样的，不过大神就是大神啊啊啊。  
>参考：  [Python Easy and Concise Solution](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/discuss/113465/Python-Easy-and-Concise-Solution)  
lee215同学好厉害哦，我的python好多都抄他的。。。抄作业的感觉。。。

```python
from collections import Counter
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sortedArr = sorted(arr)
        cnt, c1, c2 = 0, Counter(), Counter()
        for a, b in zip(arr, sorted(arr)):
            c1[a] += 1
            c2[b] += 1
            cnt += c1 == c2
        return cnt
```