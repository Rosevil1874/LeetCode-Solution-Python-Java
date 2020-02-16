# 395 - [至少有k个重复字符的最长子串](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)


## 题解
1. 有效子序列中每个字母都至少出现k次；
2. 如果一个序列中有某个字母出现的次数少于k次，那么这个字母将原序列分割为多个可能有效的子序列
3. 再依次检查子序列是否有效，并找出长度最大的子序列。
```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(substr, k) for substr in s.split(c))
        return len(s)
```