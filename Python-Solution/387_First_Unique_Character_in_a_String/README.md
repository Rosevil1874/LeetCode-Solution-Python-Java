# 387 - 字符串中的第一个唯一字符

## 题目描述
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

**Examples:**
	s = "leetcode"
	return 0.

	s = "loveleetcode",
	return 2.

**Note:** You may assume the string contain only lowercase letters.


## 1. two pass
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for idx, c in enumerate(s):
            if freq[ord(c) - ord('a')] == 1:
                return idx
        return -1
```

使用collections.Counter:
```python
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter.get(c, 0) == 1:
                return i
        return -1
```

## 2. one pass
(1)set + dict
```python
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        dic = dict()
        for i, c in enumerate(s):
            if c not in seen:
                dic[c] = i
                seen.add(c)
            elif c in dic:
                del dic[c]
        return min(dic.values()) if dic else -1
```

(2) count
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        uniq = [s.index(l) for l in letters if s.count(l) == 1]
        return min(uniq) if len(uniq) > 0 else -1
```

```python
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return -1
```