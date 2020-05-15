# 96 - 不同的二叉搜索树

## 题目描述
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?


## 动态规划
天哪[这个解答](https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/)简直amazing，仔细看解释，虽然很大一段但是很清楚的。

```python
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0] = G[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]   
```
