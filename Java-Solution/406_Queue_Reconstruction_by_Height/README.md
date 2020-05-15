# 406 - [根据身高重建队列](https://leetcode.com/problems/queue-reconstruction-by-height/)

## 题目描述
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

**Note:**
The number of people is less than 1,100.

**Example**
	Input:
	[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

	Output:
	[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


## 题解
1. 将所有数据先按身高h排序，再按k排序；
2. 将身高最高的部分抽取出来，它们在结果res中的顺序就和此时的顺序一样了；
3. 同理，将次高的到最矮的部分分别取出排序，并一个个插入到先前的res列表中。
	
```python
class Solution:
    def reconstructQueue(self, people):
        # 按h降序、k升序排列
        people.sort(key=lambda p: (-p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
```