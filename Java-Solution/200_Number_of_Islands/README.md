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

```Java
class Solution {
    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '0';   // 标记遍历过的点
        dfs(grid, i - 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i + 1, j);
        dfs(grid, i, j + 1);
        
    }

    public int numIslands(char[][] grid) {
        if (grid == null) return 0;
        int cnt = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    cnt++;
                }
            }
        }
        return cnt;
    }
}
```