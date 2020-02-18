# 172 - [阶乘后的零](https://leetcode.com/problems/factorial-trailing-zeroes/)


## 1. recursive
```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if not n:
            return 0
        return n//5 + self.trailingZeroes(n // 5)
```


## 2. iterative
```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n // 5
            n //= 5
        return cnt
```