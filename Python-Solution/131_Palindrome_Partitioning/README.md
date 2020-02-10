# 131 - 分割回文串

## 题目描述
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

**Example:**

	Input: "aab"
	Output:
	[
	  ["aa","b"],
	  ["a","a","b"]
	]


## 题解

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # path：当前划分长的的回文串
        # res：不同划分长度的回文串集合
        def dfs(s, path, res):
            # 若s遍历结束，完成一次划分，将path添加到结果res中
            if not s:
                res.append(path[:])
                return
            # 划分s或其子串
            for i in range(1, len(s) + 1):
                # 若为回文，添加到path，递归判断余下子串
                if s[:i] == s[i - 1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()
        
        res = []
        dfs(s, [], res)
        return res
```