# 50 - [Pow(x, n) ](https://leetcode.com/problems/powx-n/)

## 1. recursive
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n//2)
```

## 2. iterative
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n < 0:
            n = -n
            x = 1 / x
            
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
```