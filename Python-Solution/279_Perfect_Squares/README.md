# 279 - [完美平方数](https://leetcode.com/problems/perfect-squares/)

## 题目描述
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

**Example 1:**
	Input: n = 12
	Output: 3 
	Explanation: 12 = 4 + 4 + 4.

**Example 2:**
	Input: n = 13
	Output: 2
	Explanation: 13 = 4 + 9.


## 1. BFS

> ref: [BFS](https://leetcode.com/problems/perfect-squares/discuss/71475/).  
Runtime: 196 ms, faster than 81.78% of Python3 online submissions

```python
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        # 计算小于等于n的所有平方数
        square = []
        i = 1
        while i * i <= n:
            square.append(i * i)
            i += 1
            
        cnt = 0
        to_check = {n}
        while to_check:
            cnt += 1
            tmp = set()
            for x in to_check:
                for y in square:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    tmp.add(x - y)
            to_check = tmp
        return cnt
```


## 2. DP

> Runtime: 5336 ms, faster than 20.44% of Python3 online submissions.

```python
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        # cnt[i]：和为i的最少平方数个数，和为0的有0个
        cnt = [float('inf')] * (n + 1)
        cnt[0] = 0
        
        # i = (i - j * j) + (j * j)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # min(不减去j*j，减去j*j)
                cnt[i] = min(cnt[i], cnt[i - j*j] + 1)
                j += 1
        return cnt[-1]
```