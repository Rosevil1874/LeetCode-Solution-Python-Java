# 125 - 验证回文串

## 题目描述
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note:** For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**
	Input: "A man, a plan, a canal: Panama"
	Output: true

**Example 2:**
	Input: "race a car"
	Output: false

空字符串是有效回文串，只验证字符串中的字母和数字而不关心其他符号，不区分大小写。

## 双指针
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True
```

## 翻转
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]
```