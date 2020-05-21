# 32 - 最长有效括号

## 题目描述

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"



## 一、栈
思路：
1. 从前往后遍历字符串；
2. 若当前为字符'('则将其下标入栈，若当前字符为')'且栈顶为'('则将栈顶出栈，此时找到了一对有效括号，否则将')'的下标也入栈；
3. 遍历完成后栈中为无效括号的下标，可以计算出最长有效括号的长度。若栈为空则整个字符串中括号均有效匹配。

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    if s[stack[-1]] == '(':
                        stack.pop(-1)
                    else:
                        stack.append(i)
                else:
                    stack.append(i)

        if not stack:
            return len(s)
        else:
            longest_len = 0
            # 头尾加上两个哨兵，处理无效索引不从0开始和不以len(s)结束的情况
            stack.insert(0, -1)
            stack.append(len(s))
            for i in range(1, len(stack)):
                longest_len = max(longest_len, stack[i] - stack[i - 1] - 1)
            return longest_len
```

简化版：one pass
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest_len = 0
        left = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if not stack:
                    left = i
                else:
                    stack.pop(-1)
                    if not stack:
                        longest_len = max(longest_len, i - left)
                    else:
                        longest_len = max(longest_len, i - stack[-1])
        return longest_len
```


## 二、动态规划

> [ref:](https://leetcode.com/problems/longest-valid-parentheses/discuss/14312/My-ten-lines-python-solution).  
let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, then we have the following relationship:
dp[i + 1] = dp[p] + i - p + 1 where p is the position of '(' which can matches current ')' in the stack.

这里使用curr_longest代替dp。
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        curr_longest = [0]*(len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    curr_longest[i + 1] = curr_longest[p] + i - p + 1
        return max(curr_longest)
```
