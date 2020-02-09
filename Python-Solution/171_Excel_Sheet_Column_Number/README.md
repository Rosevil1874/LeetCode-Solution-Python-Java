# 171 - Excel表列序号

## 题目描述
Given a column title as appear in an Excel sheet, return its corresponding column number.

**For example:**
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

**Example 1:**
	Input: "A"
	Output: 1
**Example 2:**
	Input: "AB"
	Output: 28
**Example 3:**
	Input: "ZY"
	Output: 701

## 题解
```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = '#ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = 0
        for char in s:
            res = res*26 + letters.index(char)
        return res
```
