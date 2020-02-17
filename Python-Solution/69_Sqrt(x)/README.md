# 69 - [x的平方根](https://leetcode.com/problems/sqrtx/)


## 1. binary search
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1
        return right
```

## 2. bit manipulate
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        bit = 1 << 16
        
        # 从高位向低位计算，看每一位上是否可以为1
        while bit > 0:
            res |= bit
            # res回退到前一个值
            if res > x // res:
                res ^= bit
            bit >>= 1
        return res
```