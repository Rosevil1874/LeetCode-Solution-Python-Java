class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)       # 行数
        if n == 0:
            return 0

        m = len(obstacleGrid[0])    # 列数
        prev = curr = [1] + [0] * (m - 1)
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif j > 0:
                    curr[j] = prev[j] + curr[j - 1]
            prev, curr = curr, prev
        return prev[m - 1]


inp = [[1],[0]]
# inp = [[1,0]]        
# inp = [[1]]        
# inp = [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
s = Solution()
r = s.uniquePathsWithObstacles(inp)
print(r)
