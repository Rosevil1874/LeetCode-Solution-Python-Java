class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 

        # 获取四条边上点的坐标
        m, n = len(board), len(board[0])
        queue = [x for y in range(max(m, n)) for x in ((0, y), (m - 1, y), (y, 0), (y, n - 1))]
        
        # BFS：依次检查边上是否为'O'
        while queue:
            i, j = queue.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                queue += (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)

        # 将'O'替换成'X'，'T'替换回'O'
        for row in board:
            for i, c in enumerate(row):
                if c == 'O':
                    row[i] = 'X'
                elif c == 'T':
                    row[i] = 'O'
        

s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)
print(board)