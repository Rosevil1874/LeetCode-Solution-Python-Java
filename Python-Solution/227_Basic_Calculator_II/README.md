# 227 - 基本计算器 II

## 题目描述
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, \*, / operators and empty spaces . The integer division should truncate toward zero.

**Example 1:**
	Input: "3+2\*2"
	Output: 7
**Example 2:**
	Input: " 3/2 "
	Output: 1
**Example 3:**
	Input: " 3+5 / 2 "
	Output: 5
**Note:**
	You may assume that the given expression is always valid.
	Do not use the eval built-in library function.


## 题解
stack: 已经判断完符号并进行了乘除法运算的数字
num: 待计算的数字
sign：上一个还未执行的运算

```python
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    pre = stack.pop()
                    if pre < 0:
                        stack.append(-(abs(pre)//num))
                    else:
                        stack.append(pre//num)
                sign = s[i]
                num = 0
        return sum(stack)
```
