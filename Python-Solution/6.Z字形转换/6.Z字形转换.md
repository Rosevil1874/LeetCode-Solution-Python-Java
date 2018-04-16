---
title: 6 - Z字形转换
date: 2018-04-09 09:48:51
tags: 
- LeetCode
- Python
categories: LeetCode
---

## 题目描述
{% asset_img 6.png %}

<!-- more -->

看到题目的时候一脸懵逼，这啥呀，啥Z字形啊咋排的呀，怪不得这么多人给了unlike嚯嚯嚯。。。

{% asset_img down.png %}

事实证明，只有行数多了才能看出这个z，下图是直接用下标排的，一共5行。

{% asset_img Z字形.png %}


## 思路：
1. 一共N行时，total = 2*(N-1)个字符组成一个完整序列，即Z字的前两划；
2. 每total个字符为一组，计算这一组中每个字符在第几行；
3. 从第一行开始，把每一行的字符拼接起来返回。

```python
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
        	return s

        l = len(s)
        total = 2 * (numRows - 1)
        tmp = []
        ret = ''

        for k in range(numRows):
        	tmp.append('')

        for i in range(l):
        	idx = i % total
        	if idx >= numRows:
        		idx = total - idx
        	tmp[idx] += s[i]

        for j in range(numRows):
        	ret += tmp[j]
        return ret
```

自测是没有问题的，提交了三次都提交不上去，我也只好unlike了( ･´ω`･ )
恩恩好了好了AC了嚯嚯嚯