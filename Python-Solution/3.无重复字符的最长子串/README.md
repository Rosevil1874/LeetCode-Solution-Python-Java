---
title: 3 - 无重复字符的最长子串
date: 2018-04-07 15:38:59
tags: 
- LeetCode
- Python
categories: LeetCode
---

## 题目描述
![problem](images/3.png)

<!-- more -->

## 自己的方法
首先这个题目之前肯定是做过的，但是，我就知道我如此暴力肯定会超时o(╥﹏╥)o

思路：
1. 字符串长度为0或者1直接返回0/1；
2. 外层循环：从第一个字符开始，依次将每一个字符作为结果字符串的首字符；
3. 内层循环：依次加字符，若是出现重复就将此重复字符作为首字符；
4. 可行是可行，但就是超时了。。。

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = len(s)
        if l == 0 or l == 1:
        	return l

        max_l = 1
        max_r = ''
        for i in range(l):
        	res = s[i]
	        tmp_l = 1
	        tmp_r = res
	        for j in range(i+1, l):
	        	if s[j] not in res:
	        		res += s[j]
	        	else:
	        		res = s[j]
	        	length = len(res)
	        	tmp_l = tmp_l if tmp_l > length else length
	        	tmp_r = tmp_r if tmp_l > length else res
	        max_l = max_l if max_l > tmp_l else tmp_l
	        # max_r = max_r if max_l > tmp_l else tmp_r
        # return max_r
        return max_l
```

## 别人的方法
思路：
1. 遍历字符串，过程中将出现过的字符存入字典，key为字符，value为字符下标
2. 用maxLength保存遍历过程中找到的最大不重复子串的长度
3. 用start保存最长子串的开始下标
4. 如果字符已经出现在字典中，更新start的值
5. 如果字符不在字典中，更新maxLength的值

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = maxLength = 0
        usedChar = {}

        for i in range(l):
        	if s[i] in usedChar and start <= usedChar[s[i]]:
        		start = usedChar[s[i]] + 1
        	else:
        		maxLength = max(maxLength, i - start + 1)
        	usedChar[s[i]] = i
        return maxLength
```

<blockquote class="blockquote-center">有了我，LeetCode的AC率恐怕。。。 </blockquote>