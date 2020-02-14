# 371 - 两整数之和

## 题目描述
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

**Example 1:**

	Input: a = 1, b = 2
	Output: 3

**Example 2:**

	Input: a = -2, b = 3
	Output: 1


## 题解
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF    # 32bit 最大正整数
        MIN = 0x80000000    # 32bit 最小负整数
        mask = 0xFFFFFFFF   # 掩码：得到一个二进制数最后32位
        
        while b:
            # 加法不带进位的结果，进位
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # a <= MAX: a为正数，直接返回
        # a > MAX：a为负数，先计算其32为补码，再取反
        return a if a < MAX else ~(a ^ mask)
        
```
