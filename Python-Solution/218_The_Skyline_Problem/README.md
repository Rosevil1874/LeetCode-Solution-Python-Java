# 218 - [天际线问题](https://leetcode.com/problems/the-skyline-problem/)

## 题目描述
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B). 

Figure A:
![figure a](https://assets.leetcode.com/static_assets/public/images/problemset/skyline1.jpg)

Figure B:
![figure b](https://leetcode.com/static/images/problemset/skyline2.jpg)

观察图B，可以发现输出的红点是每一条水平线的起点。

## [题解](https://leetcode.com/problems/the-skyline-problem/discuss/61261/)
**思路：**使用一条竖直的线从左向右扫描，当最高的高度变化时，记录[x, height]到res。 python默认实现最小堆，我们可以push和pop值的相反数实现最大堆。 这个discussion下有一个同胞发了带详细中文注解的版本，但是我没怎么懂。因为现在是2020.02.13, 一家人因为疫情困在家里，除了我，他们都在看综艺笑得甚欢。。。

```python
from heapq import *
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 添加开始扫描建筑事件
        # 添加结束扫描建筑事件(0高度的building)
        # 为事件排序：left → right
        events = [(l, -h, r) for l, r, h in buildings]
        events += list({(r, 0, 0) for _, r, _ in buildings})
        events.sort()
        
        # res: [x, height]
        # hp: [-height, ending position], 一条高为height的skyline在end position结束
        res = [[0, 0]]
        hp = [(0, float('inf'))]
        for l, neg_h, r in events:
            # 1. pop已经扫描结束的building
            while l >= hp[0][1]:
                heappop(hp)
            
            # 2. 如果是开始扫描事件，激活这座building
            if neg_h:
                heappush(hp, (neg_h, r))
                
            # 3. 如果前一个height和当前最高height不相等，结束这个result
            if res[-1][1] != -hp[0][0]:
                res.append([l, -hp[0][0]])
        return res[1:]
```