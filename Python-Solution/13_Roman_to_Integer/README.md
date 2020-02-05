# 13 - 罗马数字转整数

## 题目描述
![problem](images/13.png)

<!-- more -->

## 罗马数字
我觉得这位兄台的和百科差不多，又比百科美观，就借过来用用嘻嘻。
![RomanNumber](images/RomanNumber.png)

## 整数转罗马数字
cr: [leetcode 罗马数字与整数的转换算法](https://blog.csdn.net/net_wolf_007/article/details/51770112)

idea: 
1. 用“放在大数左边的数字只能使用一个”的特点来判断对当前字母是加还是减。
2. 若后一个字符代表的数比当前字符代表的数字小，则使用加法，否则使用减法。

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        if s == '':
            return 0
        
        num = 0
        n = len(s)
        ref = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        for i in range(n):
            if i + 1 >= n or ref[s[i + 1]] <= ref[s[i]]:
                num += ref[s[i]]
            else:
                num -= ref[s[i]]
                
        return num
```