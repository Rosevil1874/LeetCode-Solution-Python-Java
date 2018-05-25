row = len(grid)
        col = len(grid[0])
        
        def dfs(i, j):
            if i >= 0 and i < row and j >= 0 and j < col and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) +dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(row) for j in range(col) if grid[i][j] ]
        return max(areas) if areas else 0

        
        
s = Solution()
grid = [
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
res = s.maxAreaOfIsland(grid)
print(res)