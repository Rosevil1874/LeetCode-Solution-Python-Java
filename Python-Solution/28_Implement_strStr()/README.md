# 28 - [实现 strStr()](https://leetcode.com/problems/implement-strstr/)

## 题解

```python
class Solution(object):
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n:
            return -1
        elif n == 0:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
```