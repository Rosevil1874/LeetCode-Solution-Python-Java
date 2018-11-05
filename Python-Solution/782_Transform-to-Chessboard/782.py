class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)

        # case1:任意矩形四个角不会出现奇数个的0或1，若异或结果为1则说明有奇数个1
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(N) for j in range(N)):
        	return -1

        # case2：检查第一行和第一列中1的个数是否满足为N/2或(N+1)/2.
        if not N // 2 <= sum(board[0]) <= (N + 1) // 2:
        	return -1
        if not N // 2 <= sum(board[i][0] for i in range(N)) <= (N + 1) // 2:
        	return -1

        # 第一行和第一列中与“01010101...”这个排列对应的元素个数，分别对应不需要移动的列和行的个数
        col = sum(board[0][i] == i % 2 for i in range(N))
        row = sum(board[i][0] == i % 2 for i in range(N))

        # 矩阵规模为奇数时，取交换偶数次的情况(偶数次较少)
        if N % 2:
        	if col % 2: col = N - col
        	if row % 2: row = N - row
        # 矩阵规模为偶数时，使用min函数取交换次数最少的情况
        else:
        	col = min(N - col, col)
        	row = min(N - row, row)

        # 返回行和列中交换次数较少的情况
        return (col + row)//2
        
# board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
board = [[1,1,0],[0,0,1],[0,0,1]]
# board = [[0, 1], [1, 0]]
# board = [[1, 0], [1, 0]]
s = Solution()
r = s.movesToChessboard(board)
print(r)
    