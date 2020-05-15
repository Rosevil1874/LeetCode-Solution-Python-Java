# 221 - [最大正方形](https://leetcode.com/problems/maximal-square/)

## 题目描述
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Example:**
input:
	1 0 1 0 0
	1 0 1 1 1
	1 1 1 1 1
	1 0 0 1 0
output:
	4


## 题解
1. DP[i][j]代表以matrix[i][j]为右下角的最大全为'1'的正方形边长。
2. 状态转移方程：
	DP[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
3. 初始状态：最上一行和最左一列最多构成边长为一的正方形
	- DP[i][0] = matrix[i][0] - '0'
	- DP[0][j] = matrix[0][j] - '0'

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_len = 0
        
        for i in range(m):
            for j in range(n):
                if not i or not j or matrix[i][j] == '0':
                    dp[i][j] = 0 if matrix[i][j] == '0' else 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                max_len = max(max_len, dp[i][j])
        return max_len**2

```