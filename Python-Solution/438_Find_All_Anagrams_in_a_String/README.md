# 438 - 找到字符串中所有字母异位词 

## 题目描述
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

**Example 1:**

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".



### 题解：滑动窗口
使用Counter计算滑动窗口内每个字符出现次数，若窗口内的字符频率与p中相同则将窗口起始坐标加入结果数组。

> Runtime: 156 ms, faster than 36.03% of Python3 online submissions.

```python
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(p)
        win_p = Counter(p)
        win_s = Counter(s[:n-1])
        
        for i in range(len(s) - n + 1):
            win_s[s[i + n - 1]] += 1    # 窗口加上最右值
            if win_s == win_p:
                res.append(i)
            win_s[s[i]] -= 1    # 窗口向右滑动，去掉最左值
            if not win_s[s[i]]:
                del win_s[s[i]]
        return res
```

同样的方法，使用defaultdict会快很多：

> Runtime: 104 ms, faster than 82.86% of Python3 online submissions.

```python
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(p)
        win_p, win_s = defaultdict(int), defaultdict(int)
        for x in p:
            win_p[x] += 1
        for x in s[:n-1]:
            win_s[x] += 1
        
        for i in range(len(s) - n + 1):
            win_s[s[i + n - 1]] += 1    # 窗口加上最右值
            if win_s == win_p:
                res.append(i)
            win_s[s[i]] -= 1    # 窗口向右滑动，去掉最左值
            if not win_s[s[i]]:
                del win_s[s[i]]
        return res
```