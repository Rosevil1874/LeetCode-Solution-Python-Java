---
title: 5 - 最长回文子串
date: 2018-04-08 13:27:31
tags: 
- LeetCode
- Python
categories: LeetCode
---

## 题目描述
![problem](/images/5.png)

<!-- more -->

## 方法一
思路：
1. 分别以每个元素为中心，找出偶数长度的最长回文子串和奇数长度的最长回文子串
2. 取奇偶中最长的一个
3. 取所有元素为中心的最长的一个
```python
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s

        start = 0
        max_len = 0
        max_s = ''
        for i in range(1, l):
            low = i - 1
            high = i
            while low>=0 and high<l and s[low]==s[high]:
                low -= 1
                high += 1
            if high-low+1 > max_len:
                max_len = high-low+1
                max_s = s[low+1 : high]

            low = i - 1
            high = i + 1
            while low>=0 and high<l and s[low]==s[high]:
                low -= 1
                high += 1
            if high-low+1 > max_len:
                max_len = high-low+1
                max_s = s[low+1 : high]
        return max_s
```

## 方法二：Manacher算法
**中期答辩精力有限，下次吧**