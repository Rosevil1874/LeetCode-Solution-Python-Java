# 14 - 最长公共前缀

## 题目描述
![problem](images/14.png)

<!-- more -->

>审题：多么简单粗暴的题目啊

## 方法
思路：
1. 找出最短的字符串，以其为基准；
2. 遍历最短字符串的每个字符，同时检查其他每个字符串的当前位置字符；
3. 若不相等，返回最长前缀；
4. 若相等，最长前缀更新：加上当前字符。

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        
        shortest = min(strs, key = len)
        for i, ch in enumerate(shortest):
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]
        return shortest
```