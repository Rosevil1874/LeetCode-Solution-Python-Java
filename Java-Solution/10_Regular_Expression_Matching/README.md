# 10 - 正则表达式匹配

**迷迷糊糊**
**此题有待深究 哦哦哦**

## 题目描述
![problem](images/10.png)

<!-- more -->

## 递归一：超时
剑指offer上有一道[正则表达式匹配](https://github.com/Rosevil1874/CS_Python_Notes/blob/master/sword_points_offer/python_solution/52%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%8C%B9%E9%85%8D.md)，题意是一样的，参考了当时的解答。

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        
        # string和pattern完全匹配
        if len_s == 0 and len_p == 0:
            return True
        
        # string遍历完却未匹配完
        if len_s != 0 and len_p == 0:
            return False
        
        # pattern第二个字符是*
        if len_p > 1 and p[1] == '*':
            if len_s > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
            
        # pattern第二个字符不是*，直接判断
        if len_s > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False
```


## 递归二
>cr:[Regular Expression Matching](https://articles.leetcode.com/regular-expression-matching/)

>Think   
carefully how you would do matching of ‘\*’. Please note that ‘\*’ in regular expression is different from wildcard matching, as we match the previous character 0 or more times. But, how many times? If you are stuck, recursion is your friend.
1. If the next character of p is NOT ‘\*’, then it must match the current character of s. Continue pattern matching with the next character of both s and p.
2. If the next character of p is ‘\*’, then we do a brute force exhaustive matching of 0, 1, or more repeats of current character of p… Until we could not match any more characters.


1. 若正则表达式的长度为0，字符串长度也为0时匹配，否则不匹配；
2. 若正则表达式的长度为1，当字符串长度也为1，且两字符相等或表达式为'.'时匹配，否则不匹配；
3. 由于正则表达式中'\*'只能出现在字符后，所以从第二个字符（下标为1）开始判断。
4. 若正则表达式第二个字符非'\*'，且字符串长度为0，不匹配。若其为'\*'，则第一个字符匹配且后面的剩余部分都匹配（这里使用递归判断子串是否匹配）就匹配。
5. 若正则表达式第二个字符为'\*'，则字符串的第一个字符一定是匹配的。接下来递归判断字符串与表达式第三个字符开始的子串是否匹配，若匹配返回True。否则判断字符串第二个字符开始的子串与表达式是否匹配（一个个字符一次与与'\*'匹配）。


```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        
        if len_p == 0:
            return len_s == 0
        
        if len_p == 1:
            return len_s == 1 and (s[0] == p[0] or p[0] == '.')
        
        if p[1] != '*':
            if len_s == 0:
                return False
            elif s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) and (s[0] == p[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])
```


## 动态规划
>cr:[leetcode 10 Regular Expression Matching](http://www.voidcn.com/article/p-wzvbljqo-ys.html)

This problem has a typical solution using Dynamic Programming. We define the state P[i][j] to be true if s[0..i) matches p[0..j) and false otherwise. Then the state equations are: 
>1. P[i][j] = P[i - 1][j - 1], if p[j - 1] != ‘\*’ && (s[i - 1] == p[j - 1] || p[j - 1] == ‘.’); 
2. P[i][j] = P[i][j - 2], if p[j - 1] == ‘\*’ and the pattern repeats for 0 times; 
3. P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == ‘.’), if p[j - 1] == ‘\*’ and the pattern repeats for at least 1 times. 

Putting these together, we will have the following code.

以下代码关于dp[i][j]的定义与以上分析相反，即dp[i][j]为True表示p[0..i) matches s[0..j)。比楼上递归快多了。

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        
        # dp[0][0]为True，其他均为False（两个空串match）
        dp = [[True] + [False] * len_s]
        for i in range(len_p):
            dp.append([False]*(len_s+1))

        for i in range(1, len_p + 1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in range(1, len_s+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[len_p][len_s]
```

## 使用第三方库re
一行代码/微笑脸
```python
import re

class Solution:
    def isMatch(self, s, p):
        return re.match('^' + p + '$', s) != None
```