# 150 - 逆波兰表达式求值

## 题目描述
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, \*, /. Each operand may be an integer or another expression.

**Note:**

	Division between two integers should truncate toward zero.
	The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:

	Input: ["2", "1", "+", "3", "\*"]
	Output: 9
	Explanation: ((2 + 1) \* 3) = 9

Example 2:

	Input: ["4", "13", "5", "/", "+"]
	Output: 6
	Explanation: (4 + (13 / 5)) = 6

Example 3:

	Input: ["10", "6", "9", "3", "+", "-11", "\*", "/", "\*", "17", "+", "5", "+"]
	Output: 22
	Explanation: 
	  ((10 \* (6 / ((9 + 3) \* -11))) + 17) + 5
	= ((10 \* (6 / (12 \* -11))) + 17) + 5
	= ((10 \* (6 / -132)) + 17) + 5
	= ((10 \* 0) + 17) + 5
	= (0 + 17) + 5
	= 17 + 5
	= 22


## 栈

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                r , l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                else:
                    # python中1//-3这种情况的结果为-1
                    # 而此题中应为0
                    if l*r < 0 and l % r != 0:
                        stack.append(l // r + 1)
                    else:
                        stack.append(l // r)
        return stack[0]
                
```
