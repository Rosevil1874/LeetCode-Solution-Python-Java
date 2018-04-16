---
title: 14 - 最长公共前缀
date: 2018-04-10 10:31:18
tags: 
- LeetCode
- Python
categories: LeetCode
---

## 题目描述
![problem](/images/14.png)

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
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_l = len(strs)
        if strs_l == 0:
            return ''

        pre = ''
        min_l = len(strs[0])
        for i in range(1, strs_l):
            min_l = min(min_l, len(strs[i]))

        for i in range(min_l):
            x = strs[0][i]
            for j in range(strs_l):
                if strs[j][i] != x :
                    return pre
            pre += x
        return pre
```