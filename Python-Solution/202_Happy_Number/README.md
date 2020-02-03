# 202 - [快乐数](https://leetcode.com/problems/happy-number/)

## 题目描述
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.


## 题解
```python
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            nums = [int(x) for x in str(n)]
            n = sum([i*i for i in nums])
        return n == 1
```