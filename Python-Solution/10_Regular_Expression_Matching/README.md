# 10 - 正则表达式匹配

**此题有待深究 哦哦哦**

## 题目描述
![problem](images/10.png)

<!-- more -->

自己的思路：
1. 由于*控制的是其前面字符的匹配，因此可以由正则表达式的末尾开始检查；
2. 没了。。没了。。。直接用字符串的方法肯定是不行的，越想越复杂。。

↓↓别人的思路
<blockquote class="blockquote-center">If you are stuck, recursion is your friend.</blockquote>

## 递归
>cr:[[LeetCode] Regular Expression Matching 正则表达式匹配](http://www.cnblogs.com/grandyang/p/4461713.html)

**这个代码还没调通，递归调用函数出错，作用域问题**

```pythhttps://blog.csdn.net/wangyaninglm/article/details/55827721on
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_len = len(s)
        p_len = len(p)
        if s_len == 0 and p_len == 0:
            return False

        if s_len == 1 and p_len == 1:
            if s[0] == p[0] or p[0] == '.':
                return True
            else:
                return False

        if p[1] != '*':
            if s_len == 0:
                return False
            if s[0] == p[0] or p[0] == '.':
                return isMatch(self, s[1:], p[1:])
            else:
                return False

        while len(s) and (s[0] == p[0] or p[0] == '.'):
            if isMatch(self, s, p[2:]):
                return True        
            s = s[1:]
        return isMatch(self, s, p[2:])
```

## 动态规划
>cr:[leetcode 10 Regular Expression Matching](https://blog.csdn.net/wangyaninglm/article/details/55827721)

This problem has a typical solution using Dynamic Programming. We define the state P[i][j] to be true if s[0..i) matches p[0..j) and false otherwise. Then the state equations are: 
a. P[i][j] = P[i - 1][j - 1], if p[j - 1] != ‘*’ && (s[i - 1] == p[j - 1] || p[j - 1] == ‘.’); 
b. P[i][j] = P[i][j - 2], if p[j - 1] == ‘*’ and the pattern repeats for 0 times; 
c. P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == ‘.’), if p[j - 1] == ‘\*’ and the pattern repeats for at least 1 times. 
Putting these together, we will have the following code.

```python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_len = len(s)
        p_len = len(p)
        dp = [[True] + [False] * s_len]
        for i in range(p_len):
            dp.append([False]*(s_len+1))

        for i in range(1, p_len + 1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in range(1, s_len+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[p_len][s_len]
```

## 使用第三方库re
一行代码/微笑脸
```python
import re

class Solution:
    def isMatch(self, s, p):
        return re.match('^' + p + '$', s) != None
```