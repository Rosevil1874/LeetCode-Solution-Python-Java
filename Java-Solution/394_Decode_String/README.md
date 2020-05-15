# 394 - [字符串解码](https://leetcode.com/problems/decode-string/)

## 题目描述
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].


**Examples:**

	s = "3[a]2[bc]", return "aaabcbc".
	s = "3[a2[c]]", return "accaccacc".
	s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


## stack 

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [['', 1]]     # curr_string, curr_num
        num = 0
        for c in s:
            # 数字，更新重复次数（可能不止一位，因此要和前面出现的位做运算得到结果）
            if c.isdigit():
                num = num * 10 + int(c)
                # num = num * 10 + ord(c) - ord('0')
            # 左括号，将新的子串及其重复次数压入栈顶
            elif c == '[':
                stack.append(['', num])
                num = 0
            # 右括号，说明最近一个重复子串结束，将其出栈并拼接在前面的字符串后
            elif c == ']':
                curr_string, k = stack.pop()
                stack[-1][0] += curr_string * k
            # 普通字符，直接加在curr_string后面，curr_string是栈顶的第一个值
            else:
                stack[-1][0] += c
        return stack[0][0]
```