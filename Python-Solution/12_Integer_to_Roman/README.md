---
title: 12 - 整数转罗马数字
date: 2018-04-07 18:17:26
tags: 
- LeetCode
- Python
categories: LeetCode
---

## 题目描述
![problem](images/12.png)

<!-- more -->

<blockquote class="blockquote-center">恕我无知，拿到这题的第一件事就是上搜索引擎，看看罗马数字是咋回事。。。</blockquote>

## 罗马数字
我觉得这位兄台的和百科差不多，又比百科美观，就借过来用用嘻嘻。
![RomanNumber](images/RomanNumber.png)
## 整数转罗马数字
cr: [leetcode 罗马数字与整数的转换算法](https://blog.csdn.net/net_wolf_007/article/details/51770112)

1. 数字可以放在左边也可以放在右边，逻辑比较复杂。
2. 如果都只能放在右边，那样就可以直接使用加法。如9表示为IX, 而如果表示为 VIIII,这样处理相加就OK.  
3. 可以使用组合数字来进行拆分，使程序能够实现连加的方法。

```python
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            return ''

        ret = ''
        roman = ["M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        arab = [1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5, 4, 1]

        for i in range(13):
            if num > 0:
                if num < arab[i]:
                    continue
                while num >= arab[i]:
                    num -= arab[i]
                    ret += roman[i]
        return ret
```