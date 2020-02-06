# 38 - 外观数列

## 题目描述
The count-and-say sequence is the sequence of integers with the first five terms as following:
	1.     1
	2.     11
	3.     21
	4.     1211
	5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

## 题解
第i+1个数是第i个数的count and say，所以一个一个接着计算就行。

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        start = '1'
        for i in range(n - 1):
            start = self.cnt_say(start)
        return start
        
        
    def cnt_say(self, s: str) -> str:
        res = ''
        cnt = 1
        s += '#'    # 哨兵
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                cnt += 1
                continue
            else:
                res += str(cnt) + s[i]
                cnt = 1
        return res
```
