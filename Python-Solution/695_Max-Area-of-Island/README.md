# 695 - 岛屿的最大面积

## 题目描述
![problem](images/695.png)

## DFS
### 原始代码
**空间复杂度O(1)**
```python
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
        	return 0

        row = len(grid)
        col = len(grid[0])
        maxArea = 0
        for i in range(row):
        	for j in range(col):
        		if grid[i][j] == 1:
        			area = self.dfs(grid, i, j, row, col, 0)
        			maxArea = max(maxArea, area)
        return maxArea


    def dfs(self, grid, i, j, row, col, area):
    	if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
    		return area
    	grid[i][j] = 0
    	area += 1
    	area = self.dfs(grid, i + 1, j, row, col, area)
    	area = self.dfs(grid, i - 1, j, row, col, area)
    	area = self.dfs(grid, i, j + 1, row, col, area)
    	area = self.dfs(grid, i, j - 1, row, col, area)
    	return area
```

### 进阶代码
**空间复杂度O(n)**
```pyhton
row = len(grid)
        col = len(grid[0])
        
        def dfs(i, j):
            if i >= 0 and i < row and j >= 0 and j < col and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) +dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(row) for j in range(col) if grid[i][j] ]
        return max(areas) if areas else 0
```
