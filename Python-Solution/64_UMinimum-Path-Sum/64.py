class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    
        n = len(grid)       # 行数
        if n == 0:
            return 0

        m = len(grid[0])    # 列数
        curr = [ grid[0][0] ] * m

        # 计算到第一行每个格子的路径长度
        for j in range(1, m):
            curr[j] = curr[j-1] + grid[0][j]
        for i in range( 1, n ):
            curr[0] += grid[i][0]
            for j in range( 1, m ):
                curr[j] = min(curr[j-1], curr[j]) + grid[i][j]
        return curr[m-1]
       
inp = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
s = Solution()
r = s.minPathSum(inp)
print(r)
