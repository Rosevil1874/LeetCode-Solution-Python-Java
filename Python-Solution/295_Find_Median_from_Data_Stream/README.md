# 295 - [数据流中的中位数](https://leetcode.com/problems/find-median-from-data-stream/)

## 题目描述
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

**Example:**
	addNum(1)
	addNum(2)
	findMedian() -> 1.5
	addNum(3) 
	findMedian() -> 2

**Follow up:**
1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


## 题解
使用两个堆：
1. 大顶堆中最大的数值小于等于小顶堆中的最小数，也就是小于小顶堆的堆顶。保持两个堆中的元素个数至多相差一个（这里保证小顶堆中个数较多）；
2. 数据总数是偶数时，大顶堆和小顶堆一边占一半元素，而且是有序的，很像二分法，这时，中位数为两堆顶平均值；
3. 如果数据个数为奇数，则中位数出现在元素个数多的堆的堆顶中（这里为小顶堆的堆顶）；
4. python的heapq默认实现小顶堆，添加元素和取出元素时均取反则实现大顶堆。

```python
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heappush(large, -heappushpop(small, num)) 	#将num放入小顶堆，并弹出小顶堆的最小值，取反，放入大顶堆large
        if len(small) < len(large):					#弹出large中最小的值，取反，即最大的值，放入small
            heappush(small, -heappop(large))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(small) > len(large):
            return float(small[0])
        return (small[0] - large[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
