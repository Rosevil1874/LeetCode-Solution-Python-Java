# 64 - 最小路径和


## DP
**时间复杂度：O(n^2)  
空间复杂度：O(m\*n)**

**思路**
1. 每次只能向下或者向右移动一步，则当机器人到达某一点时有以下两种情况,要得到最短路径，就从这两种情况中选择一个路径最短的：
	1. 从上面的格子下来p[i - 1][j]；
	2. 从左边的格子过来p[i][j - 1]；
2. 由第一条得出状态方程：  
	1. p[i][j]: 机器人走到(i, j)处的路径长度；
    2. p[0][j] = sum(p[0][0]...p[0][j])
    3. p[i][0] = sum(p[0][0]...p[i][0])
	4. p[i][j] = min(p[i - 1][j] + p[i][j - 1]) + p[i][j] if (i > 0 and j > 0)


```java
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    grid[i][j] = grid[i][j];
                } else if (i == 0) {
                    grid[i][j] = grid[i][j - 1] + grid[i][j];
                } else if (j == 0) {
                    grid[i][j] = grid[i - 1][j] + grid[i][j];
                } else {
                    grid[i][j] = Math.min(grid[i - 1][j] , grid[i][j - 1]) + grid[i][j];
                }
            }
        }
        return grid[m - 1][n - 1];
    }
}
```
