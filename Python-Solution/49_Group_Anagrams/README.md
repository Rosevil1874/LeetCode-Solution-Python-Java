# 49 - 

## 题目描述
Given an array of strings, group anagrams together.

**Example:**
**Input:** ["eat", "tea", "tan", "ate", "nat", "bat"],
**Output:**
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

**Note:**
All inputs will be in lowercase.
The order of your output does not matter.


```python
class Solution:
    def groupAnagrams(self, strs) :
        d = {}
        for word in strs:
            key = ''.join(sorted(word))
            d[key] = d.get(key, []) + [word]
        return list(d.values())
```