# 200 - [岛屿数量](https://leetcode.com/problems/number-of-islands/)

## 题目描述
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 2:**

Input:
11000   
11000  
00100  
00011  

Output: 3


## DFS
遍历每一个格子，如果它属于岛屿(grid[i][j]==1)则标记其所有相邻格子(DFS)，岛屿数量加一。

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt
    
    
    def dfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'    # 标记访问
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
```