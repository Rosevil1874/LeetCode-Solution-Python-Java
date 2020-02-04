# 242 - 有效的字母异位词

## 题目描述
Given two strings s and t , write a function to determine if t is an anagram of s.


## 1. collections.Counter

```python
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

## 2. dict(存字符)
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = dict(), dict() 
        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        return dict_s == dict_t
```


## 3. dict(存字符的字典顺序)
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = [0] * 26, [0] * 26
        for c in s:
            dict_s[ord(c) - ord('a')] += 1
        for c in t:
            dict_t[ord(c) - ord('a')] += 1
        return dict_s == dict_t
```


## 4. sort
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```