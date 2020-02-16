# 329 - [矩阵中的最长递增路径](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)


## DFS
```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 计算当前cell开始的最长路径
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                # 最长路径为当前cell加上四个方向中最长的路径，下一cell的值大于当前cell
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i - 1 >= 0 and matrix[i - 1][j] > val else 0,
                    dfs(i, j - 1) if j - 1 >= 0 and matrix[i][j - 1] > val else 0,
                    dfs(i + 1, j) if i + 1 < m and matrix[i + 1][j] > val else 0,
                    dfs(i, j + 1) if j + 1 < n and matrix[i][j + 1] > val else 0
                )
            return dp[i][j]
        
        
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        # 计算从每个cell开始的最长路径，最后求最大值
        for i in range(m):
            for j in range(n):
                dp[i][j] = dfs(i, j)
        return max(max(row) for row in dp)
```
